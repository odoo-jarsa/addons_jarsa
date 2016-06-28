# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    state = fields.selection([
        ('draft', 'New'),
        ('cancel', 'Cancelled'),
        ('confirmed', 'Awaiting Raw Materials'),
        ('ready', 'Ready to Produce'),
        ('in_production', 'Production Started'),
        ('print', 'Print Report'),
        ('done', 'Done')],
        string='Status', readonly=True,
        track_visibility='onchange', copy=False,
        help=("When the production order is created the status is set to "
              "'Draft'.If the order is confirmed the status is set to "
              "'Waiting Goods'.If any exceptions are there, the status is "
              "set to 'Picking Exception'.If the stock is available then the "
              "status is set to 'Ready to Produce'.When the production gets "
              "started then the status is set to 'In Production'.When the "
              "production is over, the status is set to 'Done'.")
        )

    def action_print_report(self):
        return True
