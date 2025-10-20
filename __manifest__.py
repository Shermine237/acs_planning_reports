# -*- coding: utf-8 -*-
{
    'name': 'ACS Planning Reports Extension',
    'version': '18.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'PDF Reports for Employee and Site Planning',
    'description': """
        Extension module for ACS Planning
        ==================================
        
        This module extends the ACS Planning module with:
        - PDF reports for individual employee planning
        - PDF reports for site planning (multiple agents per site)
        - Smart buttons in employee form to download planning
        - Smart buttons in site form to download site planning
        
        Dependencies:
        - acs_planning: Base planning module
        - site_ange_security: Site management module
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': [
        'acs_planning',
        'site_ange_security',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'reports/employee_planning_report.xml',
        'reports/site_planning_report.xml',
        'views/hr_employee_views.xml',
        'views/site_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'post_init_hook': 'post_init_hook',
}
