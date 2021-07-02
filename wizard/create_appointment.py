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
            'date_appointment': self.date_appointment
        }
        appointment_rec = self.env['hospital.appointment'].create(vals)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,
            # activate if want to appear as a pop up
            # 'target': 'new',
        }

    def action_view_appointment(self):
        # method 1
        # action = self.env["ir.actions.act_window"]._for_xml_id("om_hospital.action_hospital_appointment")
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # return action
        
        # method 2
        # action = self.env.ref('om_hospital.action_hospital_appointment').read()[0]
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # return action
        
        # method 3
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointment',
            'res_model': 'hospital.appointment',
            'view_type': 'form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }
