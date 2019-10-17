'''
Python Jupyter - Decorators. Decorators are first class functions and can be identified
                 by the @ symbol
'''
#%%
def hello():
  print('hellllooo')

greet = hello # Greet is pointing in memory to the function Hello()
print(greet())

#%%
def hello(func):
  func()

def greet():
  print('stilll here!')

a = hello(greet)
print(a)

#%%
