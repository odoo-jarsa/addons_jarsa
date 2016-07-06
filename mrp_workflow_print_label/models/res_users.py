# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    mrp_pin = fields.Integer(
        string='PIN',
    )

    # def _check_unique_pin(self, cr, uid, ids, context=None):

    #     record = self.browse(cr, uid, ids, context=context)
    #     pin_codes = []

    #     for data in record:

    #         if data.mrp_pin > 999:
    #             pin_codes = self.search(
    #                 cr, uid, [(
    #                     'mrp_pin', '=', data.mrp_pin), ('id', '!=', data.id)])

    #             if len(pin_codes) > 0:
    #                 return False
    #             else:
    #                 return True
    #         else:
    #             return True

    # _constraints = [(
    #     _check_unique_pin,
    #     'Error: This PIN code is invalid or assigned to other user.', [
    #         'mrp_pin'])]
