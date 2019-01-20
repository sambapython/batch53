from po2 import Supplier
from po_extension import POwithDelivery
sup=Supplier()
sup.create()
po=POwithDelivery()
po.create()
po.delivery()