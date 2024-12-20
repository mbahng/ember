import unittest
from ember import GradTensor, ScalarTensor

class TestGradTensorPivot(unittest.TestCase): 

  def testPivot(self): 
    x1 = GradTensor([1, 2, 3, 4], [2, 2], 1)
    x2 = GradTensor([1, 2, 3, 4], [1, 2, 2], 2)
    x3 = GradTensor([1, 2, 3, 4], [1, 1, 2, 2], 3)
    x4 = GradTensor([1, 2, 3, 4], [2, 1, 2, 1], 2)
    x5 = GradTensor([2, 2], 1)
    x6 = GradTensor([1, 2, 2], 2)
    x7 = GradTensor([1, 1, 2, 2], 3)
    x8 = GradTensor([2, 1, 2, 1], 2)

    self.assertEqual(x1.pivot, 1)
    self.assertEqual(x2.pivot, 2)
    self.assertEqual(x3.pivot, 3)
    self.assertEqual(x4.pivot, 2)
    self.assertEqual(x5.pivot, 1)
    self.assertEqual(x6.pivot, 2)
    self.assertEqual(x7.pivot, 3)
    self.assertEqual(x8.pivot, 2)

class TestGradTensorEquality(unittest.TestCase): 

  def testGradEquals(self): 
    x = GradTensor([1, 2, 3, 4], [2, 2], 1)
    y = GradTensor([1, 2, 3, 4], [2, 2], 1)
    self.assertEqual(x, y)

  def testGradNotEquals(self): 
    w = GradTensor([1, 2, 3, 4], [2, 2], 1)
    x = GradTensor([2, 2, 3, 4], [2, 2], 1)
    y = GradTensor([1, 2, 3, 4], [4], 1)
    z = GradTensor([1, 2, 3, 4], [2, 2], 0)

    self.assertNotEqual(w, x)
    self.assertNotEqual(w, y)
    self.assertNotEqual(w, z)
    self.assertNotEqual(x, y)
    self.assertNotEqual(x, z)
    self.assertNotEqual(y, z)

class TestGradTensorType(unittest.TestCase): 

  def testType(self): 
    x = GradTensor([1, 2, 3, 4], [2, 2], 1) 
    self.assertEqual(x.type(), "GradTensor")

  def testDtype(self): 
    x = GradTensor([1, 2, 3, 4], [2, 2], 1) 
    self.assertEqual(x.dtype(), "double")

class TestGradTensorIndex(unittest.TestCase): 

  def testGetterVector(self): 
    x = GradTensor([1, 2, 3, 4], [4], 1) 
    self.assertEqual(x[0], ScalarTensor(1))
    self.assertEqual(x[1], ScalarTensor(2))
    self.assertEqual(x[2], ScalarTensor(3))
    self.assertEqual(x[3], ScalarTensor(4))

  def testGetterMatrix(self): 
    x = GradTensor([1, 2, 3, 4], [2, 2], 1)
    self.assertEqual(x[0, 0], ScalarTensor(1))
    self.assertEqual(x[0, 1], ScalarTensor(2))
    self.assertEqual(x[1, 0], ScalarTensor(3))
    self.assertEqual(x[1, 1], ScalarTensor(4))

  def testGetterTensor(self): 
    x = GradTensor([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 2], 1)
    self.assertEqual(x[0, 0, 0], ScalarTensor(1))
    self.assertEqual(x[0, 0, 1], ScalarTensor(2))
    self.assertEqual(x[0, 1, 0], ScalarTensor(3))
    self.assertEqual(x[0, 1, 1], ScalarTensor(4))
    self.assertEqual(x[1, 0, 0], ScalarTensor(5))
    self.assertEqual(x[1, 0, 1], ScalarTensor(6))
    self.assertEqual(x[1, 1, 0], ScalarTensor(7))
    self.assertEqual(x[1, 1, 1], ScalarTensor(8)) 

  def testSetterVector(self): 
    x = GradTensor([1, 2, 3, 4], [4], 1)  
    x[0] = 5 
    self.assertEqual(x[0], ScalarTensor(5))
    x[2] = 10
    self.assertEqual(x[2], ScalarTensor(10))
    
  def testSetterMatrix(self): 
    x = GradTensor([1, 2, 3, 4], [2, 2], 1)   
    x[0, 0] = 5
    self.assertEqual(x[0, 0], ScalarTensor(5))
    x[1, 0] = 10
    self.assertEqual(x[1, 0], ScalarTensor(10))

  def testSetterTensor(self): 
    x = GradTensor([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 2], 1) 
    x[0, 0, 0] = 13
    self.assertEqual(x[0, 0, 0], ScalarTensor(13))
    x[0, 1, 1] = 19
    self.assertEqual(x[0, 1, 1], ScalarTensor(19))

class TestGradTensorSlice(unittest.TestCase): 

  def testGetterVector(self): 
    x = GradTensor([1, 2, 3, 4], [4], 1)  
    self.assertEqual(x[:], x) 
    self.assertEqual(x[0:2], GradTensor([1, 2], [2], 1))
    self.assertEqual(x[1:3], GradTensor([2, 3], [2], 1))

  def testGetterMatrix(self): 
    x = GradTensor([1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 3], 1)  
    self.assertEqual(x[0,:], GradTensor([1, 2, 3], [1, 3], 1))
    self.assertEqual(x[1,:], GradTensor([4, 5, 6], [1, 3], 1))
    self.assertEqual(x[2,:], GradTensor([7, 8, 9], [1, 3], 1))
    self.assertEqual(x[:,0], GradTensor([1, 4, 7], [3, 1], 1))
    self.assertEqual(x[:,1], GradTensor([2, 5, 8], [3, 1], 1))
    self.assertEqual(x[:,2], GradTensor([3, 6, 9], [3, 1], 1))
    self.assertEqual(x[:2,:2], GradTensor([1, 2, 4 ,5], [2, 2], 1))

class TestGradTensorTranspose(unittest.TestCase): 

  def testVectorTranspose(self):  
    x = GradTensor([1, 2, 3, 4, 5, 6], [1, 6], 1)
    t = x.transpose([0, 1]) 
    self.assertEqual(t, GradTensor([1, 2, 3, 4, 5, 6], [6, 1], 1))

  def testMatrixTranspose(self): 
    x = GradTensor([1, 2, 3, 4, 5, 6], [2, 3], 1)
    t = x.transpose([0, 1]) 
    self.assertEqual(t, GradTensor([1, 4, 2, 5, 3, 6], [3, 2], 1))

  def testTensorTranspose(self):  
    # Really this should never be called, so I'll omit this test
    pass

class TestProperGradTensorIO(unittest.TestCase):
   def testScalar(self):
       x = GradTensor([1], [1], 0)
       gt = "GradTensor\n  +1.000\nshape = (1), dtype = double, pivot = 0\n"
       self.assertEqual(str(x), gt)

   def test_1N_Vector(self):
       x = GradTensor([1, 2, 3], [1, 3], 0)
       gt = "GradTensor\n  +1.000  +2.000  +3.000\n\nshape = (1, 3), dtype = double, pivot = 0\n"
       self.assertEqual(str(x), gt)

   def test_N1_Vector(self): 
       x = GradTensor([1, 2, 3], [3, 1], 1)
       gt = "GradTensor\n  +1.000\n  +2.000\n  +3.000\n\nshape = (3, 1), dtype = double, pivot = 1\n"
       self.assertEqual(str(x), gt)

   def test_NM_Tensor(self):
       x = GradTensor([1, 2, 3, 4], [2, 2], 0)
       gt = (
           "GradTensor\n"
           "  +1.000  +2.000\n"
           "  +3.000  +4.000\n\n"
           "shape = (2, 2), dtype = double, pivot = 0\n"
       )
       self.assertEqual(str(x), gt)

   def test_1NM_Tensor(self):
       x = GradTensor([1, 2, 3, 4], [1, 2, 2], 0)
       gt = (
           "GradTensor\n[\n"
           "  +1.000  +2.000\n"
           "  +3.000  +4.000\n"
           "]\n\n"
           "shape = (1, 2, 2), dtype = double, pivot = 0\n"
       )
       self.assertEqual(str(x), gt)

   def test_N1M_Tensor(self):
       x = GradTensor([1, 2, 3, 4], [2, 1, 2], 2)
       gt = (
           "GradTensor\n[\n"
           "  +1.000  +2.000\n"
           "]\n"
           "[\n"
           "  +3.000  +4.000\n"
           "]\n\n"
           "shape = (2, 1, 2), dtype = double, pivot = 2\n"
       )
       self.assertEqual(str(x), gt)

   def test_NM1_Tensor(self):
       x = GradTensor([1, 2, 3, 4], [2, 2, 1], 1)
       gt = (
           "GradTensor\n[\n"
           "  +1.000\n"
           "  +2.000\n"
           "]\n"
           "[\n"
           "  +3.000\n"
           "  +4.000\n"
           "]\n\n"
           "shape = (2, 2, 1), dtype = double, pivot = 1\n"
       )
       self.assertEqual(str(x), gt)

   def test_1LMN_Tensor(self):
       pass

   def test_L1MN_Tensor(self):
       pass

   def test_LM1N_Tensor(self):
       pass

   def test_LMN1_Tensor(self):
       pass

if __name__ == "__main__": 
  unittest.main(verbosity=2)

