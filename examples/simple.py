from ember import GradTensor, Tensor

def testA(): 
  A = Tensor.gaussian([3, 4, 2], 0, 1, 1, True)
  B = Tensor.gaussian([2, 5], 0, 1, 0, True) 
  C = A @ B 

  D = Tensor.gaussian([4, 5], 0, 1, 0, True)
  E = C * D

  E.backprop(False)

  print(A.grad.shape)
  print(B.grad.shape)
  print(C.grad.shape)
  print(D.grad.shape)
  print(E.grad.shape)

def testB(): 
  A = Tensor.gaussian([4, 2], 0, 1, 1, True)
  B = Tensor.gaussian([3, 2], 0, 1, 1, True) 
  C = A + B 

  D = Tensor.gaussian([2], 0, 1, 0, True)
  E = D * C

  E.backprop(False)


  print(A.grad.shape)
  print(B.grad.shape)
  print(C.grad.shape)
  print(D.grad.shape)
  print(E.grad.shape)


t1 = GradTensor(list(range(1, 11)), [5, 2], 1, 0) 
t2 = GradTensor([2, 3, 4, 5, 7, 8, 9, 10], [2, 4], 1, 0) 
print(t1 @ t2)
