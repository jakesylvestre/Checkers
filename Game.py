from random import randint

#Classes for Game Pieces
class checker(object):
  def __init__(self,team,x,y):
    self.team = team
    self.x = x
    self.y = y
  def move(up, side):
    y = y+1
    if side == "left":
      x = x+1
      if x > 1:
        x = x-1
        print ("Incorrect Move. Loss of Turn")
    elif side == "right":
      x = x-1
      if x < 1:
        x = x + 1
        print ("Incorrect Move. Loss of Turn")
    else:
      print ("Incorrect Move. Loss of Turn")
class king(checker):
  def move(up,side):
    if up == "up":
      y = y+1
      if y > 8:
          y = y-1
          print ("Incorrect Move. Loss of Turn")
    elif up == "down":
      y = y-1
      if y < 1:
          y = y+1
          print ("Incorrect Move. Loss of Turn")
    else:
      print ("Incorrect Move. Loss of Turn")
    if move == "left":
      x = x+1
      if x > 8:
          x = x-1
          print ("Incorrect Move. Loss of Turn")
    elif move == "right":
      x = x-1
      if x < 1:
          x = x+1
          print ("Incorrect Move. Loss of Turn")
    else:
      print ("Incorrect Move. Loss of Turn")
def check_king(checker):
   if checker.y > 8:
     checker = king(checker.team, checker.x, checker.y)
     checker.y = checker.y - 1
red = []
#Adding Checkers
#USE ARRAYS
#make a for
red.append(checker("red", 2, 1))
red.append(checker("red", 4, 1))
red.append(checker("red", 6, 1))
red.append(checker("red", 8, 1))
red.append(checker("red", 1, 2))
red.append(checker("red", 3, 2))
red.append(checker("red", 5, 2))
red.append(checker("red", 7, 2))
red.append(checker("red", 2, 3))
red.append(checker("red", 4, 3))
red.append(checker("red", 6, 3))
red.append(checker("red", 8, 3))

black = []

black.append(checker("black", 1, 8)
black.append(checker("black", 3, 8)
black.append(checker("black", 5, 8)
black.append(checker("black", 7, 8)
black.append(checker("black", 2, 7)
black.append(checker("black", 4, 7)
black.append(checker("black", 6, 7)
black.append(checker("black", 8, 7)
black.append(checker("black", 1, 6)
black.append(checker("black", 3, 6)
black11 = checker("black", 5, 6)
black12 = checker("black", 7, 6)

#Giving Checkers to Each Player
user_checkers = [red1, red2, red3, red4, red5, red6, red7, red8, red9, red10, red11, red12]
cpu_checkers = [black1, black2, black3, black4, black5, black6, black7, black8, black9, black10, black11, black12]

#Defining Moves for Each Player
def user_move(up, side):
  

#Game
game = True
while game:
