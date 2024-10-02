from odoo import fields, models, api

class Property(models.Model):
  _name = 'estate.property'
  _description = 'Here is a description of Real Estate Tutorial'

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
  property_type_id = fields.Many2one('estate.property.type', string='Property Type')
  user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.uid)
  partner_id = fields.Many2one('res.partner', string='Buyer', copy=False)
  tag_ids = fields.Many2many('estate.property.tag', string='Tags')
  offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
  total_area = fields.Integer('Total Area', compute='_compute_total_area')
  best_price = fields.Float('Best Price', compute='_compute_best_price')

  @api.depends('living_area', 'garden_area')
  def _compute_total_area(self):
    for record in self:
      record.total_area = record.living_area + record.garden_area

  @api.depends('offer_ids')
  def _compute_best_price(self):
    for record in self:
      offer_prices = record.offer_ids.mapped('price')
      if len(offer_prices) > 0:
        record.best_price = max(offer_prices)
      else:
        record.best_price = 0
