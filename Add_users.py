import customtkinter as cutk
import mysql.connector
import Verification
import Settings

check_pos = '_select_'


def add_users_call():
    global check
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='@Bdallh1722', port=3306, database='Trainingee')
    my_cursor = mydb.cursor()
    
    root_add_users = cutk.CTk()
    root_add_users.geometry('750x500')
    root_add_users.minsize(400, 280)
    root_add_users.maxsize(400, 280)
    root_add_users.title('Add Users')

    frame = cutk.CTkFrame(root_add_users)
    frame.pack(padx=5, pady=5, fill='both', expand=True)

    
    def add():

        User_Name = entry1.get().lower()
        Password = entry2.get()
        Position = check_pos
        
        if User_Name == '':
            Verification.Verification_name()
            return
        
        elif Password == '':
            Verification.Verification_password()
            return
        
        elif Position == '_select_':
            Verification.add_Position()
            return
        
        elif len(Password) < 8:
            Verification.Password_Low()
            return
        
        else:
            sql = 'SELECT * FROM data_users_login WHERE user_name = %s '
            data = (User_Name, )
            my_cursor.execute(sql, data)
            result = my_cursor.fetchone()
            if result is not None:
                Verification.Verification_name_used()
                return
            else:
                sql = 'INSERT INTO data_users_login (user_name , password , position) VALUES(%s , %s, %s)'
                data = (User_Name, Password, Position)
                my_cursor.execute(sql, data)
                mydb.commit()
                Verification.add_user_done()

    entry1 = cutk.CTkEntry(frame, placeholder_text='User Name', text_color='black',
                            placeholder_text_color='black', font=('Roboto', 15), height=30, width=250, corner_radius=20)
    entry1.pack(padx=10, pady=12)

    entry2 = cutk.CTkEntry(frame, placeholder_text='Password', show='*', text_color='black',
                            placeholder_text_color='black', font=('Roboto', 15), height=30, width=250, corner_radius=20)
    entry2.pack(padx=10, pady=12)



    def checkbox(values):
        global check_pos
        check_pos = values


    checkbox_manager = cutk.CTkOptionMenu(frame, values=[ '_select_' , 'user' , 'editor' , 'manager'] , command=checkbox)
    checkbox_manager.pack(pady=5)


    Close = cutk.CTkButton(frame, text='Create', hover_color='black', text_color='black', command=add, corner_radius=20) 
    Close.pack(pady=15)

    root_add_users.mainloop()

def delete_user(position):

    mydb = mysql.connector.connect(host='localhost', user='root', passwd='@Bdallh1722', port=3306, database='Trainingee')
    my_cursor = mydb.cursor()

    root_delete_user = cutk.CTk()
    root_delete_user.geometry('750x500')
    root_delete_user.minsize(400, 280)
    root_delete_user.maxsize(400, 280)
    root_delete_user.title('Delete Users')

    def delete_user_in_data_base():
        user_name = entry1.get().lower()
        sql = 'DELETE FROM data_users_login WHERE User_name = %s'
        data_base = (user_name,)
        my_cursor.execute(sql, data_base)
        mydb.commit()
        Verification.add_done()


    def back():
        root_delete_user.destroy()
        Settings.settings_call(position)

    frame = cutk.CTkFrame(root_delete_user)
    frame.pack(padx=5, pady=5, fill='both', expand=True)
    
    entry1 = cutk.CTkEntry(frame, placeholder_text='User Name', text_color='black',
                            placeholder_text_color='black', font=('Roboto', 15), height=30, width=250, corner_radius=20)
    entry1.pack(padx=10, pady=12)


    Delete_user = cutk.CTkButton(frame, text='Delete', hover_color='white', text_color='black', corner_radius=20, command=delete_user_in_data_base) 
    Delete_user.pack(pady=15)

    back = cutk.CTkButton(frame, text='Back', hover_color='white', text_color='black', corner_radius=20, command=back) 
    back.pack(pady=15)
    

    root_delete_user.mainloop()


