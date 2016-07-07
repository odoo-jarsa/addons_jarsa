# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    state = fields.Selection(
            [('draft', 'New'),
             ('cancel', 'Cancelled'),
             ('confirmed', 'Awaiting Raw Materials'),
             ('ready', 'Ready to Produce'),
             ('in_production', 'Production Started'),
             ('print_label', 'Print Label'),
             ('done', 'Done')])
    lote_impresion = fields.Char(string="Lote", readonly=True)
    lote_corte = fields.Char(string='Lote de Descripcion', readonly=True)
    descripcion = fields.Char(string='Nombre del Producto', readonly=True)
    parte = fields.Char(string='No.Parte', readonly=True)
    cantidad = fields.Char(string='Cantidad', readonly=True)
    auditor = fields.Char(string='Auditor/Inspector', readonly=True)
    bar_code = fields.Char(string='Codigo de Barras', readonly=True)

    @api.multi
    def action_state_print_label(self):
        for rec in self:
            rec.state = 'print_label'
            rec.message_post(body='Printing test')
