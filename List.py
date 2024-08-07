import customtkinter as cutk
import Add_Student
import Search
import Show_All_Data
import First_Page

def search_or_add(position, track):
    root_search_or_add = cutk.CTk()
    root_search_or_add.geometry('750x500')
    root_search_or_add.minsize(550, 400)
    root_search_or_add.maxsize(550, 400)
    root_search_or_add.title('Search Or Add')
    cutk.set_appearance_mode('dark')
    cutk.set_default_color_theme('green')

    def search():
        root_search_or_add.destroy()
        Search.search(position, track)


    def add_student():
        root_search_or_add.destroy()
        Add_Student.Add_student(position , track)

    def all_student():
        root_search_or_add.destroy()
        Show_All_Data.show_all_data(position, track)

    def back_to_first_page():
        root_search_or_add.destroy()
        First_Page.first_page(position)


    def Close(): 
        root_search_or_add.destroy()

    frame = cutk.CTkFrame(root_search_or_add)
    frame.pack(padx=5, pady=5, fill='both', expand=True)

    label = cutk.CTkLabel(frame, text='Do You Want To Add A New Student Or \n Do You Want To Search For A Student?', font=('𝔻𝕠𝕦𝕓𝕝𝕖-𝕊𝕥𝕣𝕦𝕔𝕜 𝕋𝕖𝕩𝕥', 24), text_color='white')
    label.pack(padx=10, pady=12)

    search = cutk.CTkButton(frame, text='Search', hover_color='white', text_color='black', command=search, corner_radius=20, border_color='white', border_width=2)
    search.pack(pady=15)

    if position == 'editor' or position == 'manager':
        add = cutk.CTkButton(frame, text='Add', hover_color='white', text_color='black', command=add_student, corner_radius=20, border_color='white', border_width=2)
        add.pack(pady=15)

    all_data = cutk.CTkButton(frame, text='All Student', hover_color='white', text_color='black', command=all_student, corner_radius=20, border_color='white', border_width=2)
    all_data.pack(pady=15)

    back = cutk.CTkButton(frame, text='Back', hover_color='white', text_color='black', command=back_to_first_page, corner_radius=20, border_color='white', border_width=2) 
    back.pack(pady=15)

    Close = cutk.CTkButton(frame, text='Close', hover_color='white', text_color='black', command=Close, corner_radius=20, border_color='white', border_width=2) 
    Close.pack(pady=15)
        

    root_search_or_add.mainloop()

