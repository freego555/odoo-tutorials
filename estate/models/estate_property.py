from odoo import fields, models

class Property(models.Model):
  _name = "estate.property"
  _description = "Here is a description of Real Estate Tutorial"

  name = fields.Char('Name', required=True)
  description = fields.Text('Description')
  postcode = fields.Char('Postcode')
  date_availability = fields.Date('Date availability')
  expected_price = fields.Float('Expected price', required=True)
  selling_price = fields.Float('Selling price')
  bedrooms = fields.Integer('Bedrooms')
  living_area = fields.Integer('Living area')
  facades = fields.Integer('Facades')
  garage = fields.Boolean('Garage')
  garden = fields.Boolean('Garden')
  garden_area = fields.Integer('Gardean area')
  garden_orientation = fields.Selection(
    string='Garden orientation',
    selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
