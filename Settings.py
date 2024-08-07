import customtkinter as cutk
import Add_users
import First_Page
import show_all_users
from PIL import Image, ImageTk
import add_or_delete_track

def settings_call(position):

    root_settings = cutk.CTk()
    root_settings.geometry('750x500')
    root_settings.minsize(450, 400)
    root_settings.maxsize(450, 400)
    root_settings.title('Settings')
    cutk.set_appearance_mode('dark')
    cutk.set_default_color_theme('green')


    frame = cutk.CTkFrame(root_settings)
    frame.pack(padx=5, pady=5, fill='both', expand=True)


    def add_users():
        print('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')
        Add_users.add_users_call()


    def delete_user():
        root_settings.destroy()
        Add_users.delete_user(position)


    def add_track_call():
        root_settings.destroy()
        add_or_delete_track.add_track(position)


    def delete_track_call():
        root_settings.destroy()
        add_or_delete_track.delete_track_in_data_base(position)
        


    def show_users():
        root_settings.destroy()
        show_all_users.show_users(position)


    def back():
        root_settings.destroy()
        First_Page.first_page(position)


    label_settings = cutk.CTkLabel(frame, font=('Roboto', 16), text='Settings', text_color='red', corner_radius=20)
    label_settings.pack()

    image = Image.open("user.png")
    image = image.resize((15, 15))
    photo = ImageTk.PhotoImage(image)

    button = cutk.CTkButton(frame, text="Add User", command=add_users, 
                                corner_radius=20, 
                                hover_color='white', border_color='white', border_width=2,
                                 image=photo, compound="left", text_color='black')

    button.pack(padx=5, pady=5)

    delete_user = cutk.CTkButton(frame, text='Delete User', hover_color='white', text_color='black', corner_radius=20, command=delete_user, border_color='white', border_width=2) 
    delete_user.pack(padx=5, pady=5)

    show_users = cutk.CTkButton(frame, text='Show All Users', hover_color='white', text_color='black', corner_radius=20, command=show_users, border_color='white', border_width=2) 
    show_users.pack(padx=5, pady=5)

    label_space = cutk.CTkLabel(frame, font=('Roboto', 16), text=' ', text_color='red', corner_radius=20)
    label_space.pack()


    add_track = cutk.CTkButton(frame, text='Add Track', hover_color='white', text_color='black', corner_radius=20, command=add_track_call, border_color='white', border_width=2) 
    add_track.pack(padx=5, pady=5)

    delete_track = cutk.CTkButton(frame, text='Delete Track ', hover_color='white', text_color='black', corner_radius=20, command=delete_track_call, border_color='white', border_width=2) 
    delete_track.pack(padx=5, pady=5)

    label_space = cutk.CTkLabel(frame, font=('Roboto', 16), text=' ', text_color='red', corner_radius=20)
    label_space.pack()

    
    back = cutk.CTkButton(frame, text='Back', hover_color='white', text_color='black', corner_radius=20, command=back , border_color='white', border_width=2) 
    back.pack(padx=5, pady=5)

    root_settings.mainloop()


