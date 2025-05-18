import fire

def hello(name="World"):
  print("hello first");

  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)