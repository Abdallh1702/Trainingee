import customtkinter as cutk
from PIL import Image, ImageTk
import Settings
import mysql.connector
import List
import search_in_all_track



def first_page(position):

    mydb = mysql.connector.connect(host='localhost', user='root', passwd='@Bdallh1722', port=3306, database='Trainingee')
    my_cursor = mydb.cursor()



    root_home = cutk.CTk()
    root_home.geometry('750x500')
    # root_home.minsize(550, 500)
    # root_home.maxsize(550, 500)
    root_home.title('Home')
    cutk.set_appearance_mode('dark')
    cutk.set_default_color_theme('green')

    root_home.rowconfigure([0, 1], weight=1)
    root_home.columnconfigure(0, weight=1)

    imag = cutk.CTkImage(light_image=Image.open('ty.jpg'), size=(150,150))
    jws = cutk.CTkImage(light_image=Image.open('js.jpg'), size=(150,150))
    java = cutk.CTkImage(light_image=Image.open('java.jpg'), size=(150,150))
    php = cutk.CTkImage(light_image=Image.open('php.jpg'), size=(150,150))
    node = cutk.CTkImage(light_image=Image.open('node.png'), size=(150,150))
    html = cutk.CTkImage(light_image=Image.open('html.jpg'), size=(150,150))


    def check_track(track_name):
        track = track_name[0]
        root_home.destroy()
        List.search_or_add(position, track)

    def settings_page():
        root_home.destroy()
        Settings.settings_call(position)

    
    def search(event):
        entry_name = Name.get()
        search_in_all_track.search(entry_name)

        
    def logout():
        import link
        root_home.destroy()
        link.back_to_logen_page()



    frame = cutk.CTkFrame(root_home)
    frame.grid(row=1, column=0, ipadx=33, ipady=33, padx=20, pady=20)
    frame.rowconfigure((0, 1), weight=1)
    frame.columnconfigure([0, 1, 2], weight=1)


    logout = cutk.CTkButton(frame, text='Logout', hover_color='white', text_color='black', corner_radius=20,
                             command=logout, width=5, border_color='white', border_width=2)
    logout.grid(row=0, column=3)


    if position == 'manager':

        frame_buttons = cutk.CTkFrame(frame)
        frame_buttons.grid(row=0, column=2, sticky='e', padx=29)
        frame_buttons.rowconfigure(0, weight=1)
        frame_buttons.columnconfigure([0, 1, 2], weight=1)

        image = Image.open("setti.png")
        image = image.resize((15, 15))
        photo = ImageTk.PhotoImage(image)


        button = cutk.CTkButton(frame_buttons, text="Settings", command=settings_page, 
                                 width=100, height=20, corner_radius=20, 
                                hover_color='white', border_color='white', border_width=2,
                                 image=photo, compound="left", text_color='black')

        button.grid(row=0, column=2)

    Name = cutk.CTkEntry(frame, placeholder_text='Search',  text_color='white', placeholder_text_color='white',
                         font=('Roboto', 15), height=30, width=410, corner_radius=20, border_color='white', border_width=2)
    Name.grid(row=0, column=0, padx=10, pady=12)


    my_cursor.execute('SHOW TABLES')
    result = my_cursor.fetchall()
    row = 1
    column = 0


    for i in result:
        if i != result[0]:
            add_frame = cutk.CTkFrame(frame, corner_radius=20)
            add_frame.grid(row=row, column=column, ipadx=33, ipady=33, padx=10, pady=10)
            add_frame.rowconfigure((0, 1), weight=1)
            add_frame.columnconfigure(0, weight=1)

            label = cutk.CTkButton(add_frame, image=jws, corner_radius=20, bg_color='#ced4da', text=i,
                                   text_color='black', hover_color='#6c757d')
            label.configure(command=lambda button=i: check_track(button))
            label.grid(row=0, column=0)
            label.configure(fg_color='#ced4da')

            if column == 2:
                column = 0
                row += 1 
            else:
                column += 1

    
    root_home.bind('<Return>', search)

    root_home.mainloop()

