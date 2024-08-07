import customtkinter as cutk
import mysql.connector
import Verification




def login():
    global show_password

    mydb = mysql.connector.connect(host='localhost', user='root', passwd='@Bdallh1722', port=3306,
                                   database='Trainingee')
    my_cursor = mydb.cursor()

    
    root_login = cutk.CTk()
    root_login.geometry('750x500')
    root_login.minsize(550, 350)
    root_login.maxsize(550, 350)
    cutk.set_appearance_mode('dark')
    cutk.set_default_color_theme('green')
    


    frame = cutk.CTkFrame(root_login, corner_radius=20)
    frame.pack(padx=5, pady=5, fill='both', expand=True)


    label = cutk.CTkLabel(frame, text='Welcome to Trainingee', font=('𝔻𝕠𝕦𝕓𝕝𝕖-𝕊𝕥𝕣𝕦𝕔𝕜 𝕋𝕖𝕩𝕥', 23), text_color='white')
    label.pack(padx=10, pady=12)


    label = cutk.CTkLabel(frame, text='Login to be able to manage courses and students',
                          font=('𝔻𝕠𝕦𝕓𝕝𝕖-𝕊𝕥𝕣𝕦𝕔𝕜 𝕋𝕖𝕩𝕥', 15), text_color='white')
    label.pack(padx=10, pady=12)


    entry1 = cutk.CTkEntry(frame, placeholder_text='Username', text_color='white',
                           placeholder_text_color='white', font=('Roboto', 15), height=30, width=250, corner_radius=20, border_color='white', border_width=2)
    entry1.pack(padx=10, pady=12)


    entry2 = cutk.CTkEntry(frame, placeholder_text='Password', show='*',  text_color='white',
                           placeholder_text_color='white', font=('Roboto', 15), height=30, width=250, corner_radius=20, border_color='white', border_width=2)
    entry2.pack(padx=10, pady=12)


    def show_password_check():
        global show_password
        if entry2.cget('show') == '*':
            entry2.configure(show='')
        else:
            entry2.configure(show='*')

    

    def check():
        import First_Page
        global user_name, result
        entry_1 = entry1.get()
        entry_2 = entry2.get()
        sql = 'SELECT * FROM data_users_login WHERE user_name = %s '
        data_base = (entry_1,)
        my_cursor.execute(sql, data_base)
        result = my_cursor.fetchone()
        if entry_1 == '':
            Verification.Verification_name()
        elif entry_2 == '':
            Verification.Verification_password()
        else:
            if result is None:
                Verification.Verification_name_found()
                return
            user_name = result[0]
            password =result[1]
            if result is not None:
                if entry_2 != password:
                    Verification.Verification_wrong_password()
                elif entry_2 == password:
                    root_login.destroy()
                    First_Page.first_page(result[2])
                                                                                    
                    
    show_password = cutk.CTkCheckBox(frame, text='Show Password', command=show_password_check,
                                     font=('𝔻𝕠𝕦𝕓𝕝𝕖-𝕊𝕥𝕣𝕦𝕔𝕜 𝕋𝕖𝕩𝕥', 12), text_color='white')
    show_password.pack(pady=15)

    
    button = cutk.CTkButton(frame, text='Login', hover_color='white', text_color='black', command=check, corner_radius=20, border_color='white', border_width=2)
    button.pack(padx=10, pady=12)

    root_login.bind('<Return>', lambda e: check())

    root_login.mainloop()

login()