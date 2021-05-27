from tkinter import*
from tkinter import messagebox

root = Tk()
root.title('TicTacToe')

class Board:
    def __init__(self):
        self.b = []
        self.player = "X"
        self.scores = {
        "X": -10,
        "O": 10,
        "tie": 0
        }
        for i in range(3):
            self.b.append(i)
            self.b[i] = []
            x = i
            for j in range(3):
                y = j 
                self.b[i].append(j)
                self.b[i][j] = Button(root, text=" ",font=("Helvetica", 20), height = 3, 
                width = 6,bg="SystemButtonFace",
                command = lambda curr_but1=i,curr_but2=j:self.click(self.b[curr_but1][curr_but2],curr_but1,curr_but2))
                self.b[i][j].grid(row=x,column=y)
    
    def click(self,b,i,j):
        if self.player == "X":
            if self.b[i][j]["text"] == " ":  
                self.b[i][j]["text"] = "X"
                self.b[i][j].config(state = DISABLED)
                self.player = "O"
        self.print_tie()
        self.bestMove()

        
    def checkwinner(self):
        winner = " "

        for i in range(3):
            if (self.b[i][0]["text"] == self.b[i][1]["text"]) and (self.b[i][0]["text"] == self.b[i][2]["text"]) and (self.b[i][0]["text"] != " "):
                winner = self.b[i][0]["text"]

        for i in range(3):
            if (self.b[0][i]["text"] == self.b[1][i]["text"]) and (self.b[0][i]["text"] == self.b[2][i]["text"]) and (self.b[0][i]["text"] != " "):
                winner = self.b[0][i]["text"]

        if (self.b[0][0]["text"] == self.b[1][1]["text"]) and (self.b[0][0]["text"] == self.b[2][2]["text"]) and (self.b[0][0] != " "):
                winner = self.b[0][0]["text"]

        if (self.b[2][0]["text"] == self.b[1][1]["text"]) and (self.b[2][0]["text"] == self.b[0][2]["text"]) and (self.b[2][0]["text"] != " "):
                winner = self.b[2][0]["text"]

        spaces = 0
        for i in range(3):
            for j in range(3):
                if self.b[i][j]["text"] == " ":
                    spaces += 1
        
        if winner == " " and spaces == 0:
            return "tie"
        else:
            return winner

    def disableall(self):
        for i in range(3):
            for j in range(3):
                self.b[i][j].config(state = DISABLED) 

    def bestMove(self):
        bestScore = float('-inf')
        Move = (0,0)
        for i in range(3):
            for j in range(3):
                if self.b[i][j]["text"] == " ":
                    self.b[i][j]["text"] = "O"
                    score = self.minimax(self.b,0,False)
                    self.b[i][j]["text"] = " "
                    if score > bestScore:
                        bestScore = score
                        Move = (i,j)

        if self.b[Move[0]][Move[1]]["text"] == " ": 
            self.b[Move[0]][Move[1]]["text"] = "O"
        
        
        self.b[Move[0]][Move[1]].config(state = DISABLED)
        self.print()
        self.player = "X"

    def minimax(self,b,depth,isMaximizing):

        result = self.checkwinner()

        if result != " ":
            return self.scores[result]

        if isMaximizing == True:
            bestScore = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.b[i][j]["text"] == " ":
                        self.b[i][j]["text"] = "O"
                        score = self.minimax(self.b,depth+1,False)
                        self.b[i][j]["text"] = " "
                        bestScore = max(bestScore,score)
            return bestScore

        else:
            bestScore = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.b[i][j]["text"] == " ":
                        self.b[i][j]["text"] = "X"
                        score = self.minimax(self.b,depth+1,True)
                        self.b[i][j]["text"] = " "
                        bestScore = min(bestScore,score)
            return bestScore
    
    def print(self):
        result = self.checkwinner()
        if result != " " and result != "tie":
            messagebox.showinfo(title = "GameOver", message=str(result)+" wins!")
            self.disableall()
    
    def print_tie(self):
        result = self.checkwinner()
        if result != " ":
            if result == "tie":
                messagebox.showinfo(title = "GameOver", message="Tie!")
                self.disableall()
            else:
                messagebox.showinfo(title = "GameOver", message=str(result)+" wins!")
                self.disableall()

def reset():
        board = Board()




board = Board()
my_menu = Menu(root)
root.config(menu=my_menu)
options_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Options",menu = options_menu)
options_menu.add_command(label="Reset Game",command = reset)
root.mainloop()