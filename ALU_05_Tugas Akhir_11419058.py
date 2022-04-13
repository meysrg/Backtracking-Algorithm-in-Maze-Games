import turtle
from random import randint
from turtle import Turtle, Screen

Maze = turtle.Turtle()
screen = turtle.Screen()
screen.title("Bactracking pada Maze")
screen.tracer(0)

Maze.speed(0)
Maze.hideturtle()

STRING = "Welcome to Maze Game"

FONT_SIZE = 25
DELTA_SIZE = 2
FONT = ("Ariel", FONT_SIZE, "normal")
OUTLINE_FONT = ("Ariel", FONT_SIZE + 2 * DELTA_SIZE, "bold")

screen = Screen()

turtle = Turtle(visible=False)
turtle.speed('fastest')
turtle.penup()

X, Y = -220, 220

turtle.goto(X, Y)

for letter in STRING:
    turtle.color('#030354')
    oldx = turtle.xcor()
    turtle.write(letter, move=True, align="left", font=OUTLINE_FONT)
    newx = turtle.xcor()

    turtle.color(screen.bgcolor())
    turtle.setposition(oldx + (newx - oldx) // 2, Y + DELTA_SIZE)
    turtle.write(letter, align="center", font=FONT)
    turtle.setposition(newx, Y)

def text(message,x,y,size):
    Maze.penup()
    Maze.goto(x,y)    		  
    Maze.write(message,align="left",font=('Arial', size, 'normal'))

def labirin(intDim):
    Maze.begin_fill()
    Maze.forward(intDim)
    Maze.left(90)
    Maze.forward(intDim)
    Maze.left(90)
    Maze.forward(intDim)
    Maze.left(90)
    Maze.forward(intDim)
    Maze.end_fill()
    Maze.setheading(0)
    
clr = ["#ffffff","#000000","#04ad07","#abe1ff","#ffc811"]
lab =    [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
lab.append([0,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1])
lab.append([1,0,0,1,0,1,1,1,0,0,0,1,0,1,0,1])
lab.append([1,1,0,1,0,0,0,1,1,0,1,0,0,1,0,1])
lab.append([1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1])
lab.append([1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1])
lab.append([1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,1])
lab.append([1,0,0,0,1,0,1,0,1,1,0,1,0,1,1,1])
lab.append([1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1])
lab.append([1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,1])
lab.append([1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1])
lab.append([1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1])
lab.append([1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1])
lab.append([1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1])
lab.append([1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,2])
lab.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

def drawMaze(lab):
  boxSize = 26
  Maze.penup()
  Maze.goto(-210,180)
  Maze.setheading(0)
  for i in range (0,len(lab)):
    for j in range (0,len(lab[i])):
	    Maze.color(clr[lab[i][j]])
	    labirin(boxSize)
	    Maze.penup()
	    Maze.forward(boxSize)
	    Maze.pendown()	
    Maze.setheading(270) 
    Maze.penup()
    Maze.forward(boxSize)
    Maze.setheading(180) 
    Maze.forward(boxSize*len(lab[i]))
    Maze.setheading(0)
    Maze.pendown()
	
#Backtracking
def solveMaze(lab,row,col):
    if lab[row][col]==2:
      return True
    elif lab[row][col]==0:
      lab[row][col]=3
      Maze.clear()
      drawMaze(lab)
      Maze.getscreen().update()
      if row<len(lab)-1:
        if solveMaze(lab,row+1,col):
          return True
      if row>0:
        if solveMaze(lab,row-1,col):
          return True
      if col<len(lab[row])-1:
        if solveMaze(lab,row,col+1):
          return True
      if col>0:
        if solveMaze(lab,row,col-1):
          return True
      
      lab[row][col]=4    
      Maze.clear()
      drawMaze(lab) 
      Maze.getscreen().update()
      
      print("Backtrack")
  
drawMaze(lab)


solved = solveMaze(lab,1,0)
if solved:
  print("Solusi Ditemukan")
  text("Solusi Ditemukan",-80,-260,20)
else:  
  print("Tidak Ditemukan Solusi")
  text("Tidak Ditemukan Solusi",-130,-260,20)

turtle.done()
