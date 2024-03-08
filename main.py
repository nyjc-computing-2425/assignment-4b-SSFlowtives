stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 'E', 'x', '.', '-', '^']
valid = False

caret_loc = stdform.find('^')
exponent = stdform[caret_loc + 1:]

if stdform.count('.') <= 1 and stdform.count('x') <= 1 and stdform.count('^') <= 1:
  for char in stdform:
    if char not in valid_chars:
      break
  else:
    temp = exponent.lstrip('-')
    if temp.isdigit():
      valid = True

if valid:
  x_loc = stdform.find('x')
  signficand = stdform[:x_loc]
  print(f"This number in E notation is {signficand}E{exponent}.")
else:
  print("Error converting to scientific E notation.")