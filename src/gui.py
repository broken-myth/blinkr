import tkinter as tk


duration = 10  # Default duration if the user provides no input


def getDuration():
    root = tk.Tk()
    root.geometry("700x200")  # Dimensions of the GUI window
    root.configure(
        bg="white"
    )  # Other attributes like background color of the window and so on
    root.title("Welcome to blinkr")  # Title of the window that is displayed at the top

    # The text to display
    instructionText = tk.Text(
        root, height=2, width=100, bg="white", padx=20, bd=0
    )  # The text object
    instructionText.insert(
        tk.INSERT, "Set the time interval to check for blinks (in seconds)"
    )  # Inserting the text content into the object created earlier

    # The textbox input
    entry1 = tk.Entry(root, width=40, bg="gray")

    # Positioning the text displayed and the textbox input
    instructionText.grid(row=0, column=0)
    entry1.grid(row=1, column=0)

    def getValueAndClose():
        text = entry1.get()
        if text == "":
            global duration
        else:
            global duration
            duration = text
        root.destroy()

    btn = tk.Button(root, text="Proceed", command=getValueAndClose, pady=4, bd=0)
    btn.grid(row=2, column=0)
    root.mainloop()
    return duration
