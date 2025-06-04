import customtkinter as ctk
import CTkListbox 

class App(ctk.CTk):
    """
    Esta aplicacion sirve para una carrera de ciclista
    """
    def __init__(self):
        super().__init__()

        self.title("Carrera de ciclismo")
        self.geometry("700x500")

        self.grid_columnconfigure(0, weight=1) 
        self.grid_rowconfigure(0, weight=1) 
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=2)
        

        self.actionbox_frame = ctk.CTkFrame(self)
        self.actionbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")


        self.title = ctk.CTkLabel(self.actionbox_frame, text="Numero de participante", fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.entryn = ctk.CTkEntry(self.actionbox_frame, placeholder_text="01")
        self.entryn.grid(row=1, column=0, padx=20, pady=20)

        self.title = ctk.CTkLabel(self.actionbox_frame, text="Tiempo de participante", fg_color="gray30", corner_radius=6)
        self.title.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.entryh = ctk.CTkEntry(self.actionbox_frame, placeholder_text="hh")
        self.entryh.grid(row=3, column=0, padx=20, pady=20)

        self.entrym = ctk.CTkEntry(self.actionbox_frame, placeholder_text="mm")
        self.entrym.grid(row=3, column=1, padx=20, pady=20)

        self.entrys = ctk.CTkEntry(self.actionbox_frame, placeholder_text="ss")
        self.entrys.grid(row=3, column=2, padx=20, pady=20)
        


        self.button1 = ctk.CTkButton(self.actionbox_frame, text="Agregar", command=self.agregar_participante)
        self.button1.grid(row=1, column=1, padx=20, pady=20)

        self.button2 = ctk.CTkButton(self.actionbox_frame, text="Borrar", command=self.borrar_participante)
        self.button2.grid(row=1, column=2, padx=20, pady=20)

        self.listbox = CTkListbox.CTkListbox(self)
        self.listbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.listbox.insert(1, f"Participante {"01"} -- Tiempo {"00:21:10"}")
        self.listbox.insert(2, f"Participante {"02"} -- Tiempo {"00:11:43"}")
        self.listbox.insert(3, f"Participante {"03"} -- Tiempo {"00:09:27"}")
        self.id = 4

        self.promedio = ctk.CTkLabel(self, text="Promedio de Tiempo de los Ciclistas:", fg_color="green", corner_radius=6)
        self.promedio.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")


    def borrar_participante(self):
        """
        Esta funcion sirve para borrar participantes
        """
        element = self.listbox.curselection()
        self.listbox.delete(element)
    
    def agregar_participante(self):
        """
        Esta funcion sirve para agregar participantes
        """
        numero_participante = self.entryn.get()
        tiempo_participante = f"{self.entryh.get()}:{self.entrym.get()}:{self.entrys.get()}"
        self.listbox.insert(self.id, f"Participante {numero_participante} -- Tiempo {tiempo_participante}")
        self.id += 1


if __name__ == "__main__":
    app = App()
    app.mainloop()