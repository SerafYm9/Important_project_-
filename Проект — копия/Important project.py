import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime

temp = 0 
after_id = ""

def update_time():
    
    current_time = time.strftime("%H:%M:%S", time.localtime())
    label.config(text=current_time)

    label.after(1000, update_time)

def Tick_tack():
    global temp, after_id
    after_id = root.after(1000, Tick_tack)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label.config(text=str(f_temp))
    temp += 1 

def Stop():
    messagebox.showinfo("Повідомлення", "Таймер зупинено")
    root.after_cancel(after_id)
  
def start_over():
    Tick_tack


root = tk.Tk()
root.title("Поточний час")


label2 = tk.Label(root, font=("Helvetica", 48), fg="black")
label2.pack()
label = tk.Label(root, font=("Helvetica", 48), fg="black")
label.pack(padx= 50, pady= 70)
label3 = tk.Label(root, text = "Вітаємо у секундомірі!!!", font=("Helvetica", 14))
label3.pack()
#label4 = tk.Label(root, command = update_time)
#label4.pack()



tmer1 = tk.Button(root, text = "Старт",command=Tick_tack,bg = "green", padx = 30, pady= 30).pack()
tmer2 = tk.Button(root, text = "Стоп",command= Stop,bg = "red", padx = 30, pady= 30).pack()


#update_time()
root.mainloop() 