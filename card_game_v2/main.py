import customtkinter as cstki

cstki.set_appearance_mode('dark')
cstki.set_default_color_theme('green')
players = []

class App(cstki.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("Card Game")
        self.minsize(300, 200)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.textbox = cstki.CTkTextbox(master=self)
        self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        self.combobox = cstki.CTkComboBox(master=self, values=["David", "Honza", "Kvítek", "Mark", "Matyas", "Milan", "Mojmir", "Nikolas", "Pavel", "Petr", "Tom", "Žimík"])
        self.combobox.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.button = cstki.CTkButton(master=self, command=self.button_callback, text="Add character")
        self.button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

    def button_callback(self):
        if self.combobox.get() in players:
            self.textbox.insert("insert", "You or someone else already already have that character!\n")
        else:
            self.textbox.insert("insert", self.combobox.get() + " added\n")
            players.append(self.combobox.get())
            print(players)


if __name__ == "__main__":
    app = App()
    app.mainloop()