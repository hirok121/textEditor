import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def main():
    window = tk.Tk()
    window.geometry("800x600")  # Set window size
    # window.pack_slaves()  # Set window size

    frame = tk.Frame(window)
    frame.pack(fill=tk.BOTH, expand=True)  # Set frame size

    text_edit = tk.Text(frame)
    text_edit.pack(fill=tk.BOTH, expand=True)  # Let the text editor occupy the rest of the window
    # add a vertical scroll bar to the text editor
    scrollbar = tk.Scrollbar(text_edit, command=text_edit.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_edit.config(yscrollcommand=scrollbar.set)
    # scrollbar.config(command=text_edit.yview)


    window.mainloop() 

def open_file (window, text_edit) :
    filepath = askopenfilename(initialdir=os.getcwd() ,filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],defaultextension="txt")
    if not filepath :
        return
    text_edit.delete(1.0, tk. END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
        window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(initialdir=os.getcwd(), defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
        window.title(f"Save as {filepath}")

def clear_text(window,text_edit):
    text_edit.delete(1.0, tk.END)
    window.title(f"Text Editor")

def main():
    window = tk.Tk()
    #set title to Text Editor
    window.title("Text Editor")
    #set size of window
    # window.geometry("800x600")

    #create text editor frame
    text_frame = tk.Frame(window)
    text_frame.pack(fill=tk.BOTH, expand=True)  # Set frame size

    #create text editor
    text_edit = tk.Text(text_frame, font="Helvetica 18")
    text_edit.pack(side="left",fill=tk.BOTH ,expand=True)  # Let the text editor occupy the rest of the window

    #create scrollbar
    scrollbar = tk.Scrollbar(text_frame, command=text_edit.yview)
    scrollbar.pack(side=tk.LEFT, fill=tk.Y)
    #set scrollbar to text editor
    text_edit.config(yscrollcommand=scrollbar.set)

    #create buttons frame
    bframe = tk.Frame(window, relief=tk.RAISED, bd=2)

    #create buttons
    #create save button
    save_button = tk.Button(bframe, text="Save", command=lambda: save_file(window, text_edit))
    #create open button
    open_button = tk.Button(bframe, text="Open", command=lambda: open_file(window, text_edit))
    #clear button
    clear_button = tk.Button(bframe, text="Clear", command=lambda: clear_text(window, text_edit))
    #set save button position
    save_button.pack(side="right", padx=5, pady=5)
    #set open button position
    open_button.pack(side="right", padx=5)
    #set clear button position
    clear_button.pack(side="right", padx=5)
    #set frame position
    bframe.pack(fill=tk.X)

    #shortcut keys
    window.bind('<Control-o>', lambda event: open_file(window, text_edit))
    window.bind('<Control-s>', lambda event: save_file(window, text_edit))
    window.bind('<Control-x>', lambda event: clear_text(window, text_edit))

    #run window
    window.mainloop()


if __name__ == "__main__":
    main()

