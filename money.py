from tkinter import *
from tkinter import ttk

root = Tk()
root.title("โปรแกรมแปลงสกุลเงิน")

#ค่าเงินต่อ 1 บาท ไทย
EUR = 0.028
JPY = 3.91
USD = 0.030
GBP = 0.025

#input
money = IntVar()
Label(text="จำนวนเงิน(THB)",padx=10,font=30).grid(row=0,sticky=W)
et1=Entry(font=30,width=30,textvariable=money)
et1.grid(row=0,column=1)

choice = StringVar(value="โปรดเลือกสกุลเงิน")
Label(text="เลือกสกลุเงิน",padx=10,font=30).grid(row=1,sticky=W)
Combo=ttk.Combobox(width=30,font=30,textvariable=choice)
Combo["values"]=("EUR","JPY","USD","GBP")
Combo.grid(row=1,column=1)

#output 
Label(text="ผลการคำนวน",padx=10,font=30).grid(row=2,sticky=W)
et2=Entry(font=30,width=30,)
et2.grid(row=2,column=1)

def calculate():
    amount=money.get()
    currency=choice.get()
    if currency == "EUR":
        et2.delete(0,END)
        result = (amount*EUR),"EUR(ยูโร)"
        et2.insert(0,result)
    elif currency == "JPY":
        et2.delete(0,END)
        result = (amount*JPY),"JPY(เยน)"
        et2.insert(0,result)
    elif currency == "USD":
        et2.delete(0,END)
        result = (amount*USD),"USD(ดอลล่า)"
        et2.insert(0,result)
    elif currency == "GBP":
        et2.delete(0,END)
        result = (amount*GBP),"GBP(ปอนด์)"
        et2.insert(0,result)
    else :
        et2.delete(0,END)
        result = "ไม่พบข้อมูล"
        et2.insert(0,result)
    
def clear():
    et1.delete(0,END)
    et1.insert(0, 0)
    et2.delete(0,END)
    Combo.delete(0,END)
    Combo.insert(0,"โปรดเลือกสกุลเงิน")


Button(text="คำนวน",font=50,width=15,command=calculate,background="gold").grid(row=3,column=1,sticky=W)
Button(text="ล้าง",font=50,width=15,command=clear,background="purple").grid(row=3,column=1,sticky=E)

root.mainloop()