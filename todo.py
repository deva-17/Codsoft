from tkinter import *
root=Tk()



box=Listbox(root, width=50, height=15, font=("helvicta", 10))
box.grid(row=2, column=0, columnspan=4, padx=35, pady=10)

entry=Entry(root, width=30, font=("helvicta", 10))
entry.grid(row=1, column=0)




def addtask():
    task = entry.get()
    if task:
        box.insert(END, task)
    entry.delete(0, END)
    

def deletetask():
    try: 
        task = box.curselection()[0] 
        box.delete(task) 
    except IndexError: 
        pass 


 #markasdone function       
def markdone():
    try:
        task_index = box.curselection()[0]
        task = box.get(task_index)
        marked_task = task + "                             ● DONE!!!" 
        box.delete(task_index)  
        box.insert(task_index, marked_task)  
        box.itemconfig(task_index, {'bg': 'light green'})  
      
    except IndexError:
        pass




#buttons
button_add=Button(root, text="ADD_TASK", padx=3, pady=5, command= addtask,bg="green",fg="white")
button_add.grid(row=1, column=1, columnspan=1)

button_del=Button(root, text="DELETE_TASK", padx=3, pady=5, command=deletetask, bg="red",fg="white")
button_del.grid(row=1, column=2)

button_done=Button(root, text="MARK AS DONE", padx=10, pady=10, command= markdone, bg="orange",fg="white")
button_done.grid(row=3, column=2)

root.mainloop()