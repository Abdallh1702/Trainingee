from tkinter import *
from  tkinter import ttk
import mysql.connector
import customtkinter as cutk
import Add_users

def show_users(position):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='@Bdallh1722', port=3306, database='Trainingee')                        
    my_cursor = mydb.cursor()


    root_all_users = cutk.CTk()  
    root_all_users.title('All Data')
    root_all_users.geometry('1050x670')

    def call_delete_user():
        Add_users.delete_user(position)

    style = ttk.Style(root_all_users)
    style.theme_use('clam')
    style.configure('Treeview', background = '#cad2c5', fielbackground = 'blue', foreground = 'black')
    style.configure('Treeview.Heading', background = '#353535', fielbackground = 'gold', foreground = 'black', corner_radius=20)

    frame = cutk.CTkScrollableFrame(root_all_users)
    frame.pack(padx=5, pady=5, fill='both', expand=True)


    def back_settigs():
        import Settings
        root_all_users.destroy()
        Settings.settings_call(position)


    back_to_settings = cutk.CTkButton(frame, text='Back', hover_color='white', text_color='black', 
                        command=back_settigs, corner_radius=20, width=5)
    back_to_settings.grid(row=0, column=23, pady=5)

    delete_user = cutk.CTkButton(frame, text='Delete User', hover_color='white', text_color='black', 
                        command=call_delete_user, corner_radius=20, width=2)
    delete_user.grid(row=0, column=24, pady=5)

    my_data = ttk.Treeview(frame, height=27)
    my_data.grid(column=0, row=1, columnspan=25, pady=10)


    my_data['columns'] = ('User_name', 'Password', 'Position')

    my_data.column("#0", width=0,  stretch=NO)
    my_data.column("User_name", anchor=CENTER, width=400)
    my_data.column("Password", anchor=CENTER, width=400)
    my_data.column("Position", anchor=CENTER, width=400)


    my_data.heading("#0",text="",anchor=CENTER)
    my_data.heading("User_name", text="UserName",anchor=CENTER)
    my_data.heading("Password", text="Password",anchor=CENTER)
    my_data.heading("Position", text="Position",anchor=CENTER)


    my_cursor.execute('SELECT * FROM data_users_login')
    result = my_cursor.fetchall()
    for i in result:
        my_data.insert(parent='', index='end',  text='', values=i)

    
    root_all_users.mainloop()

