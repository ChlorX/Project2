import tkinter as tk
window  = tk.Tk()
def schot(*args):
    f = "задано число {}".format(chislo.get())
    frame1.configure(text=f)
    x=int(chislo.get())
    if x <= 6:
        y = x + x ** 0.5
    else:
        y = x * x ** 0.5
    f = ('y =', y)
    frame2.configure(text=f)
frame1=tk.Label(window,text='Введите X')
chislo=tk.Entry(window,width=50)
frame2=tk.Label(window)
frame1.pack()
chislo.pack()
frame2.pack()
window.bind('<Return>',schot)
window.mainloop()