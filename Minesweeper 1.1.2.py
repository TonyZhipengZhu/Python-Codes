import random
import time
from tkinter import *
import tkinter

#Board class to represent the game boards - visible and not visible
class Board:
    '''"."= Unclicked blank space;
    "B"= Bomb; "F"= Flag; "P"= Flag on top of bomb;
    "O"= clicked blank space; numbers indicate clicked on spaces with bombs adj;
    symbols "!@#$%^&*" indicate unclicked spcaes with bombs adj'''
    #Constructor to generate an empty map of some size, then randomly
    #add some number of bombs
    def __init__(self, size, bombs):
        #Initial click values are captured before board generation
        self.x1 = 0
        self.y1 = 0
        #All maps are square
        self.size = size
        #All Maps have a number of bombs
        self.bombs = bombs
        #Flag counter starts at number of bombs
        self.flags = bombs
        #All Maps have a number of open spaces
        self.opens = (self.size**2) - self.bombs
        #Maps have points parameter
        self.points = 0
        #Timer function starts at 0
        self.time = 0
        #num2symb dictionary converts bombnumbers to symbols
        self.num2symb = dict()
        self.num2symb[1] = "!"
        self.num2symb[2] = "@"
        self.num2symb[3] = "#"
        self.num2symb[4] = "$"
        self.num2symb[5] = "%"
        self.num2symb[6] = "^"
        self.num2symb[7] = "&"
        self.num2symb[8] = "*"
        #symb2num dictionary converts bombsymbols to numbers
        self.symb2num = dict()
        self.symb2num ["!"] = 1
        self.symb2num ["@"] = 2
        self.symb2num ["#"] = 3
        self.symb2num ["$"] = 4
        self.symb2num ["%"] = 5
        self.symb2num ["^"] = 6
        self.symb2num ["&"] = 7
        self.symb2num ["*"] = 8
        #Generate empty map
        self.rowlist = []
        #Add each row to the list
        for i in range(self.size):
            #put the row into the master list
            current_row = []
            self.rowlist = self.rowlist + [current_row]
            #Put the open space symbol in all the columns for the row
            for x in range(self.size):
                self.rowlist[i] = self.rowlist[i] + ["."]
    #countUp for timer function (legacy)

    def countUp(self):
        while self.time < 1000:
            time.sleep(1)
            self.time = self.time + 1
    
    def addBombs(self):
        '''adds self.bombs number of bombs randomly (no duplicates) to the map of
        self.size size ... does not add bomb at (self.x1, self.y1)'''
        bList = []
        bHist = dict()
        bHist [str(self.x1) + "," + str(self.y1+1)] = "first click"
        bHist [str(self.x1) + "," + str(self.y1)] = "first click"
        bHist [str(self.x1) + "," + str(self.y1-1)] = "first click"
        bHist [str(self.x1+1) + "," + str(self.y1+1)] = "first click"
        bHist [str(self.x1+1) + "," + str(self.y1)] = "first click"
        bHist [str(self.x1+1) + "," + str(self.y1-1)] = "first click"
        bHist [str(self.x1-1) + "," + str(self.y1+1)] = "first click"
        bHist [str(self.x1-1) + "," + str(self.y1)] = "first click"
        bHist [str(self.x1-1) + "," + str(self.y1-1)] = "first click"
        
        while len(bList) < 2*self.bombs:
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)
            if not (str(x) + "," + str(y) in bHist):
                bHist[str(x) + "," + str(y)] = "point"
                bList = bList + [x,y]
            else:
                pass
        
        #While loop scans bList and creates bombs in the map
        i = 0
        while i < len(bList) - 1:
            x = bList[i]
            y = bList[i+1]
            i = i + 2
            self.rowlist[y][x] = "B"
        print("Addbombs Done")

    def bombCheck(self, x, y, num):
        '''Checks surroundings for bombs and creates a number at (x, y).  When num == True, returns integer.
        When num == False, returns symbol'''
        out = 0
        #bomblist contains bomb characters that should return numbers
        bomblist = ["B","P"]
        if self.rowlist[y][x] in bomblist:
            return self.rowlist[y][x]
        if y-1 >= 0 and y-1 < self.size and x-1 >= 0 and x-1 < self.size:
            if self.rowlist[y-1][x-1] in bomblist:
                out = out + 1
            else:
                pass          
        if x-1 >= 0 and x-1 <= self.size-1:
            if self.rowlist[y][x-1] in bomblist:
                out = out + 1
            else:
                pass     
        if y+1 >= 0 and y+1 < self.size and x-1 >= 0 and x-1 < self.size:
            if self.rowlist[y+1][x-1] in bomblist:
                out = out + 1
            else:
                pass
        if y-1 >= 0 and y-1 < self.size:
            if self.rowlist[y-1][x] in bomblist:
                out = out + 1
            else:
                pass
        if y+1 >= 0 and y+1 < self.size:
            if self.rowlist[y+1][x] in bomblist:
                out = out + 1
            else:
                pass
        if y-1 >= 0 and y-1 < self.size and x+1 >= 0 and x+1 < self.size:     
            if self.rowlist[y-1][x+1] in bomblist:
                out = out + 1
            else:
                pass
        if x+1 >= 0 and x+1 < self.size:
            if self.rowlist[y][x+1] in bomblist:
                out = out + 1
            else:
                pass     
        if y+1 >= 0 and y+1 < self.size and x+1 >= 0 and x+1 < self.size:
            if self.rowlist[y+1][x+1] in bomblist:
                out = out + 1
            else:
                pass
        if out == 0:
            return "."
        else:
            if num:
                return out
            else:
                return self.num2symb[out]

    def bombNumber(self):
        '''Checks for bombs in vicinity and writes bomb symbols to entire initial map'''
        #For loop checks for all bombs and adds surroundCheck symbols
        for y in range(self.size):
            for x in range(self.size):
                self.rowlist[y][x] = self.bombCheck(x, y, False)
                
    def addFlag(self, x, y):
        '''adds and removes flags at (x, y)'''
        blankslist = [".","!","@","#","$","%","^","&","*"]
        if self.rowlist[y][x] in blankslist:
            self.rowlist[y][x] = "F"
            self.flags = self.flags - 1
        elif self.rowlist[y][x] == "B":
            self.rowlist[y][x] = "P"
            self.points = self.points + 1
            self.flags = self.flags - 1
        elif self.rowlist[y][x] == "P":
            self.rowlist[y][x] = "B"
            self.points = self.points - 1
            self.flags = self.flags + 1
        elif self.rowlist[y][x] == "F":
            self.rowlist[y][x] = self.bombCheck(x, y, False)
            self.flags = self.flags - 1

    

    def opensCheck(self):
        '''Scans map for characters that represent spaces not yet clicked on and returns the number of them'''
        openslist = [".","!","@","#","$","%","^","&","*"]
        opens = 0
        for y in range(self.size):
            for x in range(self.size):
                if self.rowlist[y][x] in openslist:
                    opens = opens + 1
        self.opens = opens
        return self.opens

    #Display the map
    def display(self):
        '''Displays the map in the console'''
        for row in self.rowlist:
            #print each character
            for col in row:
                print(col, end=' ')
                #print a new line
            print("")

    #Aux Function to Display Extra Parameters
    def param(self):
        print("Opens:",self.opens,"Points:",self.points, "Flags left:", self.flags, "Bombs:", self.bombs)

    #Floodclick Function to open up all adjacent open spaces
    def floodClick(self, x, y):
        '''Opens all blank spaces adjacent to (x, y)'''
        #if ".", turn it to "O", if in bombsymbs, turn it to number
        bombsymbs = ["!","@","#","$","%","^","&","*"]
        if self.rowlist[y][x] == ".":
            self.rowlist[y][x] = "O"
            self.floodClick(x, y)
        if self.rowlist[y][x] in bombsymbs:
            self.rowlist[y][x] = self.symb2num[self.rowlist[y][x]]
            return
        if x-1 >= 0 and x-1 <= self.size-1:
            if self.rowlist[y][x-1] == ".":
                self.rowlist[y][x-1] = "O"
                self.floodClick(x-1, y)
            elif self.rowlist[y][x-1] in bombsymbs:
                self.rowlist[y][x-1] = self.symb2num[self.rowlist[y][x-1]]
            else:
                pass     
        if y-1 >= 0 and y-1 < self.size:
            if self.rowlist[y-1][x] == ".":
                self.rowlist[y-1][x] = "O"
                self.floodClick(x, y-1)
            elif self.rowlist[y-1][x] in bombsymbs:
                self.rowlist[y-1][x] = self.symb2num[self.rowlist[y-1][x]]
            else:
                pass
        if y+1 >= 0 and y+1 < self.size:
            if self.rowlist[y+1][x] == ".":
                self.rowlist[y+1][x] = "O"
                self.floodClick(x, y+1)
            elif self.rowlist[y+1][x] in bombsymbs:
                self.rowlist[y+1][x] = self.symb2num[self.rowlist[y+1][x]]
            else:
                pass
        if x+1 >= 0 and x+1 < self.size:
            if self.rowlist[y][x+1] == ".":
                self.rowlist[y][x+1] = "O"
                self.floodClick(x+1, y)
            elif self.rowlist[y][x+1] in bombsymbs:
                self.rowlist[y][x+1] = self.symb2num[self.rowlist[y][x+1]]
            else:
                pass     
        else:
            return

    def isEmpty(self):
        charlist = ["!","@","#","$","%","^","&","*","B","F","P","O"]
        for y in range(self.size):
            for x in range(self.size):
                if self.rowlist[y][x] in charlist:
                    return False
                else:
                    pass
        else:
            print("map empty")
            return True

    #A Function that looks at coords where user clicked
    def clickCheck(self, x, y):
        '''Looks at click location, generates bomb locations, and decides win/loss and floodclick'''
        if self.isEmpty():
            #empty map - now it generates the map after the first click
            self.x1 = x
            self.y1 = y
            self.addBombs()
            self.bombNumber()
            self.floodClick(x, y)
            print("MapGen Done.")
        if self.rowlist[y][x] == "B":
            'you lose function'
            return
        if self.rowlist[y][x] == "F" or self.rowlist == "P":
            return
        blankslist = [".","!","@","#","$","%","^","&","*"]
        if self.rowlist[y][x] in blankslist:
            self.floodClick(x, y)
            self.opensCheck()
            print("Opens:",self.opens, "Points:", self.points)
        if self.points == self.bombs and self.opens == 0:
            'you win function'

#Prompt user for both board size and number of bombs
size = int(input("What size square board? (1 integer): "))
bombs = int(input("How many bombs? "))
#x1 = int(input("initial x: "))
#y1 = int(input("initial y: "))
board = Board(size, bombs)
#board.clickCheck(x1, y1)
#board.addFlag(0,0)
#board.addFlag(3,3)
board.param()

class GUI:
    def __init__(self,size):
        self.size=size

    def base(self):
        self.master=tkinter.Tk()
        for i in range(self.size):
            for j in range(self.size):
                if board.rowlist[j][i]== ".":
                    tkinter.Label(self.master, relief=RAISED,width=4,height=2).grid(row=i,column=j)
                else:
                    tkinter.Label(self.master, text="no",relief=RAISED,width=4,height=2).grid(row=i,column=j)        
        self.master.mainloop() 

    def GUIbase(self):
        self.board = [ [1]*self.size for _ in range(self.size) ]
        self.root = tkinter.Tk() 
    
    def seeSpace(self):
        for j in range(self.size):
            for i in range(self.size):
                if board.rowlist[j][i]== "O":
                    tkinter.Label(self.root, relief=RIDGE,text="  ",bg="white").grid(row=j,column=i)
                elif board.rowlist[j][i]== 1:
                    tkinter.Label(self.root, relief=RIDGE,text="1",bg="white").grid(row=j,column=i)
                elif board.rowlist[j][i]== 2:
                    tkinter.Label(self.root, relief=RIDGE,text="2").grid(row=j,column=i)
                elif board.rowlist[j][i]== 3:
                    tkinter.Label(self.root, relief=RIDGE,text="3").grid(row=j,column=i)
                elif board.rowlist[j][i]== 4:
                    tkinter.Label(self.root, relief=RAISED,text="4").grid(row=j,column=i)
                elif board.rowlist[j][i]== 5:
                    tkinter.Label(self.root, relief=RAISED,text="5").grid(row=j,column=i)
                elif board.rowlist[j][i]== 6:
                    tkinter.Label(self.root, relief=RAISED,text="6").grid(row=j,column=i)
                elif board.rowlist[j][i]== 7:
                    tkinter.Label(self.root, relief=RAISED,text="7").grid(row=j,column=i)
                elif board.rowlist[j][i]== 8:
                    tkinter.Label(self.root, relief=RAISED,text="8").grid(row=j,column=i)
                else:
                    pass

    def on_click(self,i,j,event):
        board.clickCheck(i,j)
        if board.rowlist[j][i] == "B":
            color = "red"
            event.widget.config(bg=color)
        else: 
            color = "white"
            event.widget.config(bg=color)
            self.seeSpace()

    def GUI_display(self):
        for j,row in enumerate(self.board):
            for i,column in enumerate(row):
                self.L = tkinter.Label(self.root,text='    ',relief=RAISED,bg='grey')
                self.L.grid(row=j,column=i)
                self.L.bind('<Button-1>',lambda e,i=i,j=j: BIGboy.on_click(i,j,e))
                #self.L.bind('<>',lambda e,i=i,j=j: BIGboy.on_click(i,j,e))
        #self.root.mainloop()    

BIGboy=GUI(size)
BIGboy.GUIbase()
BIGboy.GUI_display()
#board.clickCheck(BIGboy.on_click())#board.clickCheck(BIGboy.on_click())

