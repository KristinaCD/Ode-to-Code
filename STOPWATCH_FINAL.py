from tkinter import*
from tkinter import Label
from turtle import update
import time


running = False
hours = 0
minutes = 0
seconds = 0
lap_number = 0


def start():
    global running
    if not running:
        update()
        running= True

def stop():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running= False
        
def reset():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running= False 
        global hours, minutes, seconds,  lap_number 
        hours, minutes, seconds,  lap_number  = 0,0,0,0
        stopwatch_label.config(text="00:00:00")
        display.delete('1.0', END)
    
    if not running:
        stopwatch_label.after_cancel(update_time)
        running= False 
        hours, minutes, seconds, lap_number = 0,0,0,0
        stopwatch_label.config(text="00:00:00")
        display.delete('1.0', END)
        
def update():
    global hours, minutes, seconds
    seconds+= 1
    if seconds== 60:
        minutes+= 1
        seconds= 0
        
    if minutes== 60:
        hours+= 1
        minutes= 0
    
    hours_string= f"{hours}" if hours > 24 else f"0{hours}"  
    minutes_string= f"{minutes}" if minutes > 60 else f"0{minutes}"
    seconds_string= f"0{seconds}" if seconds < 10 else f"{seconds}"
    stopwatch_label.config(text= hours_string +":"+ minutes_string +":"+ seconds_string)
    global update_time
    update_time= stopwatch_label.after(1000, update)
    
    
root = Tk()
root.title("Digital Clock/Stopwatch")
root.geometry()

Label(root,font=("Times New Roman",25,"bold"),text="Stopwatch",fg="black").pack(pady= 15)

stopwatch_label=Label(root,text="00:00:00",fg="Black",font=("Times New Roman",40,"bold"))
stopwatch_label.pack()

start_button=Button(root,text="Start",height=4,width=6,font=("Arial",10,"bold"),bg="Green",fg="Black", command= start)
start_button.pack(side=LEFT)

lap_button=Button(root,text="Lap",height=4,width=6,font=("Arial",10,"bold"),bg="Purple",fg="Black")
lap_button.pack(side=LEFT)

resume_button=Button(root,text="Resume",height=4,width=6,font=("Arial",10,"bold"),bg="Yellow green",fg="Black")
resume_button.pack(side=LEFT)
        
stop_button=Button(root,text="Stop",height=4,width=6,font=("Arial",10,"bold"),bg="Red",fg="Black")
stop_button.pack(side=LEFT)

reset_button=Button(root,text="Reset",height=4,width=6,font=("Arial",10,"bold"),bg="Grey",fg="Black")
reset_button.pack(side=LEFT)

exit_button=Button(root,text="Exit",height=4,width=6,font=("Arial",10,"bold"),bg="White",fg="Black", command= quit)
exit_button.pack(side=LEFT)

display = Text(root,height=5,width=30,font=("Arial",10,"bold"))
display.pack(side=LEFT)

root.mainloop()
