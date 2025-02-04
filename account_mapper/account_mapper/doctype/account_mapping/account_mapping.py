# Copyright (c) 2025, Kiranmai and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AccountMapping(Document):
	pass


@frappe.whitelist()
def get_project_details_by_product(product):
    # Fetch the project details related to the product
    project_details = frappe.get_all(
        "Project Details",
        filters={"parent": product},
        fields=["projectclient_name", "stage", "status", "billable_status","product"]
    )
    return project_details
