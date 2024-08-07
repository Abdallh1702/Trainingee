import customtkinter as cutk
import mysql.connector
import First_Page


def add_track(position):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='@Bdallh1722', port=3306, database='Trainingee')
    my_cursor = mydb.cursor()

    root_add_trak = cutk.CTk()
    root_add_trak.geometry('750x500')
    root_add_trak.minsize(250, 240)
    root_add_trak.maxsize(250, 240)
    root_add_trak.title('Add Users')


    def add_track_in_data_base():
        track_name = entry1.get()
        my_cursor.execute(f'CREATE TABLE {track_name} (id VARCHAR(100) , name VARCHAR(100), degrees VARCHAR(100) , additional_degrees VARCHAR(100),  total VARCHAR(100), commintent VARCHAR(100))')
        root_add_trak.destroy()
        First_Page.first_page(position)
        
    def back():
        root_add_trak.destroy()
        First_Page.first_page(position)


    frame = cutk.CTkFrame(root_add_trak)
    frame.pack(padx=5, pady=5, fill='both', expand=True)

    entry1 = cutk.CTkEntry(frame, placeholder_text='Track Name', text_color='black',
                            placeholder_text_color='black', font=('Roboto', 15), height=30, width=250, corner_radius=20)
    entry1.pack(padx=10, pady=12)



    add = cutk.CTkButton(frame, text='Add Track', hover_color='black', text_color='black', corner_radius=20, command=add_track_in_data_base) 
    add.pack(pady=15)

    back = cutk.CTkButton(frame, text='Back', hover_color='black', text_color='black', corner_radius=20, command=back) 
    back.pack(pady=15)




    root_add_trak.mainloop()



def delete_track_in_data_base(position):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='@Bdallh1722', port=3306, database='Trainingee')
    my_cursor = mydb.cursor()

    root_delete_track = cutk.CTk()
    root_delete_track.geometry('750x500')
    root_delete_track.minsize(250, 240)
    root_delete_track.maxsize(250, 240)
    root_delete_track.title('Add Users')


    frame = cutk.CTkFrame(root_delete_track)
    frame.pack(padx=5, pady=5, fill='both', expand=True)

    def delete_track():
        track_name = track_name_to_delete.get()
        my_cursor.execute(f'DROP TABLE {track_name}') 
        root_delete_track.destroy()
        First_Page.first_page(position)

    def back():
        root_delete_track.destroy()
        First_Page.first_page(position)       
       


    track_name_to_delete = cutk.CTkEntry(frame, placeholder_text='Track Name', text_color='black',
                            placeholder_text_color='black', font=('Roboto', 15), height=30, width=250, corner_radius=20)
    track_name_to_delete.pack(padx=10, pady=12)

    delete_track = cutk.CTkButton(frame, text='Delete Track', hover_color='black', text_color='black', corner_radius=20, command=delete_track) 
    delete_track.pack(pady=15)

    back = cutk.CTkButton(frame, text='Back', hover_color='black', text_color='black', corner_radius=20, command=back) 
    back.pack(pady=15)



    root_delete_track.mainloop()