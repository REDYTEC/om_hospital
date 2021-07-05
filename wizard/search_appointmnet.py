# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class CreateAppointmentWizard(models.TransientModel):
    _name = 'search.appointment.wizard'
    _description = 'Search Appointment Wizard'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
