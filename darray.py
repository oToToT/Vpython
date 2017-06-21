import numpy as np

class dArray(object):
	def __init__(self, tp=float):
		super(dArray, self).__init__()
		self.arr = np.array(np.zeros(1, dtype=tp))
		self.size = 1
		self.front = 0
		self.type = tp
	def append(self, x):
		if self.front + 1 >= self.size:
			self.arr = np.append(self.arr, np.zeros(self.size, dtype=self.type))
			self.size *= 2
		self.arr[self.front] = x
		self.front += 1
	def back(self):
		return self.arr[self.front-1]

