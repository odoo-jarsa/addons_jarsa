# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


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
    prod_id = fields.Many2one(
        string='Product', related='order_id.product_id')
    user_id = fields.Many2one(
        string='Responsable', related='order_id.user_id')
    # lot_id = fields.Char(
    #     string="Lote", related="order_id.move_created_ids2")

    def print_report(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        state = self.pool['mrp.production'].browse(cr, uid, ids, context=context)
        datas = {'ids': context.get('active_ids', [])}
        res = self.read(cr, uid, ids, [
            'lote_impresion', 'lote_corte', 'descripcion',
            'parte', 'auditor', 'bar_code',
            'cantidad', 'label_type', 'order_id', 'prod_id', 'user_id'
            ], context=context)
        res = res and res[0] or {}
        datas['form'] = res
        if res.get('id', False):
            datas['ids'] = [res['id']]
        for rec in state:
            rec.state = 'done'
        datas['form']['lote_impresion'] = state.move_created_ids2.lot_ids.name
        return self.pool['report'].get_action(
            cr, uid, [],
            'mrp_workflow_print_label.label_qweb',
            data=datas, context=context)
