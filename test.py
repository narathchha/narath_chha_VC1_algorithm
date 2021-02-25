#  IMPORTS
import tkinter as tk
#  CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SIZE=50
MARGIN=120
#  VARIABLES
grid = [0,0,1,0,0,0,0]
def arrayToDrawing():
    global grid
    for index in range(len(grid)):
        x1=SIZE*index+MARGIN
        x2=SIZE+x1
        y1=SIZE
        y2=SIZE+y1
        for i in range(5):
            if grid[index]==1  :
                color="black" 
            else:
                color="white"
            canvas.create_rectangle(x1,y1,x2,y2 ,fill=color)
    
    return None
# draw a line with white and black squares using the global array
# def MoveLeft(event):
#     global grid
#     left = 0
#     for index in range(len(grid)):
#         if grid[index] == 1:
#             left=index
#     if left > 0:
#         grid[left] = 0
#         grid[left-1] = 1
#     arrayToDrawing()
#     print(grid)
# def MoveRigth(event):
#     global grid
#     right= 0
#     for value in range(len(grid)):
#         if grid[value] == 1:
#             right=value
#     if right < len(grid)-1:
#         grid[right] = 0
#         grid[right+1] = 1
#     arrayToDrawing()
#     print(grid)
# MAIN
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
# root.bind("<Left>", MoveLeft) #LEFT CLICK
# root.bind("<Right>",MoveRigth )  #RIGHT CLICK
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill="both")
arrayToDrawing()
root.mainloop()
