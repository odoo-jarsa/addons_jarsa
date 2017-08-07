# -*- coding: utf-8 -*-
# Copyright 2017, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Sale Report',
    'version': '10.0.0.1.0',
    'category': 'Project',
    'author': 'Jarsa Sistemas',
    'website': 'https://www.jarsa.com.mx',
    'depends': [
        'base',
        'sale'],
    'description': (
        'Create Sale Report'),
    'license': 'AGPL-3',
    'data': [
        'report/external_layout.xml',
        'report/quatation_report_id.xml',
    ],
    'application': True,
    'installable': True,
}
