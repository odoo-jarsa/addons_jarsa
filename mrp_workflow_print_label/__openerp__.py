# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "MRP Workflow Print Label",
    "summary": "Print MRP Workflow Label after Production",
    "version": "9.0.1.0.0",
    "category": "Hidden",
    "website": "https://www.jarsa.com.mx/",
    "author": "JARSA Sistemas, S.A. de C.V.",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "mrp"
    ],
    "data": [
        'wizard/mrp_print_label.xml',
        'views/mrp_view.xml',
        'views/mrp_workflow.xml',
        'views/res_users.xml',
        'reports/label.xml',
    ],
}
