from collections import OrderedDict

class Cache:

	def __init__(self, capacity=32):
		self.cache = OrderedDict()
		self.capacity = capacity

	def get(self, key):
		if key not in self.cache:
			return False
		else:
			self.cache.move_to_end(key) # --> while data is found , it re-positioned to last thats why it's not be recognized through LRU. 
			return self.cache[key]

	def put(self, key, value):
		self.cache[key] = value
		self.cache.move_to_end(key)
		if len(self.cache) > self.capacity:
			self.cache.popitem(last = False) # --> remove first added item as LRU concept.
			
	def delete(self,key):
		self.cache.pop(key)

data1={'utsav':{'msg':'hi'}}
data2={'supu':{'msg':'hiii'}}
data3={'sayan':{'msg':'hlww'}}



cache = Cache()
cache.put('utsav',data1)
cache.put('supu',data2)
cache.put('sayan',data3)

print(cache.get('utsav'))


#utsav chatterjee
