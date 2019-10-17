'''
Python Jupyter - Why do we need decorators in Python. One instance is we can test the
                 performance of our code. By wrapping our longTime function with a performance
                 function we are able to tell the runtime of our longTime function.
'''
#%%
from time import time

def performance(fn):
  def wrapper(*args, **kawrgs):
    t1 = time()
    result = fn(*args, **kawrgs)
    t2 = time
    print(f'it took {t1-t2} ms')
    return result

@performance
def longTime():
  for i in range(100000000):
    i*5

print(longTime())

#%%
