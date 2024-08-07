import customtkinter as cutk
import Verification
import mysql.connector
import List

def Add_student(position, track):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='@Bdallh1722', port=3306, database='Trainingee')
    my_cursor = mydb.cursor()



    root_Add = cutk.CTk()
    root_Add.geometry('750x500')
    root_Add.minsize(650, 450)
    root_Add.maxsize(650, 450)
    root_Add.title('Add The Student')

    def back():
        root_Add.destroy()
        List.search_or_add(position, track)

    def add_data():
        
        my_cursor.execute(f'SELECT * FROM {track}')
        result = my_cursor.fetchall()
        var0 = 0
        for i in result:
            print(i)
            var0 = i[0]

        entry_1 = int(var0) + 1
        entry_2 = entry2.get()
        entry_3 = entry3.get()
        entry_4 = entry4.get()
        entry_5 = ''
        entry_6 = ''
        if entry_1 == '':
            Verification.Verification_add_id()
            return
        elif entry_2 == '':
            Verification.Verification_add_name()
            return
        elif entry_3 == '':
            Verification.Verification_wrong_data()
            return
        elif entry_4 == '':
            Verification.Verification_wrong_data()
            return
        else:
            sql = f'INSERT INTO {track} (id , name , degrees , additional_degrees , total , commintent) VALUES(%s , %s , %s , %s , %s , %s)'
            data = (entry_1, entry_2, entry_3, entry_4, entry_5, entry_6)
            my_cursor.execute(sql, data)
            mydb.commit()
            Verification.add_done()

    def Close(): 
        root_Add.destroy()


    frame = cutk.CTkFrame(root_Add)
    frame.pack(padx=5, pady=5, fill='both', expand=True)

    label = cutk.CTkLabel(frame, text='Add The Student', font=('𝔻𝕠𝕦𝕓𝕝𝕖-𝕊𝕥𝕣𝕦𝕔𝕜 𝕋𝕖𝕩𝕥', 24), text_color='white')
    label.pack(padx=10, pady=12)

    entry2 = cutk.CTkEntry(frame, placeholder_text='Student Name',  text_color='white',
                            placeholder_text_color='white', font=('Roboto', 15), height=30, width=250, border_color='white', border_width=2)
    entry2.pack(padx=10, pady=12)

    entry3 = cutk.CTkEntry(frame, placeholder_text='Degrees', text_color='black',
                            placeholder_text_color='white', font=('Roboto', 15), height=30, width=250, border_color='white', border_width=2)
    entry3.pack(padx=10, pady=12)

    entry4 = cutk.CTkEntry(frame, placeholder_text='Additional', text_color='white',
                            placeholder_text_color='white', font=('Roboto', 15), height=30, width=250, border_color='white', border_width=2)
    entry4.pack(padx=10, pady=12)

    button = cutk.CTkButton(frame, text='Add', hover_color='white', text_color='black', command=add_data, border_color='white', border_width=2)
    button.pack(pady=15)

    back = cutk.CTkButton(frame, text='Back', hover_color='white', text_color='black', command=back, border_color='white', border_width=2)
    back.pack(pady=15)

    Close = cutk.CTkButton(frame, text='Close', hover_color='white', text_color='black', command=Close, border_color='white', border_width=2) 
    Close.pack(pady=15)

    root_Add.mainloop()




