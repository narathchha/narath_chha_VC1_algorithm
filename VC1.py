import tkinter as tk 
from tkinter import messagebox
#make empty window
root=tk.Tk()
# put screenwidth and 
root.geometry("600x600")
#veriable for stalled
grid = [
[1,4,4,4,4,4,4,4,4,0,0],
[0,2,2,2,2,2,2,2,2,0,0],
[0,0,4,4,4,4,4,4,4,4,4],
[0,0,2,2,2,2,2,2,2,0,4],
[0,0,8,0,4,2,4,4,4,4,4],
[0,0,0,0,4,2,0,0,0,0,0],
[0,0,0,7,4,2,0,0,0,0,0],
[0,0,0,5,4,2,0,0,6,0,0],
[0,0,4,4,4,2,0,0,0,3,0],
[0,0,2,2,2,2,2,2,2,0,0]]
frame=tk.Frame()
frame.master.title("Hey,Let's Play Crazy Game")
myImage= tk.PhotoImage(file='player.png')
myFlag = tk.PhotoImage(file='flags.png')
myCoins = tk.PhotoImage(file='coinsilver.png')
# myDiamond = tk.PhotoImage(file='diamond2.png')
myAnemie1 = tk.PhotoImage(file='anemie1.png')
myAnemie2 = tk.PhotoImage(file='anemies2.png')
myAnemie3 = tk.PhotoImage(file='anemies3.png')
# Display Background
bg=tk.PhotoImage(file='background2.png')
# canvas.create_image(0,0, image=bg,anchor="nw")
# Sound
# import Sound
# winsound.PlaySound("error2.wav",winsound.SND_FILENAME)
# Founction



def drawGrid():
    global myImage,myFlag,myCoins,myDiamond,myAnemie1,myAnemies2,myAnemies3
    canvas.delete("all")
    canvas.create_image(50,50, image=bg)

    for col in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[col][row]==1:
                # Add the image to the canvas
                # myImageId = canvas.create_image(80,90,image=myImage)
                canvas.create_image(row*50+70, col*50+70,image=myImage)
            elif grid[col][row]==2:
                canvas.create_rectangle((row*50+50, col*50+50, 100+(row*50),100+(col*50)) ,outline="green", fill="green")
            elif grid[col][row]==3:
                canvas.create_image(row*50+70, col*50+70,image=myFlag)
            elif grid[col][row]==4:
                canvas.create_image(row*50+70, col*50+70,image=myCoins)
            # elif grid[col][row]==5:
                # canvas.create_image(row*50+70, col*50+70,image=myDiamond)
            elif grid[col][row]==6:
                canvas.create_image(row*50+70, col*50+70,image=myAnemie1)
            elif grid[col][row]==7:    
                canvas.create_image(row*50+70, col*50+70,image=myAnemie2)
            elif grid[col][row]==8:    
                Move=canvas.create_image(row*50+70, col*50+70,image=myAnemie3)
    return None
def moveAnemie():
    canvas.move(Move,2,2)
def displayMessageWin():
    messagebox.showinfo("Title", "You Win!")
def moveLeft(event):

    global grid 
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]==1:
                indexRow=row
                indexCol=col
    if indexCol>0:
        if grid[indexRow][indexCol-1]==2:
            displayMessageWin()
        if grid[indexRow][indexCol-1]!=2:
            grid[indexRow][indexCol]=0
            grid[indexRow][indexCol-1]=1
    drawGrid()
    
def moveRight(event):
    global grid
    # indexX=-1
    # indexY=-1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]==1:
                indexRow=row
                indexCol=col
    if indexCol <len(grid[0])-1:
        if grid[indexRow][indexCol+1]==3:
            displayMessageWin()
        if grid[indexRow][indexCol+1]!=2:
            grid[indexRow][indexCol]=0
            grid[indexRow][indexCol+1]=1
    drawGrid()
def moveUp(event):
    global grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]==1:
                indexRow=row
                indexCol=col
    if indexRow >0:
        if grid[indexRow-1][indexCol]==3:
            displayMessageWin()
        if grid[indexRow-1][indexCol]!=2:
            grid[indexRow][indexCol]=0
            grid[indexRow-1][indexCol]=1
    drawGrid()
def moveDown(event):
    global grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]==1:
                indexRow=row
                indexCol=col
    if indexRow <len(grid)-1:
        if grid[indexRow+1][indexCol]==3:
            displayMessageWin()
        if grid[indexRow+1][indexCol]!=2:
            grid[indexRow][indexCol]=0
            grid[indexRow+1][indexCol]=1
    drawGrid()
canvas=tk.Canvas(root)
root.bind("<Left>",moveLeft)#move to left
root.bind("<Right>",moveRight)#move to right
root.bind("<Up>",moveUp)#move to up
root.bind("<Down>",moveDown)#move to down
#move ball
# canvas.after(1000,lambda:moveBall1(ball1))
canvas.pack(expand=True,fill='both')
drawGrid()
root.resizable(False,False)
root.mainloop()

