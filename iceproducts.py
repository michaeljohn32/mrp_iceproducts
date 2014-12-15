#################################################
#  
#   This program is free software: you can
#   redistribute and/or modify it.
#
#
#
#
#
#
#
#
#
###############################################
from openerp import models, fields

class product_template(models.Model):
    _inherit = 'product.template'

    drawingfilename = fields.Char(string="DrawingFileName")
    productname = fields.Char(string="BOM_ProductDesc")
    bomproductid = fields.Char(string="BOM_ProductID")
    product_timestamp = fields.Datetime(string="Product Update Timestamp")
    supplier_timestamp = fields.Datetime(string="Supplier Update Timestamp")
    bom_timestamp = fields.Datetime(string="BoM Update Timestamp")

class res_partner(models.Model):
    _inherit = 'res.partner'

    bom_supplierid = fields.Integer(string="BOM_SupplierID")
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
