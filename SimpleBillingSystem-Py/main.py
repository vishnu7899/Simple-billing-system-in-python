# module mane: main
import read
import purchase
import write

again = "Y"
while again.upper() == "Y":
    a = read.read_file()
    b = purchase.purchase(a)
    write.over_write(a, b)
    again = input("\nAre there any new customers waiting to buy product? ")
print("\nThank you for shopping from our store!!")
print("Please check your invoice for your shopping details, \nWhich we have created in .txt file format.")

from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
root =Tk()
root.geometry("500x300")
def getvals():
    if angryvalue.get()==1:
        messagebox.showinfo("YOUR RESPONSE IS RECORDED","THANK YOU FOR YOUR RESPONSE ")
    elif sadvalue.get()==1:
        messagebox.showinfo("YOUR RESPONSE IS RECORDED","THANK YOU FOR YOUR RESPONSE")
    elif calmvalue.get()==1:
        messagebox.showinfo("YOUR RESPONSE IS RECORDED","THANK YOU FOR YOUR RESPONSE")
    elif happyvalue.get()==1:
        messagebox.showinfo("YOUR RESPONSE IS RECORDED","THANK YOU FOR YOUR RESPONSE")
    else:
        messagebox.showinfo("YOUR RESPONSE IS RECORDED","THANK YOU FOR YOUR RESPONSE")

    print("excepted")

Label(root,text="ENTER YOUR RESPONSE\n",font="arial 10 bold").grid(row=0,column=3)
angry=Label(root,text="1.WORST",font="arial 10 bold")
sad=Label(root,text="2.UNSATISFIES",font="arial 10 bold")
calm=Label(root,text="3.SATISFIED",font="arial 10 bold")
happy=Label(root,text="4.GOOD",font="arial 10 bold")
excited=Label(root,text="5.EXECELLENT",font="arial 10 bold")

angry.grid(row=1,column=2)
sad.grid(row=2,column=2)
calm.grid(row=3,column=2)
happy.grid(row=4,column=2)
excited.grid(row=5,column=2)

angryvalue=IntVar()
sadvalue=IntVar()
calmvalue=IntVar()
happyvalue=IntVar()
excitedvalue=IntVar()

angryentry=Checkbutton(root,text="\U0001F620",onvalue=1,offvalue=0,font="arial 20 bold",variable =angryvalue)
sadentry=Checkbutton(root,text="\U0001F614",onvalue=1,offvalue=0,font="arial 20 bold",variable =sadvalue)
calmentry=Checkbutton(root,text="\U0001F607",onvalue=1,offvalue=0,font="arial 20 bold",variable =calmvalue)
happyentry=Checkbutton(root,text="\U0001F606",onvalue=1,offvalue=0,font="arial 20 bold",variable =happyvalue)
excitedentry=Checkbutton(root,text="\U0001F973",onvalue=1,offvalue=0,font="arial 20 bold",variable =excitedvalue)

angryentry.grid(row=1,column=3)
sadentry.grid(row=2,column=3)
calmentry.grid(row=3,column=3)
happyentry.grid(row=4,column=3)
excitedentry.grid(row=5,column=3)

Button(text="submit",command=getvals).grid(row=6,column=3)

root.mainloop()