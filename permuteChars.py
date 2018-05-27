def swap(string, A, B):
  charA = string[A]
  charB = string[B]
  letters = list(string)
  letters[A] = charB
  letters[B] = charA
  return ''.join(letters)


def permute(string, current, final):
  if (current == final):
    print(string)

  for i in range(current, final + 1):
    variation = swap(string, current, i)
    permute(variation, current + 1, final)
  return;


def permuteAll(string):
  permute(string, 0, len(string) - 1)
  return;


permuteAll('ABC')
