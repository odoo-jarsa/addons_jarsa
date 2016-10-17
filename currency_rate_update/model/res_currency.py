# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from openerp import models, fields, api, _
from openerp import exceptions
from ..services import update_service_MX_BdM
from datetime import date, datetime
from pytz import timezone

_logger = logging.getLogger(__name__)

import openerp
from openerp.osv import osv

class res_currency(osv.osv):
    _inherit = 'res.currency'
    _name = 'res.currency'

    def _get_current_rate(self, cr, uid, ids, name, arg, context=None):
        if context is None:
            context = {}
        res = {}
        date = context.get('date') or fields.Datetime.now()
        company_id = context.get('company_id') or self.pool['res.users']._get_company(cr, uid, context=context)
        for id in ids:
            cr.execute("""SELECT rate FROM res_currency_rate 
                           WHERE currency_id = %s
                             AND name::DATE <= %s::DATE
                             AND (company_id is null
                                 OR company_id = %s)
                        ORDER BY company_id, name desc LIMIT 1""",
                       (id, date, company_id))
            if cr.rowcount:
                res[id] = cr.fetchone()[0]
            else:
                res[id] = 1
        return res


    _columns = {
        'rate': openerp.osv.fields.function(_get_current_rate, string='Current Rate', digits=(12,6),
            help='The rate of the currency to the currency of rate 1.'),
    }

res_currency()

class CurrencyRate(models.Model):
    _inherit = 'res.currency'
    _name = 'res.currency'

    @api.one
    def refresh_currency(self):        
        """Refresh the currencies rates !!for all companies now"""
        _logger.info('  ** Starting to refresh currencies with service %s', self.name)
        context = dict(self._context)
        rate = 0.0
        date_cron = '%s'%(context.get('date_cron'))

        rate_obj = self.env['res.currency.rate']
        rate_brw = rate_obj.search([('name', 'like', date_cron), ('currency_id', '=', self.id)])
        rate = update_service_MX_BdM.rate_retrieve()
        if rate != 0.0 :
            vals = {
                'name': date_cron,
                'currency_id': self.id,
                'rate': rate
            }
            if not rate_brw:
                rate_obj.create(vals)
                _logger.info('  ** Create currency %s -- date %s --rate %s ',self.name, date_cron, rate)
            else:
                rate_obj.write(vals)
                _logger.info('  ** Update currency %s -- date %s --rate %s',self.name, date_cron, rate)
        try:
            rate_obj = self.env['res.currency.rate']
            rate_brw = rate_obj.search([('name', 'like', date_cron), ('currency_id', '=', self.id)])
            rate = update_service_MX_BdM.rate_retrieve()
            if rate != 0.0 :
                vals = {
                    'name': date_cron,
                    'currency_id': self.id,
                    'rate': rate
                }
                if not rate_brw:
                    rate_obj.create(vals)
                    _logger.info('  ** Create currency %s -- date %s --rate %s ',self.name, date_cron, rate)
                else:
                    rate_obj.write(vals)
                    _logger.info('  ** Update currency %s -- date %s --rate %s',self.name, date_cron, rate)
        except:
            pass
        return rate

    @api.multi
    def run_currency_update(self):
        _logger.info(' === Starting the currency rate update cron')
        tz = self.env.user.tz
        date_cron = fields.Date.today()
        if tz:
            hora_factura_utc = datetime.now(timezone("UTC"))
            hora_factura_local = hora_factura_utc.astimezone(timezone(tz))
            date_cron = hora_factura_local.date()
        services = {
            'cron': True,
            'date_cron': date_cron
        }
        res = self.search([('name', '=', 'MXN')]).with_context(**services).refresh_currency()
        _logger.info(' === End of the currency rate update cron')
        return res

    @api.model
    def _run_currency_update(self):
        self.run_currency_update()

    @api.multi
    def update_currency_rate(self):
        self.run_currency_update()        