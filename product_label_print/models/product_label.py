# -*- coding: utf-8 -*-
##############################################################################
#
#    Elneo
#    Copyright (C) 2011-2016 Elneo (Technofluid SA) (<http://www.elneo.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api


class ProductLabelPrint(models.Model):
    _name='product.label.print'
    name = fields.Char(string='Name',required=True)
    product_ids=fields.Many2many('product.product', 'label_product_product_rel', 'label_id', 'product_id','Products')
    type = fields.Selection(selection=[('standard','Standard'),('maintenance','Maintenance')],string='Type',required=True,default='standard')
    
    @api.one
    def easy_import(self):
        products = self.env['product.product'].search([('label_import','=',True)])
        self.product_ids = products
        return
    

class ProductProduct(models.Model):
    _inherit='product.product'
    label_import = fields.Boolean('Label import', help="used to import easily in new label print")

    
    
    