from po2 import PO, Supplier
class POwithDelivery(PO):
	def delivery(self):
		print("delivering the po")
class OwnSupplier(Supplier):
	def create(self):
		pass