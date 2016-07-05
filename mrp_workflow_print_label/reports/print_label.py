# -*- coding: utf-8 -*-
from datetime import datetime
from openerp import models, api
from openerp.report import report_sxw
from openerp.tools.translate import _

import logging
_logger = logging.getLogger(__name__)

class PrintLabelReport(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(PrintLabelReport, self).__init__(cr, uid, name, context=context)


class report_delivery_order_pdf(models.AbstractModel):
    _name = 'report.mrp_workflow_print_label.label_qweb'
    _inherit = 'report.abstract_report'
    _template = 'mrp_workflow_print_label.label_qweb'
    _wrapped_report_class = PrintLabelReport