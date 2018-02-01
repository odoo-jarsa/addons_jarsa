# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Close Tickets",
    "summary": "Close Tickets",
    "version": "10.0.1.0.0",
    "category": "Hidden",
    "website": "https://www.jarsa.com.mx/",
    "author": "JARSA Sistemas, S.A. de C.V.",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        'helpdesk',
    ],
    "data": [
        'data/template.xml',
        'data/ir_cron.xml',
        'data/ir_action_server.xml',
        'data/config_parameter_data.xml',
        'data/ir_filters.xml',
        'data/base_action_rule.xml',
    ],
    "demo": [
    ]
}
