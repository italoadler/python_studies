class Store:
	def __init__(self, name):
		self.name = name
		self.items = []

	def add_item(self, name, price):
		self.items.append({
			'name': name,
			'price': price
			
		})

	def stock_price(self): 
		total = 0 
		for item in self.items:
			total += item['price']
		return total



new_store = Store("oi")
new_store.add_item('petrobras', 330.30)
new_store.add_item('centauro', 1220.30)
new_store.add_item('magazine luiza', 1210.30)
new_store.add_item('pao de acucar', 1230.30)
print(new_store.items)