import customtkinter as cutk
import mysql.connector
from tkinter import *
from  tkinter import ttk


def search(name_or_id):


    mydb = mysql.connector.connect(host='localhost', user='root', passwd='@Bdallh1722', port=3306, database='Trainingee')
    my_cursor = mydb.cursor()


    root_search_in_tracks = cutk.CTk()
    root_search_in_tracks.geometry('750x500')
    # root_search_in_tracks.minsize(650, 450)
    # root_search_in_tracks.maxsize(650, 450)
    root_search_in_tracks.title('Add The Student')

    style = ttk.Style(root_search_in_tracks)
    style.theme_use('clam')
    style.configure('Treeview', background = '#cad2c5', fielbackground = 'blue', foreground = 'black')
    style.configure('Treeview.Heading', background = '#353535', fielbackground = 'gold', foreground = 'black', corner_radius=20)

    frame = cutk.CTkScrollableFrame(root_search_in_tracks)
    frame.pack(padx=5, pady=5, fill='both', expand=True)


    my_data = ttk.Treeview(frame, height=27)
    my_data.grid(column=0, row=1, columnspan=25, pady=10)


    my_data['columns'] = ('Track', 'ID', 'Name', 'Degrees', 'Additional_degrees', 'Total', 'Commintent')

    my_data.column("#0", width=0,  stretch=NO)
    my_data.column("Track", anchor=CENTER, width=200)
    my_data.column("ID", anchor=CENTER, width=40)
    my_data.column("Name", anchor=CENTER, width=150)
    my_data.column("Degrees", anchor=CENTER, width=80)
    my_data.column("Additional_degrees", anchor=CENTER, width=200)
    my_data.column("Total", anchor=CENTER, width=80)
    my_data.column("Commintent" ,anchor=CENTER, width=100)

    my_data.heading("#0",text="",anchor=CENTER)
    my_data.heading("Track", text="Track",anchor=CENTER)
    my_data.heading("ID", text="Id",anchor=CENTER)
    my_data.heading("Name", text="Name",anchor=CENTER)
    my_data.heading("Degrees", text="Degrees",anchor=CENTER)
    my_data.heading("Additional_degrees", text="Additional_degrees",anchor=CENTER)
    my_data.heading("Total", text="Total",anchor=CENTER)
    my_data.heading("Commintent", text="Commintent",anchor=CENTER)

    my_cursor.execute('SHOW TABLES') #to show all table
    result_track = my_cursor.fetchall()

    for i in result_track:
        if i != result_track[0]:
            sql = f'SELECT * FROM {i[0]} WHERE name LIKE %s OR id = %s'
            data_base = ('%' + name_or_id + '%', name_or_id)
            my_cursor.execute(sql, data_base)
            result = my_cursor.fetchone()
            add_track = [i[0]]
            if result is not None:
                for u in result:
                    add_track.append(u)
                my_data.insert(parent='', index='end',  text='', values=add_track)
            else:
                add_track.remove(i[0])
            
            
            

    root_search_in_tracks.mainloop()