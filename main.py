from tkinter import *
import win32com.client as wincom
#if __name__ == '__main__':
root = Tk()
root.title("Calculator")
root.geometry("538x575")
root.resizable(False, False)
root.configure(bg="gray1")
X="*"
equation = ""
def show(value):
    global equation
    equation += value


    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation,)

def calc():
    global equation
    result = ""
    if equation !="":
        try:
            result= eval(equation)
        except :
            result = "error"
            equation = ""

    label_result.config(text=result)





label_result = Label(root, width=54, height=3 , text="", font=("arial",30), bg="black", fg="white")
label_result.pack()

Button(root, text="AC", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="royalblue2",command=lambda:clear()).place(x=1,
                                                                                                                 y=144)
Button(root, text="←", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show(""),).place(x=135, y=144)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show("÷")).place(x=270, y=144)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="grey10", bg="azure3",
       command=lambda: show("/")).place(x=405, y=144)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show("7")).place(x=1, y=230)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show("8")).place(x=135, y=230)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show("9")).place(x=270, y=230)
Button(root, text="X", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="grey10", bg="azure3",
       command=lambda: show("*")).place(x=405, y=230)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show("4")).place(x=1, y=316)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show("5")).place(x=135, y=316)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show("6")).place(x=270, y=316)
Button(root, text="–", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="grey10", bg="azure3",
       command=lambda: show("-")).place(x=405, y=316)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show("1")).place(x=1, y=402)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show("2")).place(x=135, y=402)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show("3")).place(x=270, y=402)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="grey10", bg="azure3",
       command=lambda: show("+")).place(x=405, y=402)



Button(root, text="0", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show("0")).place(x=1, y=488)
Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=3, fg="azure3", bg="grey10",
       command=lambda: show(".")).place(x=135, y=488)
Button(root, text="=", width=11, height=1, font=("arial", 30, "bold"), bd=3, fg="grey10", bg="chocolate1",
       command=lambda: calc()).place(x=270, y=488)





root.mainloop()