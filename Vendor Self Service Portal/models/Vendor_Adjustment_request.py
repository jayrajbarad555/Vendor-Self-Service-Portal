# -*- coding: utf-8 -*-



from odoo import models, fields , api

class VendorAdjustmentRequest(models.Model):
    _name = 'vendor.adjustment.request'
    _description = 'Vendor Adjustment Request'


    #------Fields to capture order information and adjustment details-----#
    
    order_id = fields.Many2one('sale.order', string='Order')
    adjustment_detail = fields.Text(string='Adjustment Detail')
    comment = fields.Text(string='Comment')

   