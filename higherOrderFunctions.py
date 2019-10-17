'''
Python Jupyter - Higher Order Function. HOC can be 1 of two things. 1) A function that accepts
                 a function as a parameter. 2) A function that returns another function
'''
#%%
def greet(func):
  func()

def greet2():
  def func():
    return 5
  return func

print(greet2())

#%%
