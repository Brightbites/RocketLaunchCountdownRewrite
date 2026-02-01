import tkinter as tk

root = tk.Tk()
root.title("RocketLaunchCountdown")

root.configure(bg="Black")
tk.Grid.rowconfigure(root,0,weight=1)
tk.Grid.columnconfigure(root,0,weight=1)

tk.Grid.rowconfigure(root,2,weight=1)

label = tk.Label(root, text="hewwo")
label.grid(row=0,column=0, columnspan=7, sticky="nsew")

var1 = tk.IntVar()

tk.Checkbutton(root, text="TimeTill", variable=var1, fg="White", bg="Black").grid(row=1,column=6, padx=5, sticky="nsew")
tk.Text(root, height = 1, width = 4, bg = "White").grid(row=1,column=0, padx=5, sticky="nsew")
tk.Text(root, height = 1, width = 4, bg = "White").grid(row=1,column=1, padx=5, sticky="nsew")
tk.Text(root, height = 1, width = 4, bg = "White").grid(row=1,column=2, padx=5, sticky="nsew")
tk.Text(root, height = 1, width = 4, bg = "White").grid(row=1,column=3, padx=5, sticky="nsew")
tk.Text(root, height = 1, width = 4, bg = "White").grid(row=1,column=4, padx=5, sticky="nsew")
tk.Text(root, height = 1, width = 4, bg = "White").grid(row=1,column=5, padx=5, sticky="nsew")

button = tk.Button(root, text="Exit", width=20, command=root.destroy)
button.grid(row=2,column=0, columnspan=7, sticky="nsew")

root.mainloop()
