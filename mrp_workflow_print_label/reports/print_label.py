# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models
from openerp.report import report_sxw


class PrintLabelReport(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(PrintLabelReport, self).__init__(cr, uid, name, context=context)


class ReportDeliveryOrderPdf(models.AbstractModel):
    _name = 'report.mrp_workflow_print_label.label_qweb'
    _inherit = 'report.abstract_report'
    _template = 'mrp_workflow_print_label.label_qweb'
    _wrapped_report_class = PrintLabelReport
