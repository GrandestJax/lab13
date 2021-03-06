#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")
rectangle = drawpad.create_rectangle(140, 100, 100, 120, fill='cyan')
rectangle2 = drawpad.create_rectangle(600, 490, 540, 510, fill='purple')
rectangle3 = drawpad.create_rectangle(300, 300, 320, 320, fill='yellow')
dir1 = 5
dir2 = 5
dir3 = 5
# Create your "enemies" here, before the class


def animate2():
    global dir1
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(rectangle)
    if x2 > drawpad.winfo_width(): 
        dir1 = -6
    elif x1 < 0:
        dir1 = 6
    #Move our oval object by the value of direction
    drawpad.move(rectangle,dir1,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(5, animate2)
animate2()

def animate3():
    global dir2
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(rectangle2)
    if x2 > drawpad.winfo_width(): 
        dir2 = -5
    elif x1 < 0:
        dir2 = 5
    #Move our oval object by the value of direction
    drawpad.move(rectangle2,dir2,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(5, animate3)
animate3()

def animate4():
    global dir3
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(rectangle3)
    if x2 > drawpad.winfo_width(): 
        dir3 = - 3
    elif x1 < 0:
        dir3 = 3
    #Move our oval object by the value of direction
    drawpad.move(rectangle3,dir3,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(5, animate4)
animate4()

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "yellow")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "green")
       	    self.down.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "red")
       	    self.right.grid(row=0,column=3)
       	    # Bind an event to the first button
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "blue")
       	    self.left.grid(row=0,column=2)
       	    # Bind an event to the first button
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    	
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
        
        def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
	   
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
		
app = MyApp(root)
root.mainloop()
