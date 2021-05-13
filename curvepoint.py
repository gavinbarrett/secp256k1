from Crypto.Util.number import inverse

class CurvePoint:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

	def __add__(self, other):
		''' Add two points on the secp256k1 curve '''
		if self.x == 0 and self.y == 0:
			return CurvePoint(other.x, other.y)
		x1, y1 = self.x, self.y
		x2, y2 = other.x, other.y
		if x1 == x2:
			return self.double()
		lam = ((y2 - y1) * inverse(x2 - x1, self.p)) % self.p
		x_r = (pow(lam, 2, self.p) - x1 - x2) % self.p
		y_r = (lam * (x1 - x_r) - y1) % self.p
		return CurvePoint(x_r, y_r)

	def double(self):
		''' Double a point P on the secp256k1 curve '''
		x, y = self.x, self.y
		lam = (3 * pow(x, 2, self.p) * inverse(2 * y, self.p)) % self.p
		x_r = (pow(lam, 2, self.p) - x - self.x) % self.p
		y_r = (lam * (x - x_r) - y) % self.p
		return CurvePoint(x_r, y_r)
	
	def __mul__(self, xprv):
		P = self
		K = CurvePoint(0,0)
		while xprv:
			if xprv & 1:
				K = K + P
			xprv >>= 1
			if xprv:
				P = P.double()
		return K
	
	def __rmul__(self, xprv):
		P = self
		K = CurvePoint(0,0)
		while xprv:
			if xprv & 1:
				K = K + P
			xprv >>= 1
			if xprv:
				P = P.double()
		return K
	
	def __repr__(self):
		# return the point coordinates
		return f"({hex(self.x)}, {hex(self.y)})"
