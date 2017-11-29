# -*- coding: utf-8 -*-
# Copyright 2016, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    @api.model
    def close_tickets(self):
        parameter = self.env['ir.config_parameter'].get_param(
            'helpdesk_auto_close', False)
        if parameter:
            value = parameter.split('/')
        tickets_authorized = self.search([('stage_id', '=', int(value[1]))])
        stage_close = self.env['helpdesk.stage'].search([
            ('is_close', '=', True)], order='sequence', limit=1).id
        for ticket in tickets_authorized:
            times = [fields.Datetime.from_string(x)
                     for x in ticket.message_ids.mapped('date')]
            date_end = times[0]
            date_now = fields.Datetime.from_string(fields.Datetime.now())
            direfencia = date_now - date_end
            if direfencia.days >= int(value[0]):
                ticket.stage_id = stage_close
