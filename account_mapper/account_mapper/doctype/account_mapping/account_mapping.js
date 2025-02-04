// Copyright (c) 2025, Kiranmai and contributors
// For license information, please see license.txt



frappe.ui.form.on("Account Mapping", {
    product(frm) {
        if (!frm.doc.product) return;

        // Call the custom API
        frappe.call({
            method: "account_mapper.account_mapper.doctype.account_mapping.account_mapping.get_project_details_by_product",
            args: {
                product: frm.doc.product
            },
            callback: function (r) {
                if (r.message) {
                    // frm.clear_table("client"); // Replace "client" with the actual child table fieldname

                    r.message.forEach(row => {
                        let child = frm.add_child("client");
                        child.projectclient_name = row.projectclient_name;
                        child.stage = row.stage;
                        child.status = row.status;
                        child.billable_status = row.billable_status;
                        child.product = row.product;


                    });

                    frm.refresh_field("client");
                    frm.save();
                }
            }
        });
    }
});

