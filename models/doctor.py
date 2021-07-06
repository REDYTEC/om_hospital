# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HospitalAppointment(models.Model):
    _name = "hospital.doctor"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Hospital Doctor"
    # Because the model doesn't have a 'name' field, to get a name to a many2one field that uses this info,
    # need to specify a main id with _rec_name
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='other',)
    note = fields.Text(string='Description')
    image = fields.Binary(string='Doctor Image')
