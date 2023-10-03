import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("Pacemaker v0 0.1.0")

home_label = tk.Label(root, text="Pacemaker Home Screen", font=('Arial',18))
home_label.pack(padx=20, pady=20)

textbox = tk.Text(root, height = 3, font = ("Arial", 16))
textbox.pack()

myEntry = tk.Entry(root)
myEntry.pack(padx=10,pady=20)

button = tk.Button(root, text='Click me!', font=('Arial', 10))
button.pack(padx=10,pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='Option 1', font=('Arial', 18))
btn1.grid(row=0,column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonframe, text='Option 2', font=('Arial', 18))
btn2.grid(row=0,column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonframe, text='Option 3', font=('Arial', 18))
btn3.grid(row=0,column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(buttonframe, text='Option 4', font=('Arial', 18))
btn4.grid(row=1,column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(buttonframe, text='Option 5', font=('Arial', 18))
btn5.grid(row=1,column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(buttonframe, text='Option 6', font=('Arial', 18))
btn6.grid(row=1,column=2, sticky=tk.W + tk.E)

buttonframe.pack(fill='x')
root.mainloop()