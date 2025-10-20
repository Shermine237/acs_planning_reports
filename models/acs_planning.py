# -*- coding: utf-8 -*-

from odoo import models


class AcsPlanning(models.Model):
    _inherit = 'acs.planning'

    def action_print_employee_plannings(self):
        """
        Action pour imprimer les rapports de planning des employés 
        à partir des enregistrements de planning sélectionnés
        """
        # Récupérer les employés uniques des plannings sélectionnés
        employees = self.mapped('employee_id')
        
        if not employees:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Aucun employé',
                    'message': 'Aucun employé trouvé dans les plannings sélectionnés.',
                    'type': 'warning',
                    'sticky': False,
                }
            }
        
        # Générer le rapport PDF pour tous les employés
        return self.env.ref('acs_planning_reports.action_report_employee_planning').report_action(employees)
