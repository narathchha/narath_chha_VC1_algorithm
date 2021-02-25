import tkinter as tk
# Create an empty window
root = tk.Tk()
# Set TK window size to width 600 px and height 200 px
root.geometry("550x600")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame()
# Set the title of the frame
frame.master.title("Hello PNC")
canvas = tk.Canvas(frame) 
def DrawGird():
   for row in range(9):
    for column in range(9):
        oval=canvas.create_rectangle((row*50+50, column*50+50, 100+(row*50),100+(column*50)) ,fill="white")
# Load the image
myImage = tk.PhotoImage(file='.\player.png')
# Add the image to the canvas
myImageId = canvas.create_image(20, 20, image=myImage)
# HERE YOU CAN START TO DRAW
DrawGird()
# pack means "draw what i put inside" 
canvas.pack(expand=True, fill='both') 
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()