points = [1, 3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]

def letToOffset(let):
  xlet = ord(let)
  if xlet >= 97:
      xlet -= 97
  elif xlet >= 65:
      xlet -= 65
  return xlet

#the variable xlet is now the offset into points list for each letter
# THINK:  How can you apply this code to the problem at had for the scrabble score for a word?

let = input("Input a letter: ")

letterOffset = letToOffset(let)
