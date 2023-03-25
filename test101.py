import tkinter as tk

def execure():
    txt = "こんにちは"
    lbl.configure(text=txt)

root = tk.Tk()
root.title("こんにちはテスト")
root.geometry("200x100")

lbl = tk.label(text="")
btn = tk.Button(text="実行", command = execure)

lbl.pack()
btn.pack()
tk.mainloop()