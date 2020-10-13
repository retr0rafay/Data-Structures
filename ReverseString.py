def reverseString(string):
  backwards_name = []
  for i in range(len(string)):
    backwards_name.append(string[len(string) - 1 - i])
    
  return ''.join(backwards_name)

print(reverseString('Rafay'))
