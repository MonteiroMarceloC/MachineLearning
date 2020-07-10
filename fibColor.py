def fun(arg):
  print(arg)

fun('aa')

'''
def do(xxx):
  xxx += [xxx[-1]+xxx[-2]]

def validate(xxx):
  if xxx[-1] < xxx[-2]:
    xxx = xxx[0:len(xxx-2)]
    return True
  return False

current = 1
last = 0
next = 1

red = [0, 1]
green = [0, 1]
blue = [0, 1]
allColors = [red, green, blue]

for r in red:
  for g in green:
    for b in blue:
      do(blue)
      if(validate(blue)):
        break
    do(green)
    if(validate(green)):
      break
  do(red)
  if validate(red):
    break



#ffffff

def next (self, current, old):
  return current + old

