# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    date_appointment = fields.Date(string='Date', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)

    def action_create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'date_appointmnent': self.date_appointment
        }
        appointment_rec = self.env['hospital.appointment'].create(vals)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_model': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,
            'target': 'new',
        }
