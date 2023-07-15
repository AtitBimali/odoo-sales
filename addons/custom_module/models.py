from odoo import models, fields, api

class SalesReportWizard(models.TransientModel):
    _name = 'sales.report.wizard'
    
    from_date = fields.Date(string='From Date', required=True)
    to_date = fields.Date(string='To Date', required=True)
    customer = fields.Many2one('res.partner', string='Customer')

    @api.multi
    def generate_report(self):
        # Get the selected customer's name
        customer_name = self.customer.name
        
        # Query the sales data for the selected customer within the date range
        sales_data = self.env['sale.order'].search([
            ('partner_id', '=', self.customer.id),
            ('date_order', '>=', self.from_date),
            ('date_order', '<=', self.to_date),
        ])
        
        # Create the report lines
        report_lines = []
        total_amount = 0.0
        sno = 1
        for sale in sales_data:
            for line in sale.order_line:
                report_line = {
                    'sno': sno,
                    'source': sale.name,
                    'invoice_no': sale.client_order_ref,
                    'invoice_date': sale.date_order,
                    'product': line.product_id.name,
                    'quantity': line.product_uom_qty,
                    'rate': line.price_unit,
                    'total': line.price_subtotal,
                }
                report_lines.append(report_line)
                total_amount += line.price_subtotal
                sno += 1
        
        # Print the report
        report = "Sales Report of {} from {} to {}\n\n".format(customer_name, self.from_date, self.to_date)
        report += "sno Source Invoice No Invoice date Product Quantity Rate Total\n"
        for line in report_lines:
            report += "{} {} {} {} {} {} {} {}\n".format(line['sno'], line['source'], line['invoice_no'], line['invoice_date'], line['product'], line['quantity'], line['rate'], line['total'])
        report += "\nTotal Amount: {}\n".format(total_amount)
        
        # Print the report or do further processing (e.g., write to a file, send via email)
        print(report)
