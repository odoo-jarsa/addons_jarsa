from openerp import models, fields


class Wizard(models.TransientModel):
    _name = 'mrp_print_label'
    _inherit = 'mrp.production'

    def _default_session(self):
        return self.env['mrp.production'].browse(
            self._context.get('active_id'))

    lote_impresion = fields.Char(string='Lote de Impresion')
    lote_corte = fields.Char(string='Lote de Descripcion')
    descripcion = fields.Char(string='Nombre del Producto')
    parte = fields.Char(string='No.Parte')
    auditor = fields.Char(string='Auditor/Inspector')
    lote_pintura = fields.Char(string='Lote de Pintura')
    bar_code = fields.Char(string='Codigo de Barras')
    label_type = fields.Selection([
        ('cover', 'Cover'),
        ('telas', 'Telas'),
        ], string='Tipo de Etiqueta')

    def action_print():
        return True
