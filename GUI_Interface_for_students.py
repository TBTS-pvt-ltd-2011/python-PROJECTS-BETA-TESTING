
# Initializing the GUI window
main = Tk()
main.title('Student Management System')
main.geometry('1000x800')
main.resizable(0, 0)

# Creating the background and foreground color variables
lf_bg = 'SteelBlue' # bg color for the left_frame

# Creating the StringVar or IntVar variables
name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
stream_strvar = StringVar()

# Placing the components in the main window
Label(main, text="STUDENT MANAGEMENT SYSTEM", font='Arial', bg='SkyBlue').pack(side=TOP, fill=X)
left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, height=1000, width=400)
right_frame = Frame(main, bg="gray")
right_frame.place(x=400, y=30, height=1000, width=600)


# Placing components in the left frame
Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(x=30, y=50)
Label(left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(x=30,y=100)
Label(left_frame, text="Email Address", font=labelfont, bg=lf_bg).place(x=30,y=150)
Label(left_frame, text="Gender", font=labelfont, bg=lf_bg).place(x=30, y=200)
Label(left_frame, text="Date of Birth (DOB)", font=labelfont, bg=lf_bg).place(x=30, y=250)
Label(left_frame, text="Stream", font=labelfont, bg=lf_bg).place(x=30, y=300)
Entry(left_frame, width=20, textvariable=name_strvar, font=entryfont).place(x=170, y=50)
Entry(left_frame, width=19, textvariable=contact_strvar, font=entryfont).place(x=170, y=100)
Entry(left_frame, width=19, textvariable=email_strvar, font=entryfont).place(x=170,y=150)
Entry(left_frame, width=19, textvariable=stream_strvar, font=entryfont).place(x=170, y=300)
OptionMenu(left_frame, gender_strvar, 'Male', "Female").place(x=170, y=200, width=70)
dob = DateEntry(left_frame, font=("Arial", 12), width=15)
dob.place(x=180, y=250)
Button(left_frame, text='Submit and Add Record', font=labelfont, command=add_record, width=18).place(x=80, y=380)

#Place the buttons in the left frame

Button(left_frame, text='Delete Record', font=labelfont, command=remove_record, width=15).place(x=30, y=450)
Button(left_frame, text='View Record', font=labelfont, command=view_record, width=15).place(x=200, y=450)
Button(left_frame, text='Clear Fields', font=labelfont, command=reset_fields, width=15).place(x=30, y=520)
Button(left_frame, text='Remove database', font=labelfont, command=reset_form, width=15).place(x=200, y=520)
# Placing components in the right frame

Label(right_frame, text='Students Records', font='Arial', bg='DarkBlue', fg='LightCyan').pack(side=TOP, fill=X)
tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                   columns=('Stud ID', "Name", "Email Addr", "Contact No", "Gender", "Date of Birth", "Stream"))
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)

tree.heading('Stud ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Email Addr', text='Email ID', anchor=CENTER)
tree.heading('Contact No', text='Phone No', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('Stream', text='Stream', anchor=CENTER)
tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=120, stretch=NO)
tree.column('#3', width=180, stretch=NO)
tree.column('#4', width=60, stretch=NO)
tree.column('#5', width=60, stretch=NO)
tree.column('#6', width=70, stretch=NO)
tree.column('#7', width=120, stretch=NO)
tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_records()


main.update()
main.mainloop()
