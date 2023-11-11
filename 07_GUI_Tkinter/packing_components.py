import tkinter as tk


root = tk.Tk()

# tk.Label(root, text="Label 1", bg="green").pack(side="left", fill="y")
# tk.Label(root, text="Label 2", bg="red").pack(side="top", fill="x")

tk.Label(root, text="Label left", bg="green").pack(
    side="left", expand=True, fill="both"
)
tk.Label(root, text="Label 1: top", bg="red").pack(side="top", fill="both", expand=True)
tk.Label(root, text="Label 2: top", bg="red").pack(side="top", fill="both", expand=True)
tk.Label(root, text="Label left", bg="green").pack(
    side="left", expand=True, fill="both"
)
tk.Label(root, text="Label left", bg="green").pack(
    side="left", expand=True, fill="both"
)

root.mainloop()