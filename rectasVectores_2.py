# cd C:\Users\USUARIO\Documents\GitHub\Facu\Facu-main\Python

from tkinter import *
from math import sqrt, pow

genpad = 6 #Padding general

class Aplication(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=200, height=200) #Tamaño de ventana
        self.master = master
        self.pack()
        self.createWidgets()

    def vectorDirecc(self, w1, w2, v1, v2):
        global u1, u2
        u1 = round(w1 - v1, 1)
        u2 = round(w2 - v2, 1)
    
    def rectaParemetrica(self, w1, w2):
        self.parametricRect.config(text=f"x = {w1} + ({u1}).t \n y = {w2} + ({u2}).t", fg="green")
    
    def rectaCartesiana(self, w1, w2):
        global a, b, c
        a = -u2 
        b = u1
        c = -((a * w1) + (b * w2))
        self.cartesianRect.config(text=f"({a})x + ({b})y + {c} = 0", fg="green")
    
    def rectaExplicita(self):
        m = round(-(a/b), 2)
        h = round(-(c/b), 2)
        self.explicitRect.config(text=f"y = ({m})x + ({h})", fg="green")
    
    def rectaSegmentaria(self):
        corteX = round(-(c/a), 2)
        corteY = round(-(c/b), 2)
        self.segmentaryRect.config(text=f"x/({corteX}) + y/({corteY}) = 1", fg="green")
    
    def W_vectorModule(self):
        try: 
            w1 = float(self.W_firstComponent_entry.get())
            w2 = float(self.W_secondComponent_entry.get())
            w3 = float(self.W_thirdComponent_entry.get())
        except: #SI SE INGRESAN VALORES NO NUMERICOS O NULL, NO SE EJECUTA NADA
            pass
        else: 
            longitudBruta = pow(w1, 2) + pow(w2, 2) + pow(w3, 2)
            longitudExacta = round(sqrt(pow(w1, 2) + pow(w2, 2) + pow(w3, 2)), 3)
            self.module_W.config(text=f"√{longitudBruta} = {longitudExacta}", fg="green")
        
    def V_vectorModule(self):
        try: 
            v1 = float(self.V_firstComponent_entry.get())
            v2 = float(self.V_secondComponent_entry.get())
            v3 = float(self.V_thirdComponent_entry.get())
        except: #SI SE INGRESAN VALORES NO NUMERICOS O NULL, NO SE EJECUTA NADA
            pass
        else: 
            longitudBruta = pow(v1, 2) + pow(v2, 2) + pow(v3, 2)
            longitudExacta = round(sqrt(pow(v1, 2) + pow(v2, 2) + pow(v3, 2)), 3)
            self.module_V.config(text=f"√{longitudBruta} = {longitudExacta}", fg="green")

    def everything(self): #Ejecuta las funciones de ecuaciones
        try: 
            w1 = round(float(self.W_firstComponent_entry.get()), 2)
            w2 = round(float(self.W_secondComponent_entry.get()), 2)
            v1 = round(float(self.V_firstComponent_entry.get()), 2)
            v2 = round(float(self.V_secondComponent_entry.get()), 2)
        except: 
            pass
        else:
            self.vectorDirecc(w1, w2, v1, v2)
            self.rectaParemetrica(w1, w2)
            self.rectaCartesiana(w1, w2)
            if b != 0:
                self.rectaExplicita()
                if a != 0:
                    self.rectaSegmentaria()
            else: 
                self.explicitRect.config(text="--------------", fg="red")
                self.segmentaryRect.config(text="--------------", fg="red")
    
    def createWidgets(self):
        self.W_frame = Frame(self, highlightcolor="grey", highlightthickness=2, padx=genpad, pady=genpad) #Caja contenedora del vector 1
        self.V_frame = Frame(self, highlightcolor="grey", highlightthickness=2, padx=genpad, pady=genpad) #Caja contenedora del vector 2
        # --------------------------------------------------------------------------- Titulos de los frames
        self.W_text = Label(self.W_frame, text="Vector W: ")
        self.W_text.grid(row=0, column=0, ipadx=genpad, ipady=genpad)
        self.W_submit_button = Button(self.W_frame, text="Calcular modulo", command=self.W_vectorModule)
        self.W_submit_button.grid(row=0, column=1)
        
        self.V_text = Label(self.V_frame, text="Vector V: ")
        self.V_text.grid(row=0, column=0, ipadx=genpad, ipady=genpad)
        self.V_submit_button = Button(self.V_frame, text="Calcular modulo", command=self.V_vectorModule)
        self.V_submit_button.grid(row=0, column=1)
        # --------------------------------------------------------------------------- Primera fila, vector 1 
        self.W_firstComponent_text = Label(self.W_frame, text="Introduzca la primera componente: ")
        self.W_firstComponent_text.grid(row=1, column=0, ipadx=genpad, ipady=genpad)
        
        self.W_firstComponent_entry = Entry(self.W_frame)
        self.W_firstComponent_entry.grid(row=1, column=1, ipadx=genpad, ipady=genpad)
        # --------------------------------------------------------------------------- Primera fila, vector 2
        self.V_firstComponent_text = Label(self.V_frame, text="Introduzca la primera componente: ")
        self.V_firstComponent_text.grid(row=1, column=0, ipadx=genpad, ipady=genpad)
        
        self.V_firstComponent_entry = Entry(self.V_frame)
        self.V_firstComponent_entry.grid(row=1, column=1, ipadx=genpad, ipady=genpad)

        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Segunda fila, vector 1

        self.W_secondComponent_text = Label(self.W_frame, text="Introduzca la segunda componente: ")
        self.W_secondComponent_text.grid(row=2, column=0, ipadx=genpad, ipady=genpad)
        
        self.W_secondComponent_entry = Entry(self.W_frame)
        self.W_secondComponent_entry.grid(row=2, column=1, ipadx=genpad, ipady=genpad)
        # --------------------------------------------------------------------------- Segunda fila, vector 2
        self.V_secondComponent_text = Label(self.V_frame, text="Introduzca la segunda componente: ")
        self.V_secondComponent_text.grid(row=2, column=0, ipadx=genpad, ipady=genpad)
        
        self.V_secondComponent_entry = Entry(self.V_frame)
        self.V_secondComponent_entry.grid(row=2, column=1, ipadx=genpad, ipady=genpad)

        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Tercera fila, vector 1

        self.W_thirdComponent_text = Label(self.W_frame, text="Introduzca la tercera componente: ")
        self.W_thirdComponent_text.grid(row=3, column=0, ipadx=genpad, ipady=genpad)
        
        self.W_thirdComponent_entry = Entry(self.W_frame)
        self.W_thirdComponent_entry.grid(row=3, column=1, ipadx=genpad, ipady=genpad)
        # --------------------------------------------------------------------------- Tercera fila, vector 2
        self.V_thirdComponent_text = Label(self.V_frame, text="Introduzca la tercera componente: ")
        self.V_thirdComponent_text.grid(row=3, column=0, ipadx=genpad, ipady=genpad)
        
        self.V_thirdComponent_entry = Entry(self.V_frame)
        self.V_thirdComponent_entry.grid(row=3, column=1, ipadx=genpad, ipady=genpad)

        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Packing de los frames
        # * Posicionado de los frames
        self.W_frame.grid(row=0, column=0) 
        self.V_frame.grid(row=0, column=1) 
        # --------------------------------------------------------------------------- Boton de ingresar datos 
        self.submitComponents_button = Button(self, text="Ingresar valores", command=self.everything)
        self.submitComponents_button.grid(row=3, column=0, columnspan=2, ipadx=genpad, ipady=genpad)
        # --------------------------------------------------------------------------- Texto a sobreescribir por las funciones
        self.results_frame = Frame(self, padx=genpad, pady=genpad)
        
        self.module_W_text = Label(self.results_frame, text="Modulo del vector W: ")
        self.module_W_text.grid(row=0, column=0)
        self.module_W = Label(self.results_frame) # SUSTITUIR
        self.module_W.grid(row=0, column=1)

        self.module_V_text = Label(self.results_frame, text="Modulo del vector V: ")
        self.module_V_text.grid(row=1, column=0)
        self.module_V = Label(self.results_frame) # SUSTITUIR   
        self.module_V.grid(row=1, column=1)


        self.parametricRect_text = Label(self.results_frame, text="Recta parametrica que pasa por los puntos: ")
        self.parametricRect_text.grid(row=3, column=0)
        self.parametricRect = Label(self.results_frame)
        self.parametricRect.grid(row=3, column=1)   


        self.cartesianRect_text = Label(self.results_frame, text="Recta cartesiana: ")
        self.cartesianRect_text.grid(row=4, column=0)
        self.cartesianRect = Label(self.results_frame)
        self.cartesianRect.grid(row=4, column=1)


        self.segmentaryRect_text = Label(self.results_frame, text="Recta segmentaria: ")
        self.segmentaryRect_text.grid(row=5, column=0)
        self.segmentaryRect = Label(self.results_frame)
        self.segmentaryRect.grid(row=5, column=1)


        self.explicitRect_text = Label(self.results_frame, text="Recta explicita")
        self.explicitRect_text.grid(row=6, column=0)
        self.explicitRect = Label(self.results_frame)
        self.explicitRect.grid(row=6, column=1)

        self.results_frame.grid(row=4, column=0)
        
root = Tk() #Creacion de la ventana
app = Aplication(master=root)
app.mainloop()

