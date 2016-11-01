# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from openerp import api, models

class ReportPurchaseOrderCustom(models.AbstractModel):
    _name = 'report_purchase_order_custom'

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name(
            'MT_custom_report.report_purchase_order_custom')
        docs = self.env[report.model].browse(self._ids)
        entrega = {}
        lines_to_display = {}
        for purchase in docs:
            entrega[purchase.id] = (
                purchase.picking_type_id and
                purchase.picking_type_id.warehouse_id and
                purchase.picking_type_id.warehouse_id.partner_id or
                None)
        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': docs,
            'item': 1,
            'entrega': entrega,
            'Lines': lines_to_display,
        }
        return report_obj.render(
            'MT_custom_report.report_purchase_order_custom', docargs)
