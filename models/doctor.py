# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HospitalAppointment(models.Model):
    _name = "hospital.doctor"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Hospital Doctor"

    doctor_name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='other',)
    note = fields.Text(string='Description')
    image = fields.Binary(string='Doctor Image')
