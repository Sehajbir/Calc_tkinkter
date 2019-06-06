from tkinter import *
import re
def btnClick(numbers):
    global operator
    operator = operator+str(numbers)
    txt_input.set(operator)

def btnPress(event):
    a = repr(event.char)
    if(a == "\'\\r\'"):
        print(a)
        btnEquate()
    elif(a == "\'\\x08\'"):
        print(a)
        btnClear()
    elif(a == "\'\\x1b\'"):
        calculator.quit()
    else:
        a = re.sub('\'', '', a)
        btnClick(a)
def btnClear():
    global operator
    operator = ""
    txt_input.set(operator)

def btnEquate():
    global operator
    result = str(eval(operator))
    txt_input.set(result)
    operator=""

class btn:
    def __init__(self, master, r, c, t):
        self.btn = Button(master, width = 8, height=4, bd=1, fg="black", bg="ghost white", text=t, command=lambda:btnClick(t))
        self.btn.grid(row=r, column=c)
calculator = Tk()
calculator.title("Calculator")
operator = ""
txt_input = StringVar()

txt_display = Entry(calculator, textvariable = txt_input, font=('arial', 16), bd=3,  bg="lightgrey", justify='right').grid(columnspan=4) 
########################################
#Row 1
btn7 = btn(calculator, 1, 0, 7)
btn8 = btn(calculator, 1, 1, 8)
btn9 = btn(calculator, 1, 2, 9)
btnMul = btn(calculator, 1, 3, '*')

########################################
#Row 2
btn4 = btn(calculator, 2, 0, 4)
btn5 = btn(calculator, 2, 1, 5)
btn6 = btn(calculator, 2, 2, 6)
btnMin = btn(calculator, 2, 3, '-')
########################################
#Row 3
btn1 = btn(calculator, 3, 0, 1)
btn2 = btn(calculator, 3, 1, 2)
btn3 = btn(calculator, 3, 2, 3)
btnMin = btn(calculator, 3, 3, '+')
########################################
#Row 4
btn0 = btn(calculator, 4, 0, 0)
btnClr = Button(calculator, width = 8, height=4, bd=1, fg="black", bg="ghost white", text='C', command=lambda:btnClear())
btnClr.grid(row=4, column=1)
btnEq =  Button(calculator, width = 8, height=4, bd=1, fg="black", bg="ghost white", text='=', command=lambda:btnEquate())
btnEq.grid(row=4, column=2)
btnDiv = btn(calculator, 4, 3, '/')

frame = Frame(calculator)
frame.focus_set()
frame.bind('<Key>', btnPress)
frame.grid(row=5, columnspan=4)

calculator.mainloop()