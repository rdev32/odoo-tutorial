from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'estate.property'

    name = fields.Char(required=True, default='Unknown')
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        copy=False, default=fields.Date.to_date(datetime.now() + relativedelta(months=3)), string='Available From')
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(copy=False, selection=[(
        'north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    last_seen = fields.Datetime(default=fields.Datetime.now)
    active = fields.Boolean(default=True)
    state = fields.Selection(required=True, copy=False, default='new', selection=[('new', 'New'), ('recieved', 'Offer Recieved'), (
        'accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')])
