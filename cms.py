from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox



root = Tk()
root.title("Contact List")
width = 700
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#f0f0f0")

lbl_title = ttk.Label(root, text="Contact Management System")
lbl_title.config(font=('helvetica', 20))
lbl_title.pack()

#buttons
'''b = Button(root, text ="Hello")
b.pack(fill =BOTH, expand =1)'''

def addInfo():
   tkMessageBox.showinfo("Add Info", "")

B1 = ttk.Button(root, text ="Add Info", command = addInfo)
B1.pack(side =TOP)


def updateInfo():
   tkMessageBox.showinfo("Update Info", "")

B2 = ttk.Button( text ="Update Info", command = updateInfo)
B2.pack(side =TOP)

def deleteInfo():
    tkMessageBox.showinfo("Delete Info")

B3 = ttk.Button(text ="Delete Info", command = deleteInfo)
B3.pack(side =TOP)

lbl_table = ttk.Label(root, text="Contact List", font=('arial', 16))
lbl_table.pack()

lbl_fname = ttk.Label(root, text ="First name")
lbl_fname.pack(padx =1,pady =1, side =LEFT)

lbl_lname = ttk.Label(root, text ="Last name")
lbl_lname.pack(padx=2, pady=5, side=LEFT)

lbl_gender = ttk.Label(root, text ="Gender")
lbl_gender.pack(padx=1, pady=10, side=LEFT)

lbl_contact = ttk.Label(root, text ="Contact")
lbl_contact.pack(padx=1, pady=15, side=LEFT)

lbl_address =ttk.Label(root, text ="Address")
lbl_address.pack(padx=1, pady=20, side=LEFT)


#w.pack(padx=5, pady=10, side=tk.LEFT)

root.mainloop()