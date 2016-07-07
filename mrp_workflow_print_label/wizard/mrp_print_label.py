# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class MrpPrintLabel(models.TransientModel):
    _name = 'mrp.print.label'

    lote_impresion = fields.Char(string="Lote", readonly=True)
    lote_corte = fields.Char(string='Lote de Descripcion')
    descripcion = fields.Char(string='Nombre del Producto')
    parte = fields.Char(string='No.Parte')
    auditor = fields.Char(string='Auditor/Inspector')
    bar_code = fields.Char(string='Codigo de Barras')
    cantidad = fields.Char(string='Cantidad')
    order_id = fields.Many2one(
        'mrp.production', string="Order", readonly=True)

    @api.multi
    def print_report(self):
        self.order_id.write({
            'lote_impresion': self.lote_impresion,
            'lote_corte': self.lote_corte,
            'descripcion': self.descripcion,
            'parte': self.parte,
            'auditor': self.auditor,
            'bar_code': self.bar_code,
            'cantidad': self.cantidad,
            'state': 'done',
            })
        self.order_id.message_post(body="user:")
        context = dict(
            self.env.context or {},
            active_ids=[self.order_id.id],
            active_model='mrp.production')
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'mrp_workflow_print_label.label_qweb',
            'context': context,
          }
