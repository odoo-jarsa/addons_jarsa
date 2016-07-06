# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MrpPrintLabel(models.TransientModel):
    _name = 'mrp.print.label'

    lote_impresion = fields.Char(string='Lote de Impresion')
    lote_corte = fields.Char(string='Lote de Descripcion')
    descripcion = fields.Char(string='Nombre del Producto')
    parte = fields.Char(string='No.Parte')
    auditor = fields.Char(string='Auditor/Inspector')
    lote_pintura = fields.Char(string='Lote de Pintura')
    bar_code = fields.Char(string='Codigo de Barras')
    cantidad = fields.Char(string='cantidad')
    label_type = fields.Selection([
        ('cover', 'Cover'),
        ('telas', 'Telas')], string='Tipo de Etiqueta')
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
        datas = {'ids': context.get('active_ids', [])}
        res = self.read(cr, uid, ids, [
            'lote_impresion', 'lote_corte', 'descripcion',
            'parte', 'auditor', 'lote_pintura', 'bar_code',
            'cantidad', 'label_type', 'order_id', 'prod_id', 'user_id'
            ], context=context)
        res = res and res[0] or {}
        datas['form'] = res
        if res.get('id', False):
            datas['ids'] = [res['id']]

        self.pool['mrp.production'].signal_workflow(
                cr, uid, [res['order_id'][0]], 'done')

        return self.pool['report'].get_action(
            cr, uid, [],
            'mrp_workflow_print_label.label_qweb',
            data=datas, context=context)
