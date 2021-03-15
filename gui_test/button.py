import tkinter as tk

window = tk.Tk()
window.title("ECG monitor")
# window size
window.geometry('600x200')

# label
label_1 = tk.Label(window, text='test monitor label', font=("Arial Bold", 20))
label_1.grid(column=0, row=0)


# click event
def clicked():
    label_1.configure(text='Button was clicked')

# button
btn = tk.Button(window, text='Click button', bg='grey', command=clicked)
btn.grid(column=0, row=1)

window.mainloop()