#-*- coding: utf-8 -*- 

{ 
    'name': 'Compras de Productos', 
    'description': 'Ven y compra productos un precio comodo.', 
    'author': 'Alex Salazar',
    "website": "www.compras.com", 
    'depends': ['base'], 
    "data": ["views/compra_menus.xml",
    		 "views/juego.xml",
    		 "views/verdura.xml" ],
    'application': True, 
}