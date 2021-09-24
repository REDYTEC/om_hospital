from odoo import http
from odoo.htto import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class AppointmentController(http.Controller):

    @http.route('/om_hospital/appointments', auth='user', type='json')
    def appointment_banner(self):
        return {
            'html': """
            <div>
                <link>
                <center><h1><font color="red">Sub to channel....!</font></h1></center>
            </div>
            """
        }

# class Hospital(http.Controller):
