# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AdjustmentRequestWizard(models.TransientModel):
    _name = 'adjustment.request.wizard'
    _description = 'Adjustment Request Wizard'

    #--------Fields to capture order information and adjustment details--------#

    order_id = fields.Many2one('sale.order', string='Order')
    adjustment_detail = fields.Text(string='Adjustment Detail')
    comment = fields.Text(string='Comment')

    #-------Override default_get method to populate default values---------#

    @api.model
    def default_get(self, fields):
        defaults = super(AdjustmentRequestWizard, self).default_get(fields)

        #--------Fetching active_id from the context----------#

        active_id = self.env.context.get('active_id')
        if active_id:
            #-----Fetching the sale order record based on active_id----#
            order = self.env['sale.order'].browse(active_id)
            #----Setting default values for order_id field-----#
            defaults['order_id'] = order.id
        return defaults

    #---------Method to submit adjustment request--------#

    def submit_request(self):
        #-----Creating a new vendor adjustment request record------#
        adjustment_request = self.env['vendor.adjustment.request'].create({
            'order_id': self.order_id.id,
            'adjustment_detail': self.adjustment_detail,
            'comment': self.comment,
        })
        #------Close the current wizard window after submission------#
        return {
            'type': 'ir.actions.act_window_close'
        }
