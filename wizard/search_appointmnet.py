# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class CreateAppointmentWizard(models.TransientModel):
    _name = 'search.appointment.wizard'
    _description = 'Search Appointment Wizard'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)

    def action_search_appointment_m1(self):
        action = self.env["ir.actions.act_window"]._for_xml_id("om_hospital.action_hospital_appointment")
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action
