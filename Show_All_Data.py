import tkinter as tk
from  tkinter import ttk
import mysql.connector
import customtkinter as cutk
import Show_Data
import Verification
import Add_Student
import List


def show_all_data(position, track):

    mydb = mysql.connector.connect(host='localhost', user='root', passwd='@Bdallh1722', port=3306, database='Trainingee')                        
    my_cursor = mydb.cursor()


    root_all_data = cutk.CTk()  
    root_all_data.title('All Data')
    root_all_data.geometry('1050x670')
    cutk.set_appearance_mode('dark')
    cutk.set_default_color_theme('green')

    root_all_data.rowconfigure(0, weight=1)
    root_all_data.columnconfigure(0, weight=1)
    style = ttk.Style(root_all_data)
    style.theme_use('clam')
    style.configure('Treeview', background = '#cad2c5', fielbackground = 'blue', foreground = 'black')
    style.configure('Treeview.Heading', background = '#353535', fielbackground = 'gold', foreground = 'black', corner_radius=20)




    def Add_student_call():
        Add_Student.Add_student(position, track)
 
    columns = ['ID', 'Name', 'Degrees', 'Additional_degrees', 'Total', 'Commintent']
    my_data = ttk.Treeview(root_all_data, height=27, columns=columns, show='headings')
    

    def back(): 
        root_all_data.destroy()
        List.search_or_add(position, track)


    def refrash():
        root_all_data.destroy()
        show_all_data(position, track)


    def call_search():
        name_or_id = search_Entry.get()
        search(name_or_id)


    def search(get_search_Entry):
        
        sql = f'SELECT * FROM {track} WHERE name LIKE %s OR id = %s'
        data_base = ('%'  + get_search_Entry + '%', get_search_Entry)
        my_cursor.execute(sql, data_base)
        result = my_cursor.fetchone()
        if result is None:
            Verification.Verification_search_name()
            return
        else:
            Show_Data.show_data(result, position, track)

        

    search_Entry = cutk.CTkEntry(root_all_data, placeholder_text='Search',  text_color='white',
                                    placeholder_text_color='white', font=('Roboto', 15), height=40, width=666, corner_radius=20, border_color='white', border_width=2)
    search_Entry.grid(row=0, column=0, pady=5)

    go = cutk.CTkButton(root_all_data, text='Go', hover_color='white', text_color='black', 
                        command=call_search, corner_radius=20, border_color='white', border_width=2, width=15, height=40)
    go.grid(row=0, column=1, pady=5)


    if position == 'editor' or position == 'manager':
        add = cutk.CTkButton(root_all_data, text='Add', hover_color='white', text_color='black', 
                            command=Add_student_call, corner_radius=20, border_color='white', border_width=2, width=15, height=40)
        add.grid(row=0, column=5, pady=5)


    Refrash = cutk.CTkButton(root_all_data, hover_color='white', text='Refrash', text_color='black', command=refrash, corner_radius=20, border_color='white', border_width=2, width=15, height=40)
    Refrash.grid(row=0, column=4, pady=5)

    Back = cutk.CTkButton(root_all_data, hover_color='white', text='Back', text_color='black', command=back, corner_radius=20, border_color='white', border_width=2, width=15, height=40)
    Back.grid(row=0, column=3, pady=5)




    def update_database(values):
        conn = mysql.connector.connect(host='localhost', user='root', passwd='@Bdallh1722', port=3306, database='Trainingee')
        cursor = conn.cursor()
        print(values)
        sql = f"UPDATE {track} SET id = %s, name = %s, degrees = %s, additional_degrees = %s, total = %s , commintent = %s  WHERE name = %s OR id = %s"
        val =  (values[0], values[1], values[2], values[3], values[4], values[5], values[1], values[0])
        cursor.execute(sql, val)
        conn.commit()
        conn.close()


    def edit_cell(event):
        selected_item = my_data.selection()[0]
        column = my_data.identify_column(event.x)
        row = my_data.identify_row(event.y)
        x, y, width, height = my_data.bbox(selected_item, column)
        entry = tk.Entry(root_all_data)
        entry.place(x=x, y=y+90, width=width, height=height)
        entry.insert(0, my_data.set(selected_item, column))
        

        def save_edit(event):
            new_value = entry.get()
            my_data.set(selected_item, column, new_value)
            entry.destroy()
            values = my_data.item(selected_item, "values")
            update_database(values)


        entry.bind("<Return>", save_edit)
        entry.focus()

    
    
    for col in columns:
        my_data.heading(col, text=col)


    my_cursor.execute(f'SELECT * FROM {track}')
    result = my_cursor.fetchall()
    for i in result:
        for u in i:
            total = int(i[2]) + int(i[3])
            sql = f'UPDATE {track} SET total = %s WHERE name = %s'
            val = (total, i[1])
            my_cursor.execute(sql, val)
            mydb.commit()

    my_cursor.execute(f'SELECT * FROM {track}')
    result = my_cursor.fetchall()
    for i in result:
        my_data.insert(parent='', index='end',  text='', values=i)




    def check():
        query = search_Entry.get().lower()
        for i in my_data.get_children():
            item = my_data.item(i)['values']
            if query in str(item).lower():
                my_data.selection_set(i)
                my_data.see(i)

    search_Entry.bind('<Return>', lambda e: check())

    my_data.grid(column=0, row=1, columnspan=25, pady=10)
    
    if position != 'user':
        my_data.bind("<Double-1>", edit_cell)
    
    root_all_data.mainloop()

