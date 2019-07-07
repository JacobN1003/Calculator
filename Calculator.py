#Jacob Norenberg
#Simple Calculator
#July 7, 2019

from tkinter import *
root = Tk()
root.title("Jacob's Calculator")
number_string = ""
user_input = StringVar()

#=====Functions========
def buttonClear():
    global number_string
    number_string=""
    user_input.set("")
    
def buttonClick(number):
    global number_string
    number_string += str(number)
    user_input.set(number_string)

def buttonEqual():
    global number_string
    calculate = str(eval(number_string))
    user_input.set(calculate)
    number_string=""
    

#======Display==========
input_entry = Entry(root, textvariable = user_input, font=('arial',20,'bold'),
                    bd=20, width=15, bg="ghost white", justify='right').grid(row=0, pady=10, columnspan=4)
one = Button(root, command=lambda:buttonClick(1),width=2, font=('arial',20,'bold'),
             bd=10, fg="gray20",bg="snow", text="1").grid(row=1,column=0)
two = Button(root, command=lambda:buttonClick(2),width=2, font=('arial',20,'bold'),
             bd=10,fg="gray20",bg="snow",text="2").grid(row=1,column=1)
three = Button(root, command=lambda:buttonClick(3),width=2, font=('arial',20,'bold'),
               bd=10, fg="gray20",bg="snow",text="3").grid(row=1, column=2)
clear = Button(root, command=lambda:buttonClear(),width=2, font=('arial',20,'bold'),
               bd=10, fg="white",bg="PaleGreen4",text="C").grid(row=1, column=3)
four = Button(root, command=lambda:buttonClick(4),width=2, font=('arial',20,'bold'),
              bd=10, fg="gray20",bg="snow", text="4").grid(row=2,column=0)
five = Button(root, command=lambda:buttonClick(5),width=2, font=('arial',20,'bold'),
              bd=10, fg="gray20",bg="snow", text="5").grid(row=2,column=1)
six = Button(root, command=lambda:buttonClick(6),width=2, font=('arial',20,'bold'),
             bd=10, fg="gray20",bg="snow", text="6").grid(row=2,column=2)
divide = Button(root, command=lambda:buttonClick("/"),width=2, font=('arial',20,'bold'),
                bd=10, fg="gray20",bg="light gray", text=" / ").grid(row=2,column=3)
seven = Button(root, command=lambda:buttonClick(7),width=2, font=('arial',20,'bold'),
               bd=10, fg="gray20",bg="snow", text="7").grid(row=3,column=0)
eight = Button(root, command=lambda:buttonClick(8),width=2, font=('arial',20,'bold'),
               bd=10, fg="gray20",bg="snow", text="8").grid(row=3,column=1)
nine = Button(root, command=lambda:buttonClick(9),width=2, font=('arial',20,'bold'),
              bd=10, fg="gray20",bg="snow", text="9").grid(row=3,column=2)
multiply = Button(root, command=lambda:buttonClick("*"),width=2, font=('arial',20,'bold'),
                  bd=10, fg="gray20",bg="light gray", text=" * ").grid(row=3,column=3)
zero = Button(root, command=lambda:buttonClick(0),width=2, font=('arial',20,'bold'),
              bd=10, fg="gray20",bg="snow", text="0").grid(row=4,column=0)
add = Button(root, command=lambda:buttonClick("+"),width=2, font=('arial',20,'bold'),
             bd=10, fg="gray20",bg="light gray", text="+").grid(row=4,column=1)
subtract = Button(root, command=lambda:buttonClick("-"),width=2, font=('arial',20,'bold'),
                  bd=10, fg="gray20",bg="light gray", text="-").grid(row=4,column=2)
equals = Button(root, command=lambda:buttonEqual(),width=2, font=('arial',20,'bold'),
                bd=10, fg="gray20",bg="light gray", text="=").grid(row=4,column=3)


root.mainloop()

