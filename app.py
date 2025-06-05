import customtkinter as ctk
import CTkListbox 

from datetime import time
from time import strftime, gmtime

class App(ctk.CTk):
    """
    Esta aplicacion sirve para una carrera de ciclista
    """
    def __init__(self):
        super().__init__()

        self.id = 4
        self.cant = 2
        self.suma = 0
        self.time_average = 0
        self.time_win = time(23, 59, 59)
        self.num_win = 0

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

        self.input_number = ctk.CTkEntry(self.actionbox_frame, placeholder_text="01")
        self.input_number.grid(row=1, column=0, padx=20, pady=20)

        self.title = ctk.CTkLabel(self.actionbox_frame, text="Tiempo de participante", fg_color="gray30", corner_radius=6)
        self.title.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.input_hour = ctk.CTkEntry(self.actionbox_frame, placeholder_text="hh")
        self.input_hour.grid(row=3, column=0, padx=20, pady=20)

        self.input_min = ctk.CTkEntry(self.actionbox_frame, placeholder_text="mm")
        self.input_min.grid(row=3, column=1, padx=20, pady=20)

        self.input_sec = ctk.CTkEntry(self.actionbox_frame, placeholder_text="ss")
        self.input_sec.grid(row=3, column=2, padx=20, pady=20)
        


        self.button1 = ctk.CTkButton(self.actionbox_frame, text="Agregar", command=self.agregar_participante)
        self.button1.grid(row=1, column=1, padx=20, pady=20)

        self.button2 = ctk.CTkButton(self.actionbox_frame, text="Borrar", command=self.borrar_participante)
        self.button2.grid(row=1, column=2, padx=20, pady=20)

        self.listbox = CTkListbox.CTkListbox(self)
        self.listbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.promedio = ctk.CTkLabel(self, text="Promedio de Tiempo de los Ciclistas: ", fg_color="green", corner_radius=6)
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
        # funcion que verfica el tiempo
        tiempo = time(int(self.input_hour.get()), int(self.input_min.get()), int(self.input_sec.get()))
        number = self.input_number.get()

        self.suma += tiempo.second
        if tiempo < self.time_win:
            self.time_win = tiempo
            self.num_win = number
        
        self.time_average = strftime("%H:%M:%S", gmtime(self.suma/self.cant))

        numero_participante = self.input_number.get()
        tiempo_participante = f"{self.input_hour.get()}:{self.input_min.get()}:{self.input_sec.get()}"
        self.listbox.insert(self.id, f"Participante {numero_participante} -- Tiempo {tiempo_participante}")
        self.id += 1


if __name__ == "__main__":
    app = App()
    app.mainloop()