
from tkinter import *
from tkinter import messagebox
import random

color=['yellow','blue','green','black','red','purple','white','Orange','Brown']

score=0
score1 = 0
timeleft =30

def startgame(event):
    if timeleft == 30:
        countdown()
    nextcolor()


def nextcolor():
    global score
    global timeleft
    global score1
    # global score1
    if timeleft > 0:
        e.focus_set()
        if e.get().lower()==color[1].lower():
            score += 1
            
        e.delete(0,END)
        random.shuffle(color)
        label.config(fg=str(color[1]),text = str(color[0]))
        scorelbl.config(text="امتیاز:" + str(score) , font=('tahoma',12))
    
    else:
        e.get().lower()!=color[1].lower()
    score1 -= 1
    scorelbl1.config(text=" منفی امتیاز:" + str(score1) , font=('tahoma',12))


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -=1
        time.config(text='زمان:' + str(timeleft), font=('tahoma',12))
        
        if timeleft ==0:
            messagebox.showinfo('پایان زمان','زمان به پایان رسید')
        time.after(1000,countdown)

win = Tk()
win.geometry('400x300+300+100')
win.title('بازی با رنگ ها')
win.config(bg='purple')
lbl = Label(win , text='رنگ هر کلمه را به زبان انگلیسی وارد کنید',font= 'tahoma 12 bold' , fg='purple')
lbl.pack()

scorelbl=Label(win, text='بزنید تا بازی شروع شودEnter',font= 'tahoma 12 bold' , bg='purple' ,fg='pink')
scorelbl.pack()

scorelbl1=Label(win ,font= 'tahoma 12 bold' , bg='purple' ,fg='pink' )
scorelbl1.pack()

time=Label(win,text='زمان:'+ str(timeleft), font= 'tahoma 10 bold' , bg='purple')
time.pack()

label = Label(win , font=('comic sans ms',20))
label.pack()

e = Entry(win , width= 20)


win.bind('<Return>' , startgame)
e.pack()
e.focus_set()

win.mainloop()



win.mainloop()