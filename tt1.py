import tkinter as tk
import tkinter.ttk as ttk


class ClipboardHistoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clipboard History")

        self.clipboard_history = []

        # Create a Listbox to display clipboard history
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        # Create a Paste button to paste the selected item
        paste_button = ttk.Button(root, text="Paste", command=self.paste_selected)
        paste_button.pack(pady=5)

        # Create a Clear button to clear the clipboard history
        clear_button = ttk.Button(root, text="Clear History", command=self.clear_history)
        clear_button.pack(pady=5)

        # Update the clipboard history when the application starts
        self.update_history()

        # Monitor clipboard changes
        self.root.after(1000, self.monitor_clipboard)

    def update_history(self):
        # Clear the Listbox
        self.listbox.delete(0, tk.END)

        # Add items from the clipboard history to the Listbox
        for item in reversed(self.clipboard_history):
            self.listbox.insert(0, item)

    def clear_history(self):
        # Clear the clipboard history
        self.clipboard_history = []
        self.update_history()

    def paste_selected(self):
        # Get the selected item from the Listbox
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_item = self.clipboard_history[selected_index[0]]

            # Put the selected item back into the clipboard
            self.root.clipboard_clear()
            self.root.clipboard_append(selected_item)
            self.root.update()

    def monitor_clipboard(self):
        # Get the current clipboard content
        current_clipboard = self.root.clipboard_get()

        # Check if the clipboard content is different from the last item in history
        if current_clipboard and (not self.clipboard_history or current_clipboard != self.clipboard_history[0]):
            # Add the current clipboard content to the history
            self.clipboard_history.insert(0, current_clipboard)

            # Limit the clipboard history to a certain number of items (e.g., 10)
            self.clipboard_history = self.clipboard_history[:10]

            # Update the Listbox
            self.update_history()

        # Schedule the next check after 1000 milliseconds (1 second)
        self.root.after(1000, self.monitor_clipboard)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClipboardHistoryApp(root)
    root.mainloop()
