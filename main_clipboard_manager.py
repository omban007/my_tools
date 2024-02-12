import tkinter as tk
import pyperclip
from tkinter import ttk


class ClipboardHistoryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Clipboard History")
        self.clipboard_list = []

        self.style = ttk.Style()
        self.style.configure("TListbox", font=("Helvetica", 12), background="#f0f0f0")

        self.listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, height=10)
        self.listbox.pack(pady=20)

        self.listbox.bind("<ButtonRelease-1>", self.copy_selected)

        # Bind events for hiding and showing the window
        self.master.bind("<Enter>", self.show_window)
        self.master.bind("<Leave>", self.hide_window)

        self.update_clipboard_list()
        self.master.after(1000, self.check_clipboard)

    def update_clipboard_list(self):
        clipboard_data = pyperclip.paste()
        if clipboard_data and clipboard_data not in self.clipboard_list:
            self.clipboard_list.insert(0, clipboard_data)
            self.listbox.delete(0, tk.END)
            for item in self.clipboard_list:
                self.listbox.insert(tk.END, item)
        self.master.after(1000, self.update_clipboard_list)

    def check_clipboard(self):
        current_clipboard = pyperclip.paste()
        if current_clipboard != self.clipboard_list[0]:
            self.clipboard_list.insert(0, current_clipboard)
            self.listbox.insert(0, current_clipboard)
        self.master.after(1000, self.check_clipboard)

    def copy_selected(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_text = self.listbox.get(selected_index)
            pyperclip.copy(selected_text)

    def show_window(self, event):
        root.attributes("-alpha", 1)
        # self.master.deiconify()  # Unhide the window

    def hide_window(self, event):
        root.attributes("-alpha", 0.2)
        # self.master.withdraw()  # Hide the window


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.geometry("100x200+1410+300")
    root.attributes("-alpha", 0.1)
    # root.resizable(False, False)
    # root.overrideredirect(True) # TODO enable this once all coding done
    app = ClipboardHistoryApp(root)
    root.mainloop()
