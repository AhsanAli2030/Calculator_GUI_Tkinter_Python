from tkinter import *
rootVariable=Tk()





rootVariable.title("Simple Calculator")
entryVariable=Entry(rootVariable,width=45,borderwidth=5)                          # width is 3 times greater then padding
entryVariable.grid(row=0,column=0,padx=10,pady=10,columnspan=4)

def buttonclick(number):
    valueinBox=entryVariable.get()                         # 1st value taken is stored in variable and the it is cleared by del funct then second
    entryVariable.delete(0,END)
    entryVariable.insert(0,str(valueinBox)+str(number))
  
def buttonClear():
    entryVariable.delete(0,END)

def buttonAdd():
    global first_number,math
    math="Addition"
    first_number=int(entryVariable.get())
    entryVariable.delete(0,END)


def buttonEquals():
    global secondNumber
    
    secondNumber=int(entryVariable.get())
    entryVariable.delete(0,END)
    if(math=="Addition"):
            answer=first_number+secondNumber
    elif(math=="Subtraction"):
         answer=first_number-secondNumber
    elif(math=="Multiplication"):
         answer=first_number*secondNumber
    elif(math=="Divide"):
         answer=(first_number)/(secondNumber)  

    entryVariable.insert(0,answer)




def buttonSubtract():
    global first_number,math
    math="Subtraction"
    first_number=int(entryVariable.get())
    entryVariable.delete(0,END)

def buttonMultiply():
    global first_number,math
    math="Multiplication"
    first_number=int(entryVariable.get())
    entryVariable.delete(0,END)

def buttonDivide():
    global first_number,math
    math="Divide"
    first_number=int(entryVariable.get())
    entryVariable.delete(0,END)

button_7=Button(rootVariable,padx=40,pady=20,text="7",command=lambda:buttonclick(7))
button_8=Button(rootVariable,padx=40,pady=20,text="8",command=lambda:buttonclick(8))
button_9=Button(rootVariable,padx=40,pady=20,text="9",command=lambda:buttonclick(9))
button_6=Button(rootVariable,padx=40,pady=20,text="6",command=lambda:buttonclick(6))
button_5=Button(rootVariable,padx=40,pady=20,text="5",command=lambda:buttonclick(5))
button_4=Button(rootVariable,padx=40,pady=20,text="4",command=lambda:buttonclick(4))
button_3=Button(rootVariable,padx=40,pady=20,text="3",command=lambda:buttonclick(3))
button_2=Button(rootVariable,padx=40,pady=20,text="2",command=lambda:buttonclick(2))
button_1=Button(rootVariable,padx=40,pady=20,text="1",command=lambda:buttonclick(1))
button_0=Button(rootVariable,padx=40,pady=20,text="0",command=lambda:buttonclick(0))
button_clear=Button(rootVariable,padx=40,pady=20,text="C",command=buttonClear)
button_equal=Button(rootVariable,padx=40,pady=20,text="=",command=buttonEquals)
button_add=Button(rootVariable,padx=40,pady=20,text="+",command=buttonAdd)
button_subtract=Button(rootVariable,padx=40,pady=20,text="-",command=buttonSubtract)
button_multiply=Button(rootVariable,padx=40,pady=20,text="X",command=buttonMultiply)
button_divide=Button(rootVariable,padx=40,pady=20,text="/",command=buttonDivide)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_6.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_4.grid(row=2,column=2)
button_3.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_1.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1)
button_add.grid(row=1,column=3)
button_subtract.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)
button_equal.grid(row=4,column=3)
button_divide.grid(row=4,column=2)

rootVariable.mainloop()