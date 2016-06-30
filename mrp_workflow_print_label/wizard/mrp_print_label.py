from openerp import models, fields


class MrpPrintLabel(models.TransientModel):
    _name = 'mrp.print.label'

    lote_impresion = fields.Char(string='Lote de Impresion')
    lote_corte = fields.Char(string='Lote de Descripcion')
    descripcion = fields.Char(string='Nombre del Producto')
    parte = fields.Char(string='No.Parte')
    auditor = fields.Char(string='Auditor/Inspector')
    lote_pintura = fields.Char(string='Lote de Pintura')
    bar_code = fields.Char(string='Codigo de Barras')
    label_type = fields.Selection([
        ('cover', 'Cover'),
        ('telas', 'Telas')], string='Tipo de Etiqueta')
    order_id = fields.Many2one(
        'mrp.production', string="Order", readonly=True)

    def action_print():
        return True

    # @api.multi
    # def print_report(self, context=None):
    #     datas = {}
    #     if context is None:
    #         context = {}
    #     data = self.read(cr, uid, ids)[0]
    #     datas = {
    #                  'ids': [],
    #                  'model': 'object.object',
    #                  'form': data
    #     }
    #     return {'type': 'ir.actions.report.xml', 'report_name': 'label_report', 'datas': datas}