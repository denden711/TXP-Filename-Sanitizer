import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

def process_files():
    folder = folder_path.get()
    if not folder:
        messagebox.showerror("エラー", "フォルダを選択してください")
        return

    if not os.path.exists(folder):
        messagebox.showerror("エラー", "指定されたフォルダが存在しません")
        return

    try:
        for filename in os.listdir(folder):
            if filename.endswith(".txp") and 's' in filename:
                new_filename = filename.replace('s', '')
                old_file = os.path.join(folder, filename)
                new_file = os.path.join(folder, new_filename)

                # 新しいファイル名がすでに存在する場合のハンドリング
                if os.path.exists(new_file):
                    messagebox.showwarning("警告", f"ファイル名 {new_filename} はすでに存在しています")
                    continue

                os.rename(old_file, new_file)
        
        messagebox.showinfo("完了", "ファイル名の変更が完了しました")
    except Exception as e:
        messagebox.showerror("エラー", f"ファイルの処理中にエラーが発生しました: {e}")

# GUIの設定
root = tk.Tk()
root.title("ファイル名から's'を削除")

folder_path = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="フォルダを選択:").grid(row=0, column=0, pady=5)
tk.Entry(frame, textvariable=folder_path, width=50).grid(row=0, column=1, pady=5)
tk.Button(frame, text="参照", command=select_folder).grid(row=0, column=2, pady=5)

tk.Button(frame, text="実行", command=process_files).grid(row=1, columnspan=3, pady=10)

root.mainloop()
