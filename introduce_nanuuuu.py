import tkinter as tk
from tkinter import font

def show_intro():
    root = tk.Tk()
    root.title("自己紹介")
    # ウィンドウのサイズ設定
    root.geometry("500x400")
    # 背景色を少し柔らかい色に
    root.configure(bg="#f0f4f8")

    # フォント設定
    title_font = font.Font(family="Helvetica", size=24, weight="bold")
    label_font = font.Font(family="Helvetica", size=16)
    value_font = font.Font(family="Helvetica", size=16, weight="bold")
    list_font = font.Font(family="Helvetica", size=14)

    # タイトル
    title_label = tk.Label(root, text="自己紹介", font=title_font, bg="#f0f4f8", fg="#333333")
    title_label.pack(pady=30)

    # 詳細情報を入れるフレーム
    details_frame = tk.Frame(root, bg="#f0f4f8")
    details_frame.pack(pady=10)

    # 名前
    tk.Label(details_frame, text="名前:", font=label_font, bg="#f0f4f8", fg="#555555").grid(row=0, column=0, sticky="e", padx=10, pady=5)
    tk.Label(details_frame, text="なぬううう", font=value_font, bg="#f0f4f8", fg="#2c3e50").grid(row=0, column=1, sticky="w", padx=10, pady=5)

    # 職業
    tk.Label(details_frame, text="職業:", font=label_font, bg="#f0f4f8", fg="#555555").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    tk.Label(details_frame, text="学生", font=value_font, bg="#f0f4f8", fg="#2c3e50").grid(row=1, column=1, sticky="w", padx=10, pady=5)

    # 趣味
    tk.Label(details_frame, text="趣味:", font=label_font, bg="#f0f4f8", fg="#555555").grid(row=2, column=0, sticky="ne", padx=10, pady=5)
    
    hobbies = ["寝る", "ゲーム", "読書"]
    hobbies_frame = tk.Frame(details_frame, bg="#f0f4f8")
    hobbies_frame.grid(row=2, column=1, sticky="w", padx=10, pady=5)
    for hobby in hobbies:
        tk.Label(hobbies_frame, text=f"• {hobby}", font=list_font, bg="#f0f4f8", fg="#34495e").pack(anchor="w")

    # 最後の挨拶
    closing_label = tk.Label(root, text="これからよろしくお願いします！", font=label_font, bg="#f0f4f8", fg="#e74c3c")
    closing_label.pack(pady=30)

    # ウィンドウを画面中央に表示するための処理
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # アプリケーションの実行
    root.mainloop()

if __name__ == "__main__":
    show_intro()