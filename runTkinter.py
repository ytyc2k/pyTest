import tkinter as tk

def on_button_click():
    label.config(text="按钮被点击！")

root = tk.Tk()
root.title("我的 Tkinter 应用")

label = tk.Label(root, text="欢迎使用 Tkinter")
label.pack()

button = tk.Button(root, text="点击我", command=on_button_click)
button.pack()

root.mainloop()