from tkinter import *
import random as ran
from tkinter import messagebox

def generatePassword(event) :
    password.delete(0,END)    
    if length.get() != "" :
        lenstr = ""+length.get()+""
        if lenstr.isnumeric() :
            password.insert(0,generatedPassword())
        else :
            messagebox.showerror("Error","length field should be numaric")    
    else :
        messagebox.showerror("Error","length field not be empty")
    
    
def allClear(event) :
    length.delete(0,END)
    password.delete(0,END)

def generatedPassword() :
    gpassword = ""
    small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']    
    cap_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','+','-','/','|','}','{',':','?','.']
    all_val = small_letters+cap_letters+numbers+symbols
    
    for i in range(0,int(length.get())) :
        gpassword = gpassword+ran.choice(all_val)
    
    return gpassword




frame = Tk()
frame.title("Password Generator")
frame.geometry("500x300+500+100")

heading = Label(frame,text="Password Generator", font=("Arial Black",15), fg="blue").place(x=130,y=10)

lengthlb = Label(frame,text="Enter password length : ", font=("Arial Black",10), fg="brown")
lengthlb.place(x=50,y=70)

length = Entry(frame, width=10, font=("Arial Black",10), fg="green")
length.place(x=250,y=70)

passwordlb = Label(frame,text="Generated password : ", font=("Arial Black",10), fg="brown")
passwordlb.place(x=50,y=120)

password = Entry(frame, width=25, font=("Arial Black",10), fg="blue")
password.place(x=250,y=120)

submit = Button(frame, text="Generate Password", font=("Arial Black",10), bg="green", fg="white")
submit.place(x=100,y=200)

reset = Button(frame, text="Reset", font=("Arial Black",10), bg="red", fg="white")
reset.place(x=300,y=200)

submit.bind('<Button-1>',generatePassword)
reset.bind('<Button-1>',allClear)

frame.mainloop()