# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MrpPrintReason(models.Model):
    _name = 'mrp.print.reason'
    _description = 'Reason for reprinting label'

    name = fields.Char(required=True)
