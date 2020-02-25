from odoo import models, fields, api


class printers_devices(models.Model):
    _name = 'printers.devices'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Printer record'
    _rec_name = 'printer_model'

    printer_user = fields.Many2one('res.users', string='User', required=True)
    printer_image = fields.Binary(string='Image')
    printer_serial_number = fields.Char(string='Serial Number', required=1)
    printer_brand = fields.Char(string='Brand')
    printer_model = fields.Char(string='Model name')
    printer_supplier = fields.Many2one('res.partner', string='Supplier')
    printer_market_value = fields.Float(string='Market Value', digits=(12, 2))
    printer_purchase_date = fields.Date(string='Purchase Date')
    printer_warranty_expiration = fields.Date(string='Warranty Expiration')
    printer_condition = fields.Boolean(string='Unit in use')
    printer_age = fields.Char(string='Age')
    printer_comment = fields.Text(string='Internal Comment')

    _sql_constraints = [
        ('printer_serial_number_unique',
         'unique(printer_serial_number)',
         "Error! serial number already exist!"),
    ]

    @api.onchange('printer_serial_number')
    def _make_uppercase(self):
        if self.printer_serial_number:
            self.printer_serial_number = str(self.printer_serial_number).upper()
