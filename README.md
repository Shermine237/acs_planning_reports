# ACS Planning Reports Extension

## Description

This module extends the ACS Planning module to provide comprehensive PDF reporting capabilities for employee and site planning.

## Features

### Employee Planning Reports
- Generate PDF reports showing an employee's complete planning schedule
- Filter by date range
- View planning details including:
  - Shifts with start and end times
  - Working schedules
  - Work locations
  - Planning status

### Site Planning Reports  
- Generate PDF reports for all agents assigned to a specific site
- View consolidated planning for the entire site
- Includes all agents' schedules in a single report
- Useful for site managers and coordinators

### Smart Buttons
- **Employee Form**: Smart button to view planning count and download PDF report
- **Site Form**: Smart button to view agent planning count and download site PDF report

## Installation

1. Ensure dependencies are installed:
   - `acs_planning` (Employee Shift Planning)
   - `site_ange_security` (Site Management)
   
2. Install this module from the Apps menu

## Usage

### Employee Planning Report

1. Navigate to **Employees** menu
2. Open an employee record
3. Click on the **Planning** smart button to view planning count
4. Use the **Print** menu to select **Employee Planning Report**

### Site Planning Report

1. Navigate to **Sites** menu
2. Open a site record  
3. Click on the **Planning** smart button (if agents are assigned)
4. Use the **Print** menu to select **Site Planning Report**

## Technical Details

### Models Extended
- `hr.employee`: Added planning count and action methods
- `site.site`: Added planning count and action methods

### Reports
- `employee_planning_report`: Individual employee planning PDF
- `site_planning_report`: Site-wide planning PDF with all agents

## Dependencies

- Odoo 18.0+
- acs_planning
- site_ange_security
- hr (base HR module)

## License

LGPL-3

## Support

For support, please contact your system administrator.
