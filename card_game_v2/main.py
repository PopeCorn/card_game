import customtkinter as cstki

cstki.set_appearance_mode('dark')
cstki.set_default_color_theme('green')

first_player = []
second_player = []
def adding(player):
    player.append(entry)


root = cstki.CTk()
root.geometry('500x300')

frame = cstki.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = cstki.CTkLabel(master=frame, text='Card game')
label.pack(pady=12, padx=10)

entry = cstki.CTkEntry(master=frame, placeholder_text='New character')
entry.pack(pady=12, padx=10)

button = cstki.CTkButton(master=frame, text='Add', command=adding(first_player))
button.pack(pady=12, padx=10)

textbox = cstki.CTkTextbox(master=root)
textbox.insert("0.0", '''Available characters:
        David
        Matyas
        Mojmir
        Honza
        Zimik
        Kvitek
        Mark
        Milan
        Nikolas
        Pavel
        Petr
        Tom''')
text = textbox.get("0.0", "end")
textbox.pack(pady=20, padx=20)

if __name__ == '__main__':
    root.mainloop()
    print(first_player)