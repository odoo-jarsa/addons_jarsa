# -*- coding: utf-8 -*-
# Copyright 2017, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Create New Lead',
    'version': '10.0.0.1.0',
    'category': 'Sales',
    'author': 'Jarsa Sistemas',
    'description': 'Create new lead from ticket',
    'depends': [
        'crm',
        'helpdesk'
    ],
    'data': [
        'views/crm_lead.xml',
    ],
    'installable': True,
}
