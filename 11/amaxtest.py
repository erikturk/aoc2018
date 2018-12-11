import numpy as np

a=np.array([[[1,2,3],[4,5,6],[7,8,9]],
  [[10,11,12],[13,100,15],[16,17,18]],
  [[19,20,21],[22,23,24],[25,26,27]]])


print( np.amax(a))
print( np.argmax(a))
print( np.unravel_index(np.argmax(a),a.shape))
print( np.amax(a, axis=2))

