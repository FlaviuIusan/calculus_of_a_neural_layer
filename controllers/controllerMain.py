import sys
sys.path.insert(1, 'C:/Users/State/Desktop/Inteligenta Artificiala/Proiect1/views')
sys.path.insert(1, 'C:/Users/State/Desktop/Inteligenta Artificiala/Proiect1/models')

import tkinter as tk
from tkinter import ttk

from viewMainWindow import viewMainWindow

class controllerMain:
    def __init__(self):
        self.view = viewMainWindow(self)
        self.listaIntrariValoriFinale = []
        self.valoareFunctieIntrareNerotunjit = 0
        
    def main(self):
        self.view.main()
        
    def calculeaza(self, *args):
        for i in range(0, len(self.view.listaIntrariValoareInitiala)):
            valoareIntrareFinala = round(float(self.view.listaIntrariValoareInitiala[i].get())*float(self.view.listaIntrariGreutate[i].get()), 8)
            if len(self.listaIntrariValoriFinale)<=i:
                self.listaIntrariValoriFinale.append(0.0)
            self.listaIntrariValoriFinale[i] = valoareIntrareFinala
            
        if self.view.tipFunctieIntrare.get() == 'Min':
            valoareFunctie = 1000000
            for i in range(0, len(self.listaIntrariValoriFinale)):
                if self.listaIntrariValoriFinale[i]<valoareFunctie:
                    valoareFunctie = self.listaIntrariValoriFinale[i]
            valoareFunctie = valoareFunctie - float(self.view.valoareTeta.get())
            self.valoareFunctieIntrareNerotunjit = valoareFunctie
            self.view.valoareFunctieIntrare.set(format(valoareFunctie, '.20f'))
        elif self.view.tipFunctieIntrare.get() == 'Max':
            valoareFunctie = -1000000
            for i in range(0, len(self.listaIntrariValoriFinale)):
                if self.listaIntrariValoriFinale[i]>valoareFunctie:
                    valoareFunctie = self.listaIntrariValoriFinale[i]
            valoareFunctie = valoareFunctie - float(self.view.valoareTeta.get())
            self.valoareFunctieIntrareNerotunjit = valoareFunctie
            self.view.valoareFunctieIntrare.set(format(valoareFunctie, '.20f'))
            
        elif self.view.tipFunctieIntrare.get() == 'Suma':
            valoareFunctie = 0.00000000
            for i in range(0, len(self.listaIntrariValoriFinale)):
                valoareFunctie = valoareFunctie + self.listaIntrariValoriFinale[i]
            valoareFunctie = valoareFunctie - float(self.view.valoareTeta.get())
            self.valoareFunctieIntrareNerotunjit = valoareFunctie
            self.view.valoareFunctieIntrare.set(format(valoareFunctie, '.20f'))
            
        elif self.view.tipFunctieIntrare.get() == 'Produs':
            valoareFunctie = 1.00000000
            for i in range(0, len(self.listaIntrariValoriFinale)):
                valoareFunctie = valoareFunctie * self.listaIntrariValoriFinale[i]
            valoareFunctie = valoareFunctie - float(self.view.valoareTeta.get())
            self.valoareFunctieIntrareNerotunjit = valoareFunctie
            self.view.valoareFunctieIntrare.set(format(valoareFunctie, '.20f'))
        
        if self.view.tipFunctieActivare.get() == 'Liniara':
            self.view.labelAlfa.config(text = 'α:')
            if float(self.view.valoareFunctieIntrare.get()) < (-1)/float(self.view.valoareAlfa.get()):
                self.view.valoareFunctieActivare.set('-1.00000000')
            elif float(self.view.valoareFunctieIntrare.get()) > 1/float(self.view.valoareAlfa.get()):
                self.view.valoareFunctieActivare.set('1.00000000')
            else:
                self.view.valoareFunctieActivare.set(format(float(self.view.valoareFunctieIntrare.get())*float(self.view.valoareAlfa.get()), '.20f'))
        elif self.view.tipFunctieActivare.get() == 'Semn':
            self.view.labelAlfa.config(text = 'α:')
            if float(self.view.valoareFunctieIntrare.get()) >= float(self.view.valoareTeta.get()):
                self.view.valoareFunctieActivare.set('1.00000000')
            else:
                self.view.valoareFunctieActivare.set('-1.00000000')
        elif self.view.tipFunctieActivare.get() == 'Sigmoidala':
            self.view.labelAlfa.config(text = 'g:')
            e = 2.71
            valoareFunctie = 1 / ( 1 + pow(e, float(self.view.valoareAlfa.get()) * (-1) * (float(self.view.valoareFunctieIntrare.get()) - float(self.view.valoareTeta.get()))))
            self.view.valoareFunctieActivare.set(format(valoareFunctie, '.20f'))
        elif self.view.tipFunctieActivare.get() == 'Treapta':
            self.view.labelAlfa.config(text = 'α:')
            if float(self.view.valoareFunctieIntrare.get()) >= float(self.view.valoareTeta.get()):
                self.view.valoareFunctieActivare.set('1.00000000')
            else:
                self.view.valoareFunctieActivare.set('0')
        elif self.view.tipFunctieActivare.get() == 'Tangenta':
            self.view.labelAlfa.config(text = 'g:')
            e = 2.71
            valoareFunctieIntrare = float(self.view.valoareFunctieIntrare.get())
            alfa = float(self.view.valoareAlfa.get())
            teta = float(self.view.valoareTeta.get())
            valoareFunctie = ( pow(e, alfa * ( valoareFunctieIntrare - teta )) - pow(e, -alfa * ( valoareFunctieIntrare - teta )) ) / ( pow(e, alfa * ( valoareFunctieIntrare - teta )) + pow(e, -alfa * ( valoareFunctieIntrare - teta )) )
            self.view.valoareFunctieActivare.set(format(valoareFunctie, '.20f'))
        
        if self.view.valoareBinar.get() == 'true':
            if self.view.tipFunctieActivare.get() == 'Sigmoidala' or self.view.tipFunctieActivare.get() == 'Treapta':
                if float(self.view.valoareFunctieActivare.get()) >0.5 :
                    self.view.valoareFunctieIesire.set('1')
                else:
                    self.view.valoareFunctieIesire.set('0')
            if self.view.tipFunctieActivare.get() == 'Tangenta' or self.view.tipFunctieActivare.get() == 'Liniara' or self.view.tipFunctieActivare.get() == 'Semn':
                if float(self.view.valoareFunctieActivare.get()) >=0 :
                    self.view.valoareFunctieIesire.set('1')
                else:
                    self.view.valoareFunctieIesire.set('-1')
        else:
            self.view.valoareFunctieIesire.set(self.view.valoareFunctieActivare.get())
        print('Am calculat')
        
    def update_numar_intrari(self, *args):
        print(self.view.intrari.get())
        print(self.view.valoareSpinBoxIntrari.get())
        print('')
        if self.view.valoareSpinBoxIntrari.get()=='':
            return None
        intrari = int(self.view.intrari.get())
        valoareSpinBoxIntrari = int(self.view.valoareSpinBoxIntrari.get())
        if valoareSpinBoxIntrari-intrari>0:
            print(valoareSpinBoxIntrari)
            print(intrari)
            for i in range(intrari, valoareSpinBoxIntrari):
                self.view.frameIntrariValori1 = ttk.Frame(self.view.frameInCanvas, relief=tk.RAISED, borderwidth=1)
                self.view.listaFrameIntrari.append(self.view.frameIntrariValori1)
                self.view.frameIntrariValori1.pack(fill=tk.X, side = tk.TOP, padx=10, pady=10)
                self.view.labelIn = tk.Label(self.view.frameIntrariValori1, text='Ini'+str(i), height=1, width=3)
                self.view.labelIn.pack(side = tk.LEFT, padx=3, pady=3)
                self.intrareValoare = tk.StringVar()
                self.view.entryIni0 = ttk.Spinbox(self.view.frameIntrariValori1, from_=-1000000, to=1000000, increment=0.01, textvariable = self.intrareValoare)
                self.intrareValoare.set('0.01')
                self.view.listaIntrariValoareInitiala.append(self.intrareValoare)
                self.view.entryIni0.pack(fill=tk.X, expand=1, side = tk.LEFT)
                self.view.labelW0 = tk.Label(self.view.frameIntrariValori1, text='Wi'+str(i), height=1, width=3)
                self.view.labelW0.pack(side = tk.LEFT, padx=3, pady=3)
                self.intrareGreutate = tk.StringVar()
                self.view.entryWi0 = ttk.Spinbox(self.view.frameIntrariValori1, from_=-1000000, to=1000000, increment=0.01, textvariable = self.intrareGreutate)
                self.intrareGreutate.set('0.01')
                self.view.listaIntrariGreutate.append(self.intrareGreutate)
                self.view.entryWi0.pack(fill=tk.X, expand=1, side = tk.LEFT)
                self.intrareValoare.trace('w', self.calculeaza)
                self.intrareGreutate.trace('w', self.calculeaza)
            self.view.CanvasIntrariValori.configure(scrollregion=self.view.CanvasIntrariValori.bbox("all"))
        elif valoareSpinBoxIntrari-intrari<0:
            for i in range(valoareSpinBoxIntrari, intrari):
                self.view.listaFrameIntrari[-1].destroy()
                self.view.listaFrameIntrari.pop()
                self.view.listaIntrariValoareInitiala.pop()
                self.view.listaIntrariGreutate.pop()
                self.listaIntrariValoriFinale.pop()
            self.view.CanvasIntrariValori.configure(scrollregion=self.view.CanvasIntrariValori.bbox("all"))
        self.calculeaza()
        
        self.view.intrari.set(self.view.valoareSpinBoxIntrari.get())