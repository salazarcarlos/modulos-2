#-*- coding: utf-8 -*- 

from odoo import models, fields, api

class VerdurasRicas(models.Model):
    _name = "verduras.ricas"
    
    proveedor = fields.Char(string="Nombre del Proveedor", required=True)
    name = fields.Char(string="Nombre Del Producto", required=True)
    cantidad = fields.Char(string="Cantidad del producto", required=True)
    precio = fields.Float("Precio", required=True)
    fecha_hora = fields.Datetime(string="Fecha De La Compra", required=True)
    foto = fields.Binary("Foto")
    efectivo = fields.Boolean('Efectivo')
    visa = fields.Boolean('Visa') 


    @api.multi 
    def do_toggle_efectivo(self):
        self.efectivo = True

    @api.multi 
    def do_clear_efectivo(self):
        self.efectivo = False

    @api.multi 
    def pago_visa(self):
        self.visa = True

    @api.multi 
    def no_pago_visa(self):
        self.visa = False
 