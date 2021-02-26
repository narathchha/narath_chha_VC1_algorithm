import tkinter as tk 
#make empty window
root=tk.Tk()
# put screenwidth and 
root.geometry("600x600")
#veriable for stalled
grid = [[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,2,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,2]]
frame=tk.Frame()
frame.master.title("Hey,Let Play Crazy Game")
myImage=0
myFlag=0
def drawGrid():
    global myImage,myFlag
    for col in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[col][row]==1:
                # Load the image
                myImage = tk.PhotoImage(file='.\player.png')
                # Add the image to the canvas
                myImageId = canvas.create_image(70,70,image=myImage)
                # canvas.create_rectangle((row*50+50, col*50+50, 100+(row*50),100+(col*50)) ,fill="white")
            else:
                canvas.create_rectangle((row*50+50, col*50+50, 100+(row*50),100+(col*50)) ,fill="white")

            if grid[9][9]==2:
                #  Load the image
                myFlag = tk.PhotoImage(file='.\flag.png')
                # Add the image to the canvas
                myImaged = canvas.create_image(500,500,image=myFlag)
    canvas.create_rectangle(100,50,450,100,fill="green")   
    canvas.create_rectangle(200,150,250,450,fill="green")   
    canvas.create_rectangle(300,200,500,250,fill="green")   
    canvas.create_rectangle(300,300,350,450,fill="green")   
    canvas.create_rectangle(350,350,550,400,fill="green")   
    canvas.create_rectangle(50,350,150,400,fill="green")   
    canvas.create_rectangle(100,400,150,450,fill="green")   
    canvas.create_rectangle(100,200,150,350,fill="green")  
    canvas.create_rectangle(50,500,500,550,fill="green")  
    return None
def moveLeft(event):
    global grid 
    indexX=-1
    indexY=-1
    for col in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[col][row]==1:
                indexX=row
                indexY=col
    if  indexX>0:
        grid[indexY][indexX]=0
        grid[indexY][indexX-1]=1
    drawGrid()
    
def moveRight(event):
    global grid
    indexX=-1
    indexY=-1
    for col in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[col][row]==1:
                indexX=row
                indexY=col
    if indexX<len(grid)-1:
        grid[indexY][indexX]=0
        grid[indexY][indexX+1]=1
    drawGrid()
def moveUp(event):
    global grid
    indexX=-1
    indexY=-1
    for col in range(len(grid)):
        for row in range(len(grid[0])):
           if grid[col][row]==1:
               indexX=row
               indexY=col
    if  indexY>0:
        grid[indexY][indexX]=0
        grid[indexY-1][indexX]=1
    drawGrid()
def moveDown(event):
    global grid
    indexX=-1
    indexY=-1
    for  col in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[col][row]==1:
                indexX=row
                indexY=col
    if indexY<len(grid)-1:
        grid[indexY][indexX]=0
        grid[indexY+1][indexX]=1
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

