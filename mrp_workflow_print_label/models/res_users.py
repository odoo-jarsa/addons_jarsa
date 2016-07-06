# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    pin = fields.Integer(
        string='PIN', readonly=True,
    )
