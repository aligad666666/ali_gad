from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Identifying:

print("Name : Ali Ahmed Ahmed Mohamed Gad")
print("ID : 20170362")
print("Game Number : 2")
print("My Game Name : Tic Tac Toe")



Activeplayer=1 #==> To know The Turns Between Player_1 And Player_2:
Player_1=[]
Player_2=[]

#My Defaults:
board = [-100,-100,-100,-100,-100,-1000,-100,-100,-1000]  #Because If It Is [0,0,0,0,0,0,0,0,0]
optionsOdd=[1,3,5,7,9]                                       #[9]+[6]+[0]==15 And It's Error:
optionsEven=[0,2,4,6,8]                     

#My Design:
main=Tk()
main.title("Welcome To Ali's Game : Player 1 ")
style=ttk.Style()
style.theme_use('vista')


#Not Important Just For Show At The End:
def well():
    from turtle import Screen, Turtle, mainloop
    from time import clock, sleep

    def mn_eck(p, ne,sz):
        turtlelist = [p]
        #create ne-1 additional turtles
        for i in range(1,ne):
            q = p.clone()
            q.rt(360.0/ne)
            turtlelist.append(q)
            p = q
        for i in range(ne):
            c = abs(ne/2.0-i)/(ne*.7)
            # let those ne turtles make a step
            # in parallel:
            for t in turtlelist:
                t.rt(360./ne)
                t.pencolor(1-c,0,c)
                t.fd(sz)

    def main():
        s = Screen()
        s.bgcolor("black")
        p=Turtle()
        p.speed(0)
        p.hideturtle()
        p.pencolor("red")
        p.pensize(3)

        s.tracer(36,0)

        at = clock()
        mn_eck(p, 36, 19)
        et = clock()
        z1 = et-at

        sleep(1)

        at = clock()
        while any([t.undobufferentries() for t in s.turtles()]):
            for t in s.turtles():
                t.undo()
        et = clock()
        return "runtime: %.3f sec" % (z1+et-at)


    if __name__ == '__main__':
        msg = main()
        print(msg)
        mainloop()


# All Buttons:
bu1=ttk.Button(main,text=" ")
bu1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
bu1.config(command=lambda:Buclick(0))

bu2=ttk.Button(main,text=" ")
bu2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
bu2.config(command=lambda:Buclick(1))

bu3=ttk.Button(main,text=" ")
bu3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
bu3.config(command=lambda:Buclick(2))

bu4=ttk.Button(main,text=" ")
bu4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
bu4.config(command=lambda:Buclick(3))

bu5=ttk.Button(main,text=" ")
bu5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
bu5.config(command=lambda:Buclick(4))

bu6=ttk.Button(main,text=" ")
bu6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
bu6.config(command=lambda:Buclick(5))

bu7=ttk.Button(main,text=" ")
bu7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bu7.config(command=lambda:Buclick(6))

bu8=ttk.Button(main,text=" ")
bu8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bu8.config(command=lambda:Buclick(7))

bu9=ttk.Button(main,text=" ")
bu9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bu9.config(command=lambda:Buclick(8))


# Function To Make Turns Between Player_1 And Player_2 And To Get Buttons'Id:
def Buclick(id):
    global Activeplayer
    global Player_1
    global Player_2

    if(Activeplayer==1): # The Turn Of Player_1:
 
        inputOdd=int(input("Enter Odd: "))
        while(inputOdd not in optionsOdd):
            print("Numbers For Help ==> ",optionsOdd)
            inputOdd=int(input("Chose Numers From Them: "))
        optionsOdd.remove(inputOdd)
        SetLayout(id,inputOdd)
        Player_1.append(id)
        main.title("Welcome To Ali's Game : Player 2")
        Activeplayer=2
        board[id]=inputOdd        
        print("Player_1:{}".format(Player_1))


    elif(Activeplayer==2): # The Turn Of Player_2:
        
        inputEven=int(input("Enter Even: "))
        while(inputEven not in optionsEven):
            print("Numbers For Help ==> ",optionsEven)
            inputEven=int(input("Chose Numers From Them: ")) 
        optionsEven.remove(inputEven)
        SetLayout(id,inputEven)
        Player_2.append(id)
        main.title("Welcome To Ali's Game : Player 1")
        Activeplayer=1
        board[id]=inputEven
        print("Player_2:{}".format(Player_2))

    
    checkwiner()

def SetLayout(id,text):         # To avoid If The User Clicked The Same
                                # Button 2 Times (Make It disabled):
    if(id==0):
        bu1.config(text=text)
        bu1.state(['disabled'])

    elif(id==1):
        bu2.config(text=text)
        bu2.state(['disabled'])

    elif(id==2):
        bu3.config(text=text)
        bu3.state(['disabled'])

    elif(id==3):
        bu4.config(text=text)
        bu4.state(['disabled'])

    elif(id==4):
        bu5.config(text=text)
        bu5.state(['disabled'])

    elif(id==5):
        bu6.config(text=text)
        bu6.state(['disabled'])

    elif(id==6):
        bu7.config(text=text)
        bu7.state(['disabled'])

    elif(id==7):
        bu8.config(text=text)
        bu8.state(['disabled'])
        
    elif(id==8):
        bu9.config(text=text)
        bu9.state(['disabled'])


def checkwiner():
    winer=-1 # Default Value:

    if ((board[0] + board[1] + board[2] == 15) and (Activeplayer==2)):
        winer=1
        print("Player 1 Is The Winner!")

    if((board[0] + board[1] + board[2] == 15) and (Activeplayer==1)):     
        winer=2
        print("Player 2 Is The Winner!")
        
    if ((board[3] + board[4] + board[5]==15) and (Activeplayer==2)):
        winer=1
        print("Player 1 Is The Winner!")

    if ((board[3] + board[4] + board[5]==15) and (Activeplayer==1)):
        winer=2
        print("Player 2 Is The Winner!")

    if ((board[6] + board[7] + board[8]==15) and (Activeplayer==2)):
        winer=1
        print("Player 1 Is The Winner!")

    if ((board[6] + board[7] + board[8]==15) and (Activeplayer==1)):
        winer=2
        print("Player 2 Is The Winner!")

    if ((board[0] + board[3] + board[6]==15) and (Activeplayer==2)):
        winer=1
        print("Player 1 Is The Winner!")

    if ((board[0] + board[3] + board[6]==15) and (Activeplayer==1)):
        winer=2
        print("Player 2 Is The Winner!")

    if ((board[1] + board[4] + board[7]==15) and (Activeplayer==1)):
        winer=2
        print("Player 2 Is The Winner!")
            
    if ((board[1] + board[4] + board[7]==15) and (Activeplayer==2)):
        winer=1
        print("Player 1 Is The Winner!")

    if ((board[2] + board[5] + board[8]==15) and (Activeplayer==1)):
        winer=2
        print("Player 2 Is The Winner!")

    if ((board[2] + board[5] + board[8]==15) and (Activeplayer==2)):
        winer=1
        print("Player 1 Is The Winner!")

    if ((board[0] + board[4] + board[8]==15) and (Activeplayer==1)):
        winer=2
        print("Player 2 Is The Winner!")
        
    if ((board[0] + board[4] + board[8]==15) and (Activeplayer==2)):
        winer=1
        print("Player 1 Is The Winner!")

    if ((board[2] + board[4] + board[6]==15) and (Activeplayer==1)):
        winer=2
        print("Player 2 Is The Winner!")

    if ((board[2] + board[4] + board[6]==15) and (Activeplayer==2)):
        winer=1
        print("Player 1 Is The Winner!")

                                                # Message In A New Window:
    if(winer==1):
        messagebox.showinfo(title='Message',message='Player 1 Is The Winner Who Have Odd Numbers')

        well() # This Functions Just For show :

          
    if(winer==2):
        messagebox.showinfo(title='Massage',message='Player 2 Is The Winner Who Have Even Numbers')

        well() # This Functions Just For show :
