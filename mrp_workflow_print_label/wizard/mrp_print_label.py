# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class MrpPrintLabel(models.TransientModel):
    _name = 'mrp.print.label'

    company_id = fields.Many2one('res.company')
    lote_impresion = fields.Char(string="Lote de Impresion", readonly=True)
    lote_corte = fields.Char(string='Lote de Descripcion')
    descripcion = fields.Char(string='Nombre del Producto')
    parte = fields.Char(string='No.Parte')
    auditor = fields.Char(string='Auditor/Inspector')
    cantidad = fields.Char(string='Cantidad')
    order_id = fields.Many2one(
        'mrp.production', string="Order", readonly=True)

    @api.multi
    def print_report(self):
        self.order_id.write({
            'lote_impresion': self.order_id.move_created_ids2.lot_ids.name,
            'lote_corte': self.lote_corte,
            'descripcion': self.descripcion,
            'parte': self.parte,
            'auditor': self.auditor,
            'cantidad': self.cantidad,
            'state': 'done',
            })
        self.order_id.message_post(
            body="Printed by: %s" % (self.order_id.user_id.name))
        context = dict(
            self.env.context or {},
            active_ids=[self.order_id.id],
            active_model='mrp.production')

        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'mrp_workflow_print_label.label_qweb',
            'context': context,
            'docs': self.order_id.id
          }
