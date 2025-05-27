import tkinter as tk
from tkinter import ttk
import tiktoken

class TokenCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Token 计算器")
        self.root.geometry("600x400")
        
        # 設置樣式
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#2196F3")
        style.configure("TLabel", font=("微軟正黑體", 12))
        style.configure("TEntry", font=("微軟正黑體", 12))
        
        # 創建主框架
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 輸入區域
        ttk.Label(main_frame, text="请输入文字：").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.text_input = tk.Text(main_frame, height=10, width=50, font=("微軟正黑體", 12))
        self.text_input.grid(row=1, column=0, columnspan=2, pady=5)
        
        # 計算按鈕
        ttk.Button(main_frame, text="计算 Token", command=self.calculate_tokens).grid(row=2, column=0, pady=10)
        
        # 結果顯示
        self.result_label = ttk.Label(main_frame, text="Token 数量：0")
        self.result_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        
        # 說明文字
        info_text = "说明：\n1. 在文字框中输入任意文字\n2. 点击「计算 Token」按钮\n3. 系统会显示 token 数量"
        ttk.Label(main_frame, text=info_text, wraplength=400).grid(row=4, column=0, columnspan=2, pady=10)
        
    def calculate_tokens(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if text:
            try:
                encoding = tiktoken.get_encoding("cl100k_base")
                tokens = encoding.encode(text)
                self.result_label.config(text=f"Token 数量：{len(tokens)}")
            except Exception as e:
                self.result_label.config(text=f"计算错误：{str(e)}")
        else:
            self.result_label.config(text="请输入文字")

if __name__ == "__main__":
    root = tk.Tk()
    app = TokenCalculator(root)
    root.mainloop()

    