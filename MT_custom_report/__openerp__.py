# -*- coding: utf-8 -*-
# © <2015> <Jarsa Sistemas S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "MT Custom Report",
    "version": "9.0.1.0.0",
    "category": "Report",
    "website": "http://jarsa.com.mx",
    "author": "<Jarsa Sistemas S.A. de C.V.>, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "purchase",
    ],
    "data": [
        'views/purchase_order_view.xml',
        'views/purchase_order_report.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
