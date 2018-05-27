import math

def addition(a, b):
  return a + b

def subrtraction(a, b):
  return a - b

def multiplication(a, b):
  return a * b

def division(a, b):
  return a / b

operations = {
  '+': addition,
  '-': subrtraction,
  '*': multiplication,
  '/': division
}

def postFix(string):
  stack = []
  tokens = string.split(' ')

  for token in tokens:
    if token.isdigit():
      stack.append(float(token))
    elif token in operations:
      b = stack.pop()
      a = stack.pop()

      value = operations[token](a, b)
      stack.append(value)

  if len(stack) > 1:
    print('Input Error')

  return stack[0]


print(postFix('1 2 +'))
