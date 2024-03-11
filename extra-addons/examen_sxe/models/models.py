from odoo import models, fields

class Product(models.Model):
    _name = 'product'
    _description = 'Product'

    id = fields.Integer(string='ID')
    producto = fields.Char(string='Producto')
    viabilidad = fields.Float(string='Viabilidad')