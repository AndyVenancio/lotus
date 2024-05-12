import numpy as np
xTx = np.array([[12, 6, 294, 155], [6, 6, 155, 155], [294, 155, 7314, 4063], [155, 155, 4063, 4063]])
xTy = np.array([29.63, 46.23, 978.81, 1298.79])
inverse = np.linalg.inv(xTx)
result = np.dot(inverse, xTy)
print(result)
sigmahat = inverse * 8.54
diag = np.diag(sigmahat)
print(np.sqrt(diag))