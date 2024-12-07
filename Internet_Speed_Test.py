from tkinter import *
import speedtest

def speedcheck():
    try:
        sp = speedtest.Speedtest()
        sp.get_best_server()
        down = str(round(sp.download() / (10**6), 2)) + " Mbps"
        up = str(round(sp.upload() / (10**6), 2)) + " Mbps"
        lb_down.config(text=down)
        lb_up.config(text=up)
    except Exception as e:
        lb_down.config(text="Error")
        lb_up.config(text="Error")
        print(f"Error: {e}")

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="blue")

lb = Label(sp, text="Internet Speed Test", font=("Times New Roman", 30, "bold"), bg="blue", fg="white")
lb.place(x=60, y=40, height=50, width=380)

lb = Label(sp, text="Downloading Speed", font=("Times New Roman", 30, "bold"))
lb.place(x=60, y=120, height=50, width=380)

lb_down = Label(sp, text="00 Mbps", font=("Times New Roman", 30, "bold"))
lb_down.place(x=60, y=200, height=50, width=380)

lb = Label(sp, text="Uploading Speed", font=("Times New Roman", 30, "bold"))
lb.place(x=60, y=290, height=50, width=380)

lb_up = Label(sp, text="00 Mbps", font=("Times New Roman", 30, "bold"))
lb_up.place(x=60, y=360, height=50, width=380)

bu = Button(sp, text="Check Speed", font=("Times New Roman", 30, "bold"), relief=RAISED, bg="red", command=speedcheck)
bu.place(x=60, y=460, height=50, width=380)

sp.mainloop()
