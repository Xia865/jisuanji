import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("计算器")
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # 获取用户名称
        self.get_username()
        
    def get_username(self):
        self.name_window = tk.Toplevel(self.window)
        self.name_window.title("输入用户名")
        self.name_window.geometry("300x100")
        
        tk.Label(self.name_window, text="请输入您的名字:").pack(pady=10)
        self.name_entry = tk.Entry(self.name_window)
        self.name_entry.pack()
        
        tk.Button(self.name_window, text="确认", command=self.check_name).pack(pady=10)
        
    def check_name(self):
        name = self.name_entry.get()
        if "otto" in name.lower() or "一秒" in name:
            messagebox.showerror("不是你用你妈呀", "开源区不欢迎你们这些废物")
            self.window.quit()
        else:
            self.name_window.destroy()
            self.create_calculator()
            
    def create_calculator(self):
        # 创建显示框
        self.display = tk.Entry(self.window, width=35, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # 按钮文本
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]
        
        # 创建按钮
        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.click(x)
            tk.Button(self.window, text=button, width=5, command=command).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
                
    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "错误")
        elif key == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)
            
    def on_closing(self):
        if messagebox.askokcancel("退出", "你他妈真的要滚吗？"):
            self.window.destroy()
            
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()