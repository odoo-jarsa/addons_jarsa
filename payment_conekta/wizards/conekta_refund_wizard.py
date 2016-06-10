# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models
# from openerp.tools.translate import _

import logging
_logger = logging.getLogger(__name__)

try:
    import conekta
except:
    _logger.debug('Cannot `import conekta`.')


class ConektaRefundWizard(models.TransientModel):
    _name = 'conekta.refund.wizard'

    message = fields.Text(placeholder="Motive of refund", required=True)
    sale_order_id = fields.Many2one('sale.order', readonly=True)
    amount = fields.Float(string='Amount to refund', required=True)

    @api.multi
    def conekta_refund_card(self):
        acquirer = self.env.ref('payment_conekta.payment_acquirer_conekta')
        tx = self.sale_order_id.payment_tx_id
        conekta.api_key = acquirer.conekta_private_key
        charge = conekta.Charge.find(tx.acquirer_reference)
        so_price = self.sale_order_id.order_line.price_unit
        transaction = self.env['payment.transaction']
        if self.amount < so_price:
            charge.refund(amount=int(self.amount*100))
            self.sale_order_id.message_post_with_template(self.env.ref(
                    'payment_conekta.email_template_partially_action').id)
        else:
            tx.state = 'cancel'
            charge.refund()
            self.sale_order_id.message_post_with_template(self.env.ref(
                    'payment_conekta.email_template_cash_back').id)
        tx_ids = transaction.search(
            [('sale_order_id', '=', tx.sale_order_id.id)])
        list_tx = []
        for tx_reference in tx_ids:
            list_tx.append(tx_reference.acquirer_reference)
        number = len(list_tx)
        for refunds in charge.refunds:
            if refunds['id'] in list_tx:
                pass
            else:
                transaction.create({
                    'acquirer_id': tx.acquirer_id.id,
                    'amount': self.amount * -1,
                    'currency_id': tx.currency_id.id,
                    'partner_id': tx.partner_id.id,
                    'partner_country_id': tx.partner_country_id.id,
                    'reference': tx.reference + '_refund_' + str(number),
                    'sale_order_id': tx.sale_order_id.id,
                    'acquirer_reference': refunds['id'],
                    'status': 'done',
                })
                number += 1
