
class A(object):
	def get_a(self):
		print('a')

	@classmethod
	def get_b(self):
		print('b')

a = A()
a.get_a()
A.get_a(A())
A.get_b()
