import tkinter as tk
from tkinter import ttk
    


class viewMainWindow(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.geometry("1200x400+300+300")
        
        self.listaFrameIntrari=[]
        self.listaIntrariValoareInitiala=[]
        self.listaIntrariGreutate=[]
        self.valoareSpinBoxIntrari = tk.StringVar()
        self.intrari = tk.StringVar()
        self.tipFunctieIntrare = tk.StringVar()
        self.tipFunctieActivare = tk.StringVar()
        self.valoareFunctieIntrare = tk.StringVar()
        self.valoareFunctieActivare = tk.StringVar()
        self.valoareTeta = tk.StringVar()
        self.valoareAlfa = tk.StringVar()
        self.valoareFunctieIesire = tk.StringVar()
        self.valoareBinar = tk.StringVar()
        
        self.frameIntrari = ttk.Frame(self, relief=tk.RAISED, borderwidth=1)
        self.frameIntrari.pack(fill=tk.Y, side = tk.LEFT, pady=10, padx=10)
        
        self.frameIntrariNumar = ttk.Frame(self.frameIntrari, relief=tk.RAISED, borderwidth=1)
        self.frameIntrariNumar.pack(fill=tk.X, side = tk.TOP, pady=10, padx=10)
        self.labelNumarIntrari = ttk.Label(self.frameIntrariNumar, text='Number of entries:')
        self.labelNumarIntrari.pack(side = tk.LEFT, ipadx=3, ipady=3)
        self.entryNumarIntrari = ttk.Spinbox(self.frameIntrariNumar, from_=1, to=100000000, textvariable=self.valoareSpinBoxIntrari, width=7)
        self.entryNumarIntrari.pack(side = tk.LEFT)
        
       
        self.CanvasIntrariValori = tk.Canvas(self.frameIntrari)
        self.scrollBarFrameIntrariValori = ttk.Scrollbar(self.frameIntrari, orient=tk.VERTICAL, command=self.CanvasIntrariValori.yview)
        self.scrollBarFrameIntrariValori.pack(fill = tk.Y, expand=1, side = tk.RIGHT)
        self.CanvasIntrariValori.pack(fill=tk.BOTH, expand=1, side = tk.TOP)
        self.CanvasIntrariValori.configure(yscrollcommand=self.scrollBarFrameIntrariValori.set)
        self.CanvasIntrariValori.bind('<Configure>', lambda e: self.CanvasIntrariValori.configure(scrollregion = self.CanvasIntrariValori.bbox('all')))
        self.frameInCanvas = ttk.Frame(self.CanvasIntrariValori)
        self.CanvasIntrariValori.create_window((0,0), window=self.frameInCanvas, anchor=tk.NW)
        
        
        
        self.frameFunctiiSiRezultate = ttk.Frame(self, relief=tk.RAISED, borderwidth=1)
        self.frameFunctiiSiRezultate.pack(fill=tk.BOTH, expand=1, side = tk.RIGHT, pady=10, padx=10)
        self.frameFunctii = ttk.Frame(self.frameFunctiiSiRezultate, relief=tk.RAISED, borderwidth=1)
        self.frameFunctii.pack(fill=tk.BOTH, side = tk.TOP, pady=10, padx=10)
        self.frameFunctiaDeIntrare = ttk.Frame(self.frameFunctii, relief=tk.RAISED, borderwidth=1)
        self.frameFunctiaDeIntrare.pack(fill=tk.BOTH, expand=1, side = tk.LEFT, pady=10, padx=10)
        self.labelFunctiaDeIntrare = ttk.Label(self.frameFunctiaDeIntrare, text='Entry Function')
        self.labelFunctiaDeIntrare.pack(side = tk.TOP, padx=3, pady=3)
        self.entryValoareFunctiaDeIntrare = ttk.Entry(self.frameFunctiaDeIntrare, textvariable=self.valoareFunctieIntrare)
        self.entryValoareFunctiaDeIntrare.pack(side = tk.TOP, fill=tk.X)
        self.entryTipFunctiaDeIntrare = ttk.Combobox(self.frameFunctiaDeIntrare, values=['Min', 'Max', 'Suma', 'Produs'], textvariable=self.tipFunctieIntrare)
        self.tipFunctieIntrare.set('Min')
        self.entryTipFunctiaDeIntrare.pack(side = tk.TOP, fill=tk.X)
        
        self.frameFunctiaDeActivare = ttk.Frame(self.frameFunctii, relief=tk.RAISED, borderwidth=1)
        self.frameFunctiaDeActivare.pack(fill=tk.BOTH, expand=1, side = tk.LEFT, pady=10, padx=10)
        self.labelFunctiaDeActivare = ttk.Label(self.frameFunctiaDeActivare, text='Activation Function')
        self.labelFunctiaDeActivare.pack(side = tk.TOP, padx=3, pady=3)
        self.entryValoareFunctiaDeActivare = ttk.Entry(self.frameFunctiaDeActivare, textvariable = self.valoareFunctieActivare)
        self.entryValoareFunctiaDeActivare.pack(side = tk.TOP, fill=tk.X)
        self.entryTipFunctiaDeActivare = ttk.Combobox(self.frameFunctiaDeActivare, values=['Liniara', 'Semn', 'Sigmoidala', 'Treapta', 'Tangenta'], textvariable=self.tipFunctieActivare)
        self.tipFunctieActivare.set('Liniara')
        self.entryTipFunctiaDeActivare.pack(side = tk.TOP, fill=tk.X)
        self.frameTeta = ttk.Frame(self.frameFunctiaDeActivare, relief=tk.RAISED, borderwidth=1)
        self.frameTeta.pack(side = tk.TOP, fill=tk.X)
        self.labelTeta = tk.Label(self.frameTeta, text='θ:', height=1, width=3)
        self.labelTeta.pack(side = tk.LEFT, padx=3, pady=3)
        self.entryTetaFunctiaDeActivare = ttk.Spinbox(self.frameTeta, from_=0, to=100000000, increment=0.01, width=7, textvariable = self.valoareTeta)
        self.entryTetaFunctiaDeActivare.pack(side = tk.LEFT)
        self.valoareTeta.set('0.00')
        self.frameAlfa = ttk.Frame(self.frameFunctiaDeActivare, relief=tk.RAISED, borderwidth=1)
        self.frameAlfa.pack(side = tk.TOP, fill=tk.X)
        self.labelAlfa = tk.Label(self.frameAlfa, text='Alpha:', height=1, width=3)
        self.labelAlfa.pack(side = tk.LEFT, padx=3, pady=3)
        self.entryAlfaFunctiaDeActivare = ttk.Spinbox(self.frameAlfa, from_=0, to=100000000, increment=0.01, width=7, textvariable = self.valoareAlfa)
        self.entryAlfaFunctiaDeActivare.pack(side = tk.LEFT)
        self.valoareAlfa.set('1.00')
        
        self.frameFunctiaDeIesire = ttk.Frame(self.frameFunctii, relief=tk.RAISED, borderwidth=1)
        self.frameFunctiaDeIesire.pack(fill=tk.BOTH, expand=1, side = tk.LEFT, pady=10, padx=10)
        self.labelFunctiaDeIesire = ttk.Label(self.frameFunctiaDeIesire, text='Output Function')
        self.labelFunctiaDeIesire.pack(side = tk.TOP, padx=3, pady=3)
        self.entryValoareFunctiaDeIesire = ttk.Entry(self.frameFunctiaDeIesire, textvariable = self.valoareFunctieIesire)
        self.entryValoareFunctiaDeIesire.pack(side = tk.TOP, fill=tk.X)
        self.entryBinarFunctiaDeIesire = tk.Checkbutton(self.frameFunctiaDeIesire, text='Binary', variable = self.valoareBinar, onvalue='true', offvalue='false')
        self.entryBinarFunctiaDeIesire.pack(side = tk.TOP)
        self.valoareBinar.set('false')
        
        
        self.frameGrafic = ttk.Frame(self.frameFunctiiSiRezultate, relief=tk.RAISED, borderwidth=1)
        self.frameGrafic.pack(fill=tk.BOTH, expand=1, side = tk.TOP, pady=10, padx=10)
        
        
    def main(self):
        self.valoareSpinBoxIntrari.set('1')
        self.intrari.set('1')
        
        self.frameIntrariValori1 = ttk.Frame(self.frameInCanvas, relief=tk.RAISED, borderwidth=1)
        self.listaFrameIntrari.append(self.frameIntrariValori1)
        self.frameIntrariValori1.pack(fill=tk.X, side = tk.TOP, padx=10, pady=10)
        self.labelIn = tk.Label(self.frameIntrariValori1, text='Ini0', height=1, width=3)
        self.labelIn.pack(side = tk.LEFT, padx=3, pady=3)
        self.intrareValoare = tk.StringVar()
        self.entryIni0 = ttk.Spinbox(self.frameIntrariValori1, from_=-1000000, to=1000000, increment=0.01, textvariable = self.intrareValoare)
        self.intrareValoare.set('0.01')
        self.listaIntrariValoareInitiala.append(self.intrareValoare)
        self.entryIni0.pack(fill=tk.X, expand=1, side = tk.LEFT)
        self.labelW0 = tk.Label(self.frameIntrariValori1, text='Wi0', height=1, width=3)
        self.labelW0.pack(side = tk.LEFT, padx=3, pady=3)
        self.intrareGreutate = tk.StringVar()
        self.entryWi0 = ttk.Spinbox(self.frameIntrariValori1, from_=-1000000, to=1000000, increment=0.01, textvariable= self.intrareGreutate)
        self.intrareGreutate.set('0.01')
        self.listaIntrariGreutate.append(self.intrareGreutate)
        self.entryWi0.pack(fill=tk.X, expand=1, side = tk.LEFT)
        self.CanvasIntrariValori.configure(scrollregion=self.CanvasIntrariValori.bbox("all"))
        self.intrareValoare.trace('w', self.controller.calculeaza)
        self.intrareGreutate.trace('w', self.controller.calculeaza)
        
        self.valoareSpinBoxIntrari.trace('w', self.controller.update_numar_intrari)
        
        self.tipFunctieIntrare.trace('w', self.controller.calculeaza)
        self.tipFunctieActivare.trace('w', self.controller.calculeaza)
        self.valoareTeta.trace('w', self.controller.calculeaza)
        self.valoareAlfa.trace('w', self.controller.calculeaza)
        self.valoareBinar.trace('w', self.controller.calculeaza)
        
        self.controller.calculeaza()
        
        self.mainloop()
