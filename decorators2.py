'''
Python Jupyter - Decortors 2. Decortors super chrge our functions by wrpping our function
                 with nother function. Or by enhncing or chnging it.
'''
#%%
def myDecorator(func):
  def wrapFunc():
    print('**************')
    func()
    print('**************')

  return wrapFunc

@myDecorator
def hello():
  print('hellloo')

print(hello())

#%%
# Under the hood
def myDecorator(func):
  def wrapFunc():
    print('**************')
    func()
    print('**************')

  return wrapFunc

@myDecorator
def hello():
  print('hellloo')

myDecorator(hello)()
#%%
