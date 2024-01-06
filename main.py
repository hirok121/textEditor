import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

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
    # window.geometry("500x500")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(0, minsize=400)
    #create text editor
    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=0)

    #create scrollbar
    scrollbar = tk.Scrollbar(window, command=text_edit.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    #set scrollbar to text editor
    text_edit.config(yscrollcommand=scrollbar.set)

    #create frame
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)

    #create buttons
    #create save button
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    #create open button
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))
    #clear button
    clear_button = tk.Button(frame, text="Clear", command=lambda: clear_text(window, text_edit))
    #set save button position
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    #set open button position
    open_button.grid(row=0, column=1, padx=5, sticky="ew")
    #set clear button position
    clear_button.grid(row=0, column=2, padx=5, sticky="ew")
    #set frame position
    frame.grid(row=1, column=0, sticky="ns")

    #shortcut keys
    window.bind('<Control-o>', lambda event: open_file(window, text_edit))
    window.bind('<Control-s>', lambda event: save_file(window, text_edit))
    window.bind('<Control-x>', lambda event: clear_text(window, text_edit))

    #run window
    window.mainloop()


# def main():
# window = tk.Tk()
# window. title( "Text Editor")
# window. rowconfigure(0, minsize=4Ø0)
# window. columnconfigure(l, minsize—5ØØ)
# text_edit : tk. Text(window, font: "Helvetica 18")
# text_edit. grid (row=e, column—I)
# frame - tk.Frame(window, relief-tk.RAISED, bd:2)
# save_button tk.Button(
# text_edit) )
# frame, textz"Save"
# command-lambda: save_file(window,
# open_button : tk.Button(
# frame, text: "Open" ,
# command-lambda:
# text_edit) )
# save_button .grid(row-ø, column-Ø, padx=5, eggy-5, sticky-"ew" )
# open_button. column=Ø, padx=5,
# frame. gridl(row-ø, columnzø, sticky: "ns'
# window. mainloop()

if __name__ == "__main__":
    main()
