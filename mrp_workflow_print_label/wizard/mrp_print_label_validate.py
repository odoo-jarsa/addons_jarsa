# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MrpPrintLabelValidate(models.TransientModel):
    _name = 'mrp.print.label.validate'

    user_id = fields.Many2one('res.users')
    pin = fields.Integer(
        'Field Label',
    )

    def validate(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        res = self.read(cr, uid, ids, ['user_id', 'pin'], context=context)
        user = self.pool['res.users'].browse(
            cr, uid, res[0]['user_id'][0], context=context)
        if(user.mrp_pin == res[0]['pin']):
            production_id = context.get('active_id', False)
            mrp = self.pool['mrp.production'].browse(
                cr, uid, production_id, context=context)
            mrp.message_post(body="user: %s" % user.name)
        else:
                print 'pin invalido'
        view_id = self.pool.get('ir.model.data').get_object_reference(
                cr, uid, 'mrp_workflow_print_label', 'mrp_print_label_wizard')
        return {
            'name': "MRP Workflow Print Label Wizard",
            'view_mode': 'form',
            'view_id': view_id[1],
            'view_type': 'form',
            'res_model': 'mrp.print.label',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
