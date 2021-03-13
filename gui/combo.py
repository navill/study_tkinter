import tkinter as tk
from tkinter.ttk import Combobox

window = tk.Tk()
window.title("ECG monitor")
# label
label_1 = tk.Label(window, text='test monitor label', font=("Arial Bold", 20))
label_1.grid(column=0, row=0)

# window 크기 지정
window.geometry('600x200')

# combobox 설정
combo = Combobox(window)  # combobox 객체 생성(어디에 위치시킬 것인지 매개변수 입력)
combo['values'] = [1, 2, 3, 4, 5]  # 값 설정
combo.current(0)  # default: values중 몇 번째 값을 default 값으로 쓸 것인지 설정
combo.grid(column=0, row=0)  # 콤보박스 창을 메인창의 어디에 위치 시킬 것인지 설정

window.mainloop()
