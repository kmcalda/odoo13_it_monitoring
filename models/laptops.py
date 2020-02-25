from odoo import models, fields, api

class laptops_devices(models.Model):
    _name = 'laptops.devices'
    _description = 'for laptop'
    _rec_name = 'laptop_user'

    laptop_image = fields.Binary(string='Image')
    laptop_user = fields.Many2one('res.users',string='User')
    laptop_serial_number = fields.Char(string='Serial Number')
    laptop_os = fields.Char(string='Operating System')
    laptop_brand = fields.Char(string='Brand')
    laptop_model = fields.Char(string='Model')
    laptop_processor = fields.Char(string='Processor')
    laptop_hd = fields.Char(string='HDD')
    laptop_ram = fields.Char(string='RAM')
    laptop_office = fields.Char(string='Office')
    laptop_supplier = fields.Char(string='Supplier')
    laptop_market_value = fields.Float(string='Market Value', digits=(12,2))
    laptop_purchase_date = fields.Date(string='Purchase Date')
    laptop_warranty_expiration = fields.Date(string='Warranty Expire')
    laptop_condition = fields.Char(string='Condition')
    laptop_age = fields.Char(string='Age')

    _sql_constraints = [
        ('laptop_serial_number_unique',
         'unique(laptop_serial_number)',
         "Error! serial number already exist!"),
    ]

    @api.onchange('laptop_serial_number')
    def _make_uppercase(self):
        if self.laptop_serial_number:
            self.laptop_serial_number = str(self.laptop_serial_number).upper()