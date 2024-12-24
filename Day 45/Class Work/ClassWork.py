def dup(arry):
    result = []
    
    for word in arry:
        changed_word = word[0]
        for i in range(1, len(word)):
            if word[i] != word[i-1]:
                changed_word += word[i]
        result.append(changed_word)
        
    return result


def count_vowels(word):
    count = 0
    for char in word:
        if char in "aeiouAEIOU":
            count += 1
    return count
# Test the functions

def bij(c):
  if (c == '1'): return 'a'
  if (c == '2'): return 'e'
  if (c == '3'): return 'i'
  if (c == '4'): return 'o'
  if (c == '5'): return 'u'
  if (c == 'a'): return '1'
  if (c == 'e'): return '2'
  if (c == 'i'): return '3'
  if (c == 'o'): return '4'
  if (c == 'u'): return '5'
  return  c

encode = decode = lambda st: ''.join(map(bij,st))  

def main(): 
  print(encode('hello'))
  print(decode('h2ll4'))
  print(dup(['Hello', 'World', 'Python']))

  