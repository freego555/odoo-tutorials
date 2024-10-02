from odoo import fields, models, api

class PropertyOffer(models.Model):
  _name = 'estate.property.offer'
  _description = 'Property offers'

  price = fields.Float('Price')
  status = fields.Selection(string='Status', copy=False, selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
  partner_id = fields.Many2one('res.partner', string='Partner', required=True)
  property_id = fields.Many2one('estate.property', string='Property', required=True)
  validity = fields.Integer('Validity (days)', default=7)
  date_deadline = fields.Date('Deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline')

  @api.depends('validity')
  def _compute_date_deadline(self):
    for record in self:
      create_date = fields.Date.today()
      if record.create_date:
        create_date = record.create_date
      record.date_deadline = fields.Date.add(create_date, days=record.validity)

  def _inverse_date_deadline(self):
    for record in self:
      timedelta = record.date_deadline - record.create_date.date()
      record.validity = timedelta.days
