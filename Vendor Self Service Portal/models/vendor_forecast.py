# -*- coding: utf-8 -*-
import xlsxwriter


from odoo import models, fields

class VendorForecast(models.Model):
    _name = 'new.forecast'
    _description = 'Forecast details'


    #---------Fields to store forecast information-------#
    
    product_name = fields.Char(string = 'Product Name')
    expected_quantity = fields.Integer(string='Expected Quantity')
    forecast_date = fields.Date(string='Forecast Date')
    # product_id = fields.Many2one('product.product', string='Product', required=True)
    product_id = fields.Many2one('new.forecast', string='Product')



    def action_generate_report(self):
    # Fetch all records of the model
        forecasts = self.env['new.forecast'].search([])

        # Create an Excel workbook and add a worksheet
        workbook = xlsxwriter.Workbook(r'E:\jayrajsinh pendrive\excel_download\forecast_report.xlsx')
        worksheet = workbook.add_worksheet('Forecast Report')

        # Write column headers
        worksheet.write(0, 0, 'Product Name')
        worksheet.write(0, 1, 'Expected Quantity')
        worksheet.write(0, 2, 'Forecast Date')

        # Write data rows
        row = 1
        for forecast in forecasts:
            worksheet.write(row, 0, forecast.product_name)
            worksheet.write(row, 1, forecast.expected_quantity)
            worksheet.write(row, 2, str(forecast.forecast_date))
            row += 1

        # Close the workbook
        workbook.close()

        # Read the Excel file and return it as a binary
        with open(r'E:\jayrajsinh pendrive\excel_download\forecast_report.xlsx', 'rb') as f:
            file_data = f.read()

        # Return the binary data
        return {
            'type': 'ir.actions.act_url',
            'url': 'web/content/?model=new.forecast&id=%s&filename_field=report_filename&field=report&download=true&filename=forecast_report.xlsx' % (self.id),
            'target': 'self',
        }




   



    
