import customtkinter as cutk



def Verification_name_found():
    root_name_found = cutk.CTk()
    root_name_found.geometry('750x500')
    root_name_found.minsize(250, 150)
    root_name_found.maxsize(250, 150)
    root_name_found.title('Error')

    def Close(event): 
        root_name_found.destroy() 

    frame = cutk.CTkFrame(root_name_found)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    label_text = cutk.CTkLabel(frame, font=('Roboto', 16), text='Username dosenot match', text_color='red')
    label_text.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)

    root_name_found.bind('<Return>', Close)

    root_name_found.mainloop()

def Verification_name():
    root_name = cutk.CTk()
    root_name.geometry('750x500')
    root_name.minsize(250, 150)
    root_name.maxsize(250, 150)
    root_name.title('Error')


    def Close(event): 
        root_name.destroy()

    frame = cutk.CTkFrame(root_name)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    label_text = cutk.CTkLabel(frame, font=('Roboto', 16), text='Please Enter Your Username', text_color='red')
    label_text.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)

    root_name.bind('<Return>', Close)

    root_name.mainloop()


def Verification_password():
    root_password = cutk.CTk()
    root_password.geometry('750x500')
    root_password.minsize(250, 150)
    root_password.maxsize(250, 150)
    root_password.title('Error')


    def Close(event): 
        root_password.destroy()

    frame = cutk.CTkFrame(root_password)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    label_text = cutk.CTkLabel(frame, font=('Roboto', 16), text='Please Enter Your Password', text_color='red')
    label_text.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)

    root_password.bind('<Return>', Close)

    root_password.mainloop()


def Password_Low():

    root_Password_Low = cutk.CTk()
    root_Password_Low.geometry('750x500')
    root_Password_Low.minsize(350, 150)
    root_Password_Low.maxsize(350, 150)
    root_Password_Low.title('Error')

    frame = cutk.CTkFrame(root_Password_Low)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    def Close(event): 
        root_Password_Low.destroy()

    password_low = cutk.CTkLabel(frame, font=('Roboto', 17), text='Low Password', text_color='red')
    password_low.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)
    
    root_Password_Low.bind('<Return>', Close)

    root_Password_Low.mainloop()



def add_Position():
    
    root_add_Position = cutk.CTk()
    root_add_Position.geometry('750x500')
    root_add_Position.minsize(450, 120)
    root_add_Position.maxsize(450, 120)
    root_add_Position.title('Error')

    frame = cutk.CTkFrame(root_add_Position)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    def Close(event): 
        root_add_Position.destroy()

    error_position = cutk.CTkLabel(frame, font=('Roboto', 17), text='Please Select Position', text_color='red')
    error_position.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)
    
    root_add_Position.bind('<Return>', Close)

    root_add_Position.mainloop()

def add_user_done():
    
    root_add_user_done = cutk.CTk()
    root_add_user_done.geometry('750x500')
    # root_add_user_done.minsize(250, 150)
    # root_add_user_done.maxsiz(250, 150)
    root_add_user_done.title('Error')

    frame = cutk.CTkFrame(root_add_user_done)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    def Close(event): 
        root_add_user_done.destroy()

    error_position = cutk.CTkLabel(frame, font=('Roboto', 17), text='Done', text_color='green')
    error_position.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)
    
    root_add_user_done.bind('<Return>', Close)

    root_add_user_done.mainloop()



def Verification_wrong_password():
    root_wrong_password = cutk.CTk()
    root_wrong_password.geometry('750x500')
    root_wrong_password.minsize(250, 150)
    root_wrong_password.maxsize(250, 150)
    root_wrong_password.title('Error')


    def Close(event): 
        root_wrong_password.destroy()


    frame = cutk.CTkFrame(root_wrong_password)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    label_text = cutk.CTkLabel(frame, font=('Roboto', 12), text='incorrect password',
                                               text_color='red')
    label_text.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)

    root_wrong_password.bind('<Return>', Close)

    root_wrong_password.mainloop()


def Verification_name_used():
    root_name_used = cutk.CTk()
    root_name_used.geometry('750x500')
    root_name_used.minsize(250, 150)
    root_name_used.maxsize(250, 150)
    root_name_used.title('Error')


    def Close(event): 
        root_name_used.destroy()


    frame = cutk.CTkFrame(root_name_used)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    label_text = cutk.CTkLabel(frame, font=('Roboto', 12), text='Username is Already Token', text_color='red')
    label_text.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)

    root_name_used.bind('<Return>', Close)

    root_name_used.mainloop()


def Verification_wrong_data():
    root_wrong_data = cutk.CTk()
    root_wrong_data.geometry('750x500')
    root_wrong_data.minsize(300, 150)
    root_wrong_data.maxsize(300, 150)
    root_wrong_data.title('Error')


    def Close(): 
        root_wrong_data.destroy()

    frame = cutk.CTkFrame(root_wrong_data)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    label_text = cutk.CTkLabel(frame, font=('Roboto', 16), text='Incorrect Data. Please Enter Valid Data',
                                               text_color='red')
    label_text.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)

    root_wrong_data.mainloop()


# def Verification_add_id():
#     root_add_id = cutk.CTk()
#     root_add_id.geometry('750x500')
#     root_add_id.minsize(250, 150)
#     root_add_id.maxsize(250, 150)
#     root_add_id.title('Error')


#     def Close(): 
#         root_add_id.destroy()

#     frame = cutk.CTkFrame(root_add_id)
#     frame.pack(padx=1, pady=1, fill='both', expand=True)

#     label_text = cutk.CTkLabel(frame, font=('Roboto', 16), text='Please Enter Your Student ID',
#                                                text_color='red')
#     label_text.pack()

#     button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
#     button.pack(pady=15)

#     root_add_id.mainloop()



def Verification_add_name():
    root_add_name = cutk.CTk()
    root_add_name.geometry('750x500')
    root_add_name.minsize(250, 150)
    root_add_name.maxsize(250, 150)
    root_add_name.title('Error')


    def Close(): 
        root_add_name.destroy()

    frame = cutk.CTkFrame(root_add_name)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    label_text = cutk.CTkLabel(frame, font=('Roboto', 16), text='Please Enter Your Student Name',
                                               text_color='red')
    label_text.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)

    root_add_name.mainloop()


def Verification_search_id():
    root_Verification_search_id = cutk.CTk()
    root_Verification_search_id.geometry('750x500')
    root_Verification_search_id.minsize(250, 150)
    root_Verification_search_id.maxsize(250, 150)
    root_Verification_search_id.title('Error')


    def Close(): 
        root_Verification_search_id.destroy()

    frame = cutk.CTkFrame(root_Verification_search_id)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    label_text = cutk.CTkLabel(frame, font=('Roboto', 16), text='ID dose Not Match',
                                               text_color='red')
    label_text.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)

    root_Verification_search_id.mainloop()


def Verification_search_name():
    root_Verification_search_name = cutk.CTk()
    root_Verification_search_name.geometry('750x500')
    root_Verification_search_name.minsize(250, 150)
    root_Verification_search_name.maxsize(250, 150)
    root_Verification_search_name.title('Error')


    def Close(): 
        root_Verification_search_name.destroy()

    frame = cutk.CTkFrame(root_Verification_search_name)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    label_text = cutk.CTkLabel(frame, font=('Roboto', 16), text='Name Is Not Found',
                                               text_color='red')
    label_text.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)

    root_Verification_search_name.mainloop()


def add_done():
    root_add_done = cutk.CTk()
    root_add_done.geometry('750x500')
    root_add_done.minsize(250, 150)
    root_add_done.maxsize(250, 150)
    root_add_done.title('Error')


    def Close(): 
        root_add_done.destroy()

    frame = cutk.CTkFrame(root_add_done)
    frame.pack(padx=1, pady=1, fill='both', expand=True)

    label_text = cutk.CTkLabel(frame, font=('Roboto', 16), text='Data Save',
                                               text_color='green')
    label_text.pack()

    button = cutk.CTkButton(frame, text='OK', hover_color='black', text_color='black', command=Close)
    button.pack(pady=15)

    root_add_done.mainloop()


