def repeat(f):
  def any():
    print("start your function.")
    f()
    print("end your function.")
  return any  

@repeat

def hello():
  print("hello")

hello()
