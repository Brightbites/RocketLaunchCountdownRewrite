import tkinter as tk

root = tk.Tk()
root.title("RocketLaunchCountdown")

root.configure(bg="Black")
tk.Grid.rowconfigure(root,(1),weight=1, uniform="a")
tk.Grid.columnconfigure(root,(0,1,2,3,4,5,6),weight=1, uniform="a")
tk.Grid.rowconfigure(root,(0,2,3), weight=2, uniform="a")


Tminus = tk.Label(root, text="t-").grid(row=0, column=0, sticky="new")
label = tk.Label(root, text="00:00:00").grid(row=0,column=1, columnspan=6, sticky="new")

var1 = tk.IntVar()

tk.Checkbutton(root, text="TimeTill", variable=var1, fg="White", bg="Black").grid(row=1,column=6, padx=5, sticky="ew")
tk.Text(root, height = 1, width = 4, bg = "White").grid(row=1,column=0, padx=5, sticky="ew")
tk.Text(root, height = 1, width = 4, bg = "White").grid(row=1,column=1, padx=5, sticky="ew")
tk.Text(root, height = 1, width = 4, bg = "White").grid(row=1,column=2, padx=5, sticky="ew")
tk.Text(root, height = 1, width = 4, bg = "White").grid(row=1,column=3, padx=5, sticky="ew")
tk.Text(root, height = 1, width = 4, bg = "White").grid(row=1,column=4, padx=5, sticky="ew")
tk.Text(root, height = 1, width = 4, bg = "White").grid(row=1,column=5, padx=5, sticky="ew")

controlbar = tk.Frame(root)
controlbar.grid(row=2, column=0, columnspan=7)
Start = tk.Button(controlbar, text="Exit", width=10).grid(row=0, column=0, sticky="nsew")
Hold = tk.Button(controlbar, text="Exit", width=10).grid(row=0, column=1, sticky="nsew")
Stop = tk.Button(controlbar, text="Exit", width=10).grid(row=0, column=2, sticky="nsew")

button = tk.Button(root, text="Exit", width=10, command=root.destroy).grid(row=3,column=2, columnspan=3, sticky="sew")

label = tk.Label(root, text="Made by: HampsterSpaceNerd3000, Rewriten by: Brightbites").grid(row=4,column=0, columnspan=7, sticky="sew")

root.mainloop()
