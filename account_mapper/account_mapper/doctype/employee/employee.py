# # Copyright (c) 2025, Kiranmai and contributors
# # For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Employee(Document):

	def before_insert(self):
		# Create a new User only if e_mail_id and employee_full_name are set
		if self.e_mail_id and self.employee_full_name:
			user = frappe.new_doc("User")
			user.email = self.e_mail_id
			user.first_name = self.employee_full_name
			user.enabled = 1  # Enable user
			user.add_roles("Employee")
			user.insert(ignore_permissions=True)  # Insert user ignoring permissions
			
			# Assign the Employee role
			# frappe.get_doc("User", user.name).add_roles("Employee")

