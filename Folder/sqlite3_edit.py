import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3

# 데이터베이스 연결 혹은 생성
conn = sqlite3.connect('id.db')
c = conn.cursor()

# # users 테이블 생성
c.execute('''CREATE TABLE IF NOT EXISTS images
             (id INTEGER PRIMARY KEY, file_path TEXT UNIQUE, sort_order INTEGER)''')
conn.commit()


class DatabaseApp:
    def __init__(self, master):
        self.master = master
        master.title('SQLite3 DB Editor')

        self.listbox = tk.Listbox(master, width=50, height=15)
        self.listbox.pack()

        self.refresh_button = tk.Button(master, text="Refresh", command=self.refresh_listbox)
        self.refresh_button.pack()

        self.add_button = tk.Button(master, text="Add User", command=self.add_user)
        self.add_button.pack()

        self.delete_button = tk.Button(master, text="Delete User", command=self.delete_user)
        self.delete_button.pack()

        self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for row in c.execute('SELECT * FROM users'):
            self.listbox.insert(tk.END, row)

    def add_user(self):
        name = simpledialog.askstring("Input", "Enter user name:", parent=self.master)
        age = simpledialog.askinteger("Input", "Enter user age:", parent=self.master)
        age = simpledialog.askinteger("Input", "Enter user age:", parent=self.master)
        if name and age:
            c.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
            conn.commit()
            self.refresh_listbox()
        else:
            messagebox.showerror("Error", "Name and age are required.")

    def delete_user(self):
        try:
            index = self.listbox.curselection()[0]
            user_id = self.listbox.get(index)[0]
            c.execute('DELETE FROM users WHERE id=?', (user_id,))
            conn.commit()
            self.refresh_listbox()
        except IndexError:
            messagebox.showerror("Error", "Select a user to delete.")

root = tk.Tk()
app = DatabaseApp(root)
root.mainloop()
