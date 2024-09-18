from odoo import fields, models

class Property(models.Model):
  _name = "estate.property"
  _description = "Here is a description of Real Estate Tutorial"

  name = fields.Char('Name', required=True)
  description = fields.Text('Description')
  active = fields.Boolean('Active', default=True)
  state = fields.Selection(
    string='State',
    required=True,
    copy=False,
    default='new',
    selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')])
  postcode = fields.Char('Postcode')
  date_availability = fields.Date('Date availability',
    copy=False,
    default=fields.Date.add(fields.Date.today(), months=3))
  expected_price = fields.Float('Expected price', required=True)
  selling_price = fields.Float('Selling price', readonly=True, copy=False)
  bedrooms = fields.Integer('Bedrooms', default=2)
  living_area = fields.Integer('Living area')
  facades = fields.Integer('Facades')
  garage = fields.Boolean('Garage')
  garden = fields.Boolean('Garden')
  garden_area = fields.Integer('Gardean area')
  garden_orientation = fields.Selection(
    string='Garden orientation',
    selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
