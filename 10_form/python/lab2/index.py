import tkinter as tk

root = tk.Tk()
root.title('Петухон — топ')
root.geometry('1500x600')

l1 = tk.Label(root, font='15',bg='light blue',width=15,height=1)
l1.grid(row=0,column=0)

l2 = tk.Label(root, font='20',bg='red',width=30,height=1)
l2.grid(row=0,column=2,columnspan=2)

l3 = tk.Label(root, font='20',bg='green',width=15,height=4)
l3.grid(row=2,rowspan=4,column=0)

l4 = tk.Label(root, font='20',bg='purple',width=30,height=1)
l4.grid(row=4,column=1,columnspan=2)

l5 = tk.Label(root, font='20',bg='black',width=15,height=1)
l5.grid(row=3,column=3)

l6 = tk.Label(root, font='20',bg='pink',width=30,height=1)
l6.grid(row=2,column=4,columnspan=2)

l7 = tk.Label(root, font='20',bg='yellow',width=15,height=3)
l7.grid(row=1,column=6,rowspan=3)

l8 = tk.Label(root, font='20',bg='grey',width=15,height=1)
l8.grid(row=4,column=5)

l9 = tk.Label(root, font='20',bg='orange',width=15,height=2)
l9.grid(row=5,column=4,rowspan=2)

l10 = tk.Label(root, font='20',bg='light green',width=15,height=1)
l10.grid(row=6,column=6)

root.mainloop()