import tkinter as tk

window = tk.Tk()
window.title("ECG monitor")

# label
label_1 = tk.Label(window, text='test monitor label', font=("Arial Bold", 20))
label_1.grid(column=0, row=0)

# label with StringVar
txt_var = tk.StringVar()
label_2 = tk.Label(window, textvariable=txt_var)
label_2.grid(column=1, row=0)

# window size
window.geometry('600x200')

# entry
txt = tk.Entry(window, width=10)
txt.grid(column=0, row=2)
txt2 = tk.Entry(window, textvariable=txt_var)
txt2.grid(column=1, row=1)


# click event
def clicked():
    label_1.configure(text=f'input value is "{txt.get()}"')
    # txt_var.set('set test')


# button
btn = tk.Button(window, text='Click button', bg='grey', command=clicked)
btn.grid(column=0, row=1)

window.mainloop()
