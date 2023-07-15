# Custom Odoo Module

This is a custom module developed for Odoo version 10.0, designed to provide a Sales Report for a specific customer within a given date range. It is supported on Python version 2.7.9.

## Description

The Custom Odoo Module extends the existing Sale Reporting functionality in Odoo by adding a new menu item called "Sales Report." This menu item is accessible only to users with the sales manager role.

The module includes a wizard with the following fields:
- From date: Select the starting date for the sales report.
- To date: Select the ending date for the sales report.
- Customer: Choose a specific customer from the available options.

By entering the desired date range and selecting a customer, users can generate a sales report that displays the sales data for the specified customer within the given date range.

## How to Use

1. Make sure you have Odoo version 10.0 and Python version 2.7.9 installed.

2. Install the custom module by placing it in the addons directory of your Odoo installation.

3. Restart the Odoo server to load the custom module.

4. Log in to Odoo with a user account that has the sales manager role.

5. Navigate to the "Sales Reporting" menu in Odoo.

6. Click on the "Sales Report" menu item to open the wizard.

7. Fill in the "From Date," "To Date," and "Customer" fields in the wizard.

8. Click the "Generate Report" button to generate the sales report.

9. The sales report will be displayed with the customer-wise sales data in the desired format.


## Note:
Please update your database configuration mentioned in ```openerp-server.conf``` file
