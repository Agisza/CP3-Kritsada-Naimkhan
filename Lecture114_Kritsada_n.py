from time import strftime
from tkinter import *
from tkinter import ttk
from datetime import date, datetime
from currency_converter import CurrencyConverter
import calendar
import matplotlib.pyplot as plt
from tkinter import messagebox


# funtion แลกเงิน
def convert_rate():
    if   currency_first_comb.get() == "" or currency_first_comb.get() == "" or value_entry.get() == "" :
        messagebox.showerror("Error", "กรุณเลือกข้อมูลหรือใส่ข้อมูลให้ครับถ้วน")
        pass
    else :
        try :
            result = CurrencyConverter(fallback_on_wrong_date=True,fallback_on_missing_rate=True).convert(float(value_entry.get()), currency_first_comb.get(), currency_second_comb.get(), date=datetime.now()) 
            result_label.configure(text=("%.2f")%(result))
        except:
            messagebox.showerror("Error", "กรุณาใส่ข้อมูลเป็นตัวเลข")


# funtion สร้างกราฟ
def plot_graph(): 
    if   currency_first_comb.get() == "" or currency_first_comb.get() == "" :
        messagebox.showerror("Error", "กรุณเลือกข้อมูล")
        pass
    else :    
        list_year=[]
        list_value=[]
        now_month = datetime.now().month
        for i in range(now_month) :
            list_year.append(i+1)
            add_list =  float("{:.2f}".format(CurrencyConverter(fallback_on_wrong_date=True,fallback_on_missing_rate=True).convert(1, currency_first_comb.get(), currency_second_comb.get(), date=date(2021, i+1, 15))))
            list_value.append(add_list)

        # พอทกราฟ
        plt.plot(list_year,list_value)   
        plt.xlabel('Month')
        plt.ylabel('Unit')
        plt.title('Exchange per 1 unit')
        plt.show()
    

# ส่วน window หลัก
main_window = Tk()
main_window.title("อัตราแลกเปลี่ยนเงิน")
main_window.geometry("280x400")

# ส่วน Frame หัวเรื่อง
header_frame =Frame(main_window, bd="4")
header_frame.grid(row=0, column=0 )

# ส่วน Frame เนื้อหา
main_frame = Frame(main_window , bd="8")
main_frame.grid(row=1, column=0 )

# ส่วน Frame กราฟ
graph_frame = Frame(main_window , bd="8")
graph_frame.grid(row=2, column=0 )

# combox เลือกหน่วยเงิน
currency_first_comb = ttk.Combobox(main_frame, font=("Angsana New", 16), width=10)
currency_first_comb["value"] = ["THB", "USD", "EUR", "JPY", "GBP"]
currency_first_comb.grid(row=2, column=0 ,)

currency_second_comb = ttk.Combobox(main_frame, font=("Angsana New", 16), width=10)
currency_second_comb["value"] = ["THB", "USD", "EUR", "JPY", "GBP"]
currency_second_comb.grid(row=2, column=2)

# label ต่างๆ
header_label = Label(header_frame, text="อัตราแลกเปลี่ยนเงินประจำวันที่ : " + datetime.now().strftime("%d/%m/%Y") , font=("Angsana New", 16), bg="#D1DDDB")
header_label.grid(row=0,column=1)

exchang_label = Label(main_frame, text=">>>", font=("Angsana New", 16), width=4)
exchang_label.grid(row=2, column=1)

exchang01_label = Label(main_frame, text="หน่วยการซื้อ :", font=("Angsana New", 16))
exchang01_label.grid(row=1, column=0)

exchang02_label = Label(main_frame, text="หน่วยการขาย :", font=("Angsana New", 16))
exchang02_label.grid(row=1, column=2)

exchang03_label = Label(main_frame, text="จำนวนเงิน :", font=("Angsana New", 16))
exchang03_label.grid(row=3, column=0)

exchang04_label = Label(main_frame, text="จำนวนเงิน :", font=("Angsana New", 16))
exchang04_label.grid(row=3, column=2)

# Label แสดงผลลัพท์
result_label = Label(main_frame, text="----", font=("Angsana New", 16))
result_label.grid(row=4, column=2)

# Textbox ใส่จำนวนเงิน
value_entry = Entry(main_frame,  font=("Angsana New", 16), width=12)
value_entry.grid(row=4, column=0)

# ปุ่มกด
convert_button = Button(main_frame , text = "แลกเปลี่ยน" , font=("Angsana New", 16), command=convert_rate)
convert_button.grid(row=5,column=1)

trand_button = Button(graph_frame , text = "ดูกราฟอัตราแลกเปลี่ยนต่อ 1 หน่วย" , font=("Angsana New", 16), command=plot_graph)
trand_button.grid(row=1,column=1)


main_window.mainloop()