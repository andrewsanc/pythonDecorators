'''
Python Jupyter - Decortors 3.
'''
#%%
def myDecorator(func):
  def wrapFunc(greet):
    print('**************')
    func(greet)
    print('**************')

  return wrapFunc

@myDecorator
def hello(greeting):
  print(greeting)

hello('hiiiiii!')

#%%
