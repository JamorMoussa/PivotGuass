import numpy as np

class SystemError(Exception):
	def __init__(self, text):
		super(SystemError, self).__init__(text)

class InverseError(Exception):
	def __init__(self, text):
		super(InverseError, self).__init__(text)
		
		

def SolveSys(A,B):
	"""
	This Method use the Gauss Elimination Method. It's used to find 
	a solution of linear system : 
									A.X = B
	which X = (x1, ...... , xn) 
	It's return a numpy array which contain the solution.

	Example:

		>>> A = np.array([25, 5, 1],
					 [64, 8, 1],
					 [144,12,1],dtype='float64')

		>>> B = np.array([106.8, 177.2, 279.2])
		>>> SolveSys(A,B)
			-> array([ 0.29047619 19.69047619  1.08571429])
	"""
	if A.shape[0] == A.shape[1] and np.linalg.det(A) != 0 :
		a = np.array(A,copy=True,dtype=float)
		b = np.array(B,copy=True,dtype=float)
		n = a.shape[0] - 1

		Xi = dict()

		for i in range(n+1):
			p = a[i,i]
			for j in range(i+1,n+1):
				r = a[j,i]/p
				a[j,:] = a[j,:] - r * a[i,:]
				b[j] = b[j] - r * b[i]

		Xi[n] = b[n] / a[n,n]

		for i in range(n-1,-1,-1):
			tmp = 0
			for j in range(i+1,n+1):
				tmp += a[i,j] * Xi[j]
			Xi[i] = (b[i] - tmp)/a[i,i]
		return np.array([Xi[i] for i in range(n+1)])
	else:
		raise SystemError("The System can't solved, Matrice 'A' not squared or det(A)= 0.")


def InvM(A):

	"""
	This Method use the Gauss Elimination Method. It's used to find 
	inverse of Matrice A  : 
									A.A^(-1) = I
	It's return a numpy array.

	Example:

		>>> A = np.array([25, 5, 1],
					 [64, 8, 1],
					 [144,12,1],dtype='float64')

		>>> InvM(A)
			-> array([[ 0.04761905 , -0.08333333 , 0.03571429]
 					  [-0.95238095 , 1.41666667  , -0.46428571]
                      [ 4.57142857 , -5.         ,  1.42857143]]
	"""
	try:
		np.linalg.det(A)
		a = np.array(A,copy=True,dtype=float)
		n = a.shape[0] - 1
		I = np.identity(n+1)

		for i in range(n+1):
			p = a[i,i]
			for j in range(i+1,n+1):
				r = a[j,i]/p
				a[j,:] = a[j,:] - r * a[i,:]
				I[j,:] = I[j,:] - r * I[i,:]

		for i in range(n,0,-1):
			p = a[i,i]
			for j in range(i-1,-1,-1):
				r = a[j,i]/p
				a[j,:] = a[j,:] - r * a[i,:]
				I[j,:] = I[j,:] - r * I[i,:]

		for i in range(n+1):
			I[i,:] /= a[i,i]

		return I 
	except:
		raise InverseError("The A matrix can't be inversed")




