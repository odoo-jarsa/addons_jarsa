# -*- coding: utf-8 -*-
# Copyright 2017, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    @api.multi
    def new_crm_lead(self):
        obj_crm = self.env['crm.lead']
        partner = (
            self.partner_id.parent_id.id
            if self.partner_id.parent_id
            else self.partner_id.id)
        contact_name = self.partner_id.name
        title = self.partner_id.title.id if self.partner_id.title else False

        obj_crm.create({
            'name': self.name,
            'partner_id': partner,
            'team_id': 1,
            'type': 'lead',
            'email_from': self.partner_email,
            'contact_name': contact_name,
            'title': title,
        })

        stage = self.env['helpdesk.stage'].search(
            [('is_close', '=', True)])
        self.stage_id = stage[-1].id
