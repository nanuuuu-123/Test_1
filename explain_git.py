import tkinter as tk
from tkinter import ttk, font

def create_git_explainer():
    root = tk.Tk()
    root.title("Git & GitHub 初心者ガイド")
    root.geometry("750x650")
    root.configure(bg="#f8f9fa")

    # フォント設定
    title_font = font.Font(family="Helvetica", size=20, weight="bold")
    text_font = font.Font(family="Helvetica", size=13)
    code_font = font.Font(family="Consolas", size=13, weight="bold")
    
    # タイトル
    tk.Label(root, text="🌱 Git & GitHub はじめてのガイド", font=title_font, bg="#f8f9fa", fg="#24292e").pack(pady=15)

    # タブ（Notebook）のスタイル設定
    style = ttk.Style()
    style.theme_use('default')
    style.configure("TNotebook", background="#f8f9fa", borderwidth=0)
    style.configure("TNotebook.Tab", font=("Helvetica", 11), padding=[10, 5])
    style.configure("TFrame", background="#ffffff")
    
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both", padx=20, pady=10)

    # タブの中身を作るための便利関数
    def create_tab_content(parent, content_parts):
        frame = tk.Frame(parent, bg="#ffffff")
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        for part_type, part_text in content_parts:
            if part_type == "text":
                tk.Label(frame, text=part_text, font=text_font, justify="left", bg="#ffffff", wraplength=650).pack(anchor="nw", pady=(0, 10))
            elif part_type == "code":
                tk.Label(frame, text=part_text, font=code_font, bg="#eef1f5", fg="#d73a49", padx=10, pady=5).pack(anchor="w", padx=20, pady=(0, 15))

    # ----------------------------------------
    # タブ1: 基本
    # ----------------------------------------
    tab_intro = ttk.Frame(notebook)
    notebook.add(tab_intro, text="基本")
    intro_parts = [
        ("text", "【Git（ギット）とは？】\nゲームの「セーブ機能」のようなものです！\nファイルをいつ、誰が、どう変更したかの履歴を記録してくれます。\n間違えてファイルを消してしまっても、過去の状態に戻すことができます。\n\n【GitHub（ギットハブ）とは？】\nGitのセーブデータをインターネット上に保存・共有する「クラウドサービス」です。\n他の人と一緒に一つの作品（プログラムなど）を作る時にとても便利です。")
    ]
    create_tab_content(tab_intro, intro_parts)

    # ----------------------------------------
    # タブ2: クローン
    # ----------------------------------------
    tab_clone = ttk.Frame(notebook)
    notebook.add(tab_clone, text="1. クローン (Clone)")
    clone_parts = [
        ("text", "【クローン（Clone）とは？】\nGitHub上にあるプロジェクトのデータを、自分のパソコンに「丸ごとコピー」してくることです。\n\n【やり方】\n1. GitHubのページを開き、緑色の「<> Code」ボタンをクリックしてURLをコピーします。\n2. 自分のパソコンでターミナル（黒い画面）を開き、以下のコマンドを入力します："),
        ("code", "git clone [コピーしたURL]"),
        ("text", "（例）\ngit clone https://github.com/nanuuuu-123/Test_1.git\n\nこれだけで、パソコンの中にプロジェクトのフォルダが作成されます！")
    ]
    create_tab_content(tab_clone, clone_parts)

    # ----------------------------------------
    # タブ3: ブランチ
    # ----------------------------------------
    tab_branch = ttk.Frame(notebook)
    notebook.add(tab_branch, text="2. ブランチ (Branch)")
    branch_parts = [
        ("text", "【ブランチ（Branch）とは？】\nメインのストーリー（大元のコード）に影響を与えずに、「別の世界線（分岐）」を作って安全に作業するための機能です。\n\n【やり方】\n新しいブランチを作成して、その世界線に移動するコマンド："),
        ("code", "git checkout -b [新しいブランチ名]"),
        ("text", "（例：新機能を作るためのブランチ）\ngit checkout -b feature-new-button\n\n【今のブランチを確認するには？】"),
        ("code", "git branch"),
        ("text", "（* がついているのが、今自分がいる世界線です）")
    ]
    create_tab_content(tab_branch, branch_parts)

    # ----------------------------------------
    # タブ4: セーブ (Add / Commit)
    # ----------------------------------------
    tab_save = ttk.Frame(notebook)
    notebook.add(tab_save, text="3. セーブ (Add / Commit)")
    save_parts = [
        ("text", "ファイルを変更したら、その状態をセーブ（記録）します。\nGitのセーブは「準備」と「決定」の2ステップに分かれています。\n\n【STEP 1: 準備（Add）】\nセーブしたい変更を「カートに入れる」イメージです。"),
        ("code", "git add .\n# 「.」は全部の変更をカートに入れるという意味です"),
        ("text", "【STEP 2: 決定（Commit）】\nカートに入れた変更に「どんな変更をしたか」というメモをつけて確定します。"),
        ("code", 'git commit -m "ボタンの色を赤色に変更"'),
        ("text", "これであなたのパソコンの中に履歴（セーブデータ）が記録されました！")
    ]
    create_tab_content(tab_save, save_parts)

    # ----------------------------------------
    # タブ5: 共有 (Push / Pull)
    # ----------------------------------------
    tab_share = ttk.Frame(notebook)
    notebook.add(tab_share, text="4. 共有 (Push / Pull)")
    share_parts = [
        ("text", "【プッシュ（Push）】\nパソコンでセーブしたデータ（コミット）を、GitHub（クラウド）にアップロードします！\n他の人にあなたの作業を見てもらうために必要です。"),
        ("code", "git push origin [ブランチ名]"),
        ("text", "（例）\ngit push origin feature-new-button\n\n【プル（Pull）】\n逆に、GitHub上にある「最新のデータ」を自分のパソコンにダウンロード（更新）します。\n他の人が行った変更を取り込む時に使います。"),
        ("code", "git pull origin main"),
        ("text", "※「main」はメインの世界線の名前です。")
    ]
    create_tab_content(tab_share, share_parts)

    # ウィンドウを画面中央に表示するための処理
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    # アプリケーションの実行
    root.mainloop()

if __name__ == "__main__":
    create_git_explainer()
