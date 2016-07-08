# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class MrpPrintLabelValidate(models.TransientModel):
    _name = 'mrp.print.label.validate'

    pin = fields.Char(string='PIN')
    order_id = fields.Many2one('mrp.production')

    @api.multi
    def validate(self):
        user = self.env['res.users'].search(
            [('mrp_pin', '=', self.pin)])
        if len(user) == 0 or self.pin is False:
            raise UserError(_('Invalid PIN'))
        else:
            self.order_id.message_post(body=_(
                "Re-Print Authorized by: %s") % user.name)
            context = dict(
                self.env.context or {},
                active_ids=[self.order_id.id],
                active_model='mrp.production')
            if self.order_id.report_type == 'cover':
                report_name = 'mrp_workflow_print_label.label_qweb'
            else:
                report_name = 'mrp_workflow_print_label.label_cloth'

            return {
                'type': 'ir.actions.report.xml',
                'report_name': report_name,
                'context': context,
<<<<<<< Updated upstream
                'docs': self.order_id.id
=======
>>>>>>> Stashed changes
            }
