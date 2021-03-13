import tkinter as tk
from tkinter.ttk import Combobox

window = tk.Tk()
window.title("ECG monitor")
# label
label_1 = tk.Label(window, text='test monitor label', font=("Arial Bold", 20))
label_1.grid(column=0, row=0)

# label_2 = tk.Label(window, text='input value')
# label_2.grid(column=0, row=1)
# label_3 = tk.Label(window, text='combo box')
# label_3.grid(column=0, row=2)

# window size
window.geometry('600x200')

# input entry(Entry class)
txt = tk.Entry(window, width=10)
txt.grid(column=1, row=1)
#
# # combobox
combo = Combobox(window)
combo['values'] = [1, 2, 3, 4, 5]
combo.current(0)
combo.grid(column=1, row=2)


# click event
def clicked():
    label_1.configure(text='Button was clicked')
    # label_2.configure(text=f'input value: {txt.get()}')
    # label_3.configure(text=f'selected combobox: {combo.get()}')


# button
btn = tk.Button(window, text='Click button', bg='grey', command=clicked)
btn.grid(column=1, row=0)

window.mainloop()
