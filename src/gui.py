import tkinter as tk

duration =10
def getDuration():
    root = tk.Tk()
    root.geometry('700x200')
    root.configure(bg="white")
    root.title("Welcome to blinkr")

    instructionText = tk.Text(root,height=2,width=100,bg="white",padx=20,bd=0)
    instructionText.tag_configure("center",justify="center")
    instructionText.insert(tk.INSERT,"Set the time interval to check for blinks (in seconds)")
    instructionText.config(state="disabled")
    entry1 = tk.Entry(root,width=40,bg="gray")
    instructionText.grid(row=0,column=0)
    entry1.grid(row=1,column=0)

    def getValueAndCLose():
        text = entry1.get()
        if text=="":
            global duration
        else:
            global duration
            duration = text
        root.destroy()

    btn = tk.Button(root,text="Proceed",command = getValueAndCLose,pady=4,bd=0)
    btn.grid(row = 2,column = 0)
    root.mainloop()
    return duration


