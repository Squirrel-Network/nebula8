from pprint import pprint

class Optional:
	@staticmethod
	def of(value = None):
		if value == None:
			return Nope()
		else:
			return Just(value)

	def __init__(self, value = None):
		self.maybeValue = value

	def valueOf(self):
		return self.maybeValue

class Nope(Optional):
	def map(self, f):
		return Nope()

	def flatMap(self, f):
		return Nope()

	def valueOf(self):
		return None

class Just(Optional):
	@staticmethod
	def of(value = None):
		return Just(value)

	def map(self, f):
		return Optional.of(f(self.maybeValue))

	def flatMap(self, f):
		flattened = f(value)
		assert isinstance(flattened, Optional)
		return flattened

	def valueOf(self):
		return self.maybeValue

class Given(Optional):
	def of(value = None):
		return Given(value)

	def when(self, predicate, then):
		if predicate(self.maybeValue):
			return GivenJust(then)
		else:
			return GivenNope(self.maybeValue)

	def otherwise(self, then):
		return Just.of(then)

	def valueOf(self):
		return self.maybeValue

class GivenNope(Given):
	def __init__(self, searchVal = None):
		self.maybeValue = searchVal

	def valueOf(self):
		return None

	def otherwise(self, then):
		return Just.of(then)

class GivenJust(Given):
	def valueOf(self):
		return self.maybeValue

	def when(self, predicate, then):
		return self

	def otherwise(self, then):
		return Just.of(self.maybeValue)

class Try(Optional):
	@staticmethod
	def of(f):
		assert callable(f)
		return Try(f)

	def __init__(self, f):
		self.maybeValue = False
		try:
			value = f()
			self.maybeValue = True

			self.tryResult = value
		except Exception as e:
			self.error = e

	def catch(self, f):
		if not self.maybeValue:
			f(self.error)
		return self

	def map(self, f):
		if self.maybeValue:
			return Just(self.tryResult).map(f)
		else:
			return Nope()

	def flatMap(self, f):
		if self.maybeValue:
			return Just(self.tryResult).flatMap(f)
		else:
			return Nope()

	def valueOf(self):
		if self.maybeValue:
			return self.maybeValue
		else:
			return None
