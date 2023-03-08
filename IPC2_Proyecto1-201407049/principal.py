from os import system, startfile
import xml.etree.ElementTree as ET
from xml.dom import minidom
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from celda import *
from listaM import *  
from ORG import *  

class Organismo:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre


class muestra:
    def __init__(self, codigo, descripcion, filas, columnas): 
        self.codigo = codigo
        self.descripcion = descripcion
        self.filas = filas
        self.columnas = columnas 

class celdaViva:
    def _init_(self,  fila, columnas, codigoOrganismo):
        self.fila = fila
        self.columnas = columnas
        self.codigoOrganismo = codigoOrganismo


class Nodo():
    
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class Lista_simple(): 
    def __init__(self):
        self.cabeza = None
    
    
    def agregar_al_inicio(self, dato):
        self.cabeza = Nodo(dato=dato, siguiente=self.cabeza)


class List:
    def __init__(self):
        self.first = None

    def insert(self, Organismo):
        if self.first is None:  
            self.first = Nodo(Organismo=Organismo)
            return
        actual = self.first
        while actual.next_position:  
            actual = actual.next_position
        actual.next_position = Nodo(Organismo=Organismo)

    def run(self):
        actual = self.first
        while actual is not None:
            print("|listaOrganismos:", actual.Organismo.name, "|Organismo:", actual.Organismo.age, "|Tamaño:", actual.Organismo.size)
            actual = actual.next_position

    def delete(self, name):
        actual = self.first
        previous = None

        while actual and actual.Organismo.name != name:
            previous = actual
            actual = actual.next_position

        if previous is None:
            self.first = actual.next_position
            actual.next_position = None
        elif actual:
            previous.next_position = actual.next_position
            actual.next_position = None

    def search(self, name):
        actual = self.first

        while actual and actual.Organismo.name != name:
            actual = actual.next_position
        print("|listaOrganismos:", actual.Organismo.name, "|Organismo:", actual.Organismo.age, "|Tamaño:", actual.Organismo.size)


def grafica():
    graphviz = """
    digraph myGraph{
    Nodo[shape=box fillcolor="#FFEDBB" style=filled]
    subgraph cluster_p{
        label = "Matriz Dispersa"
        bgcolor = "#398D9C"
        edge[dir = "none"]
        /*Here we start creating the columns.
        color = "#398D9C" style=invisible
        */
        Row1[label="r1"]
        Row2[label="r2"]
        Row3[label="r3"]
        Row4[label="r4"]
        Row5[label="r5"]
        Row6[label="r6"]
        Row7[label="r7"]

        Row1 -> Row2;


        Fila1[label="1", group=1];
        Fila2[label="2", group=2];
        Fila3[label="3", group=3];
        Fila4[label="4", group=4];
        Fila5[label="5", group=5];
        /*Linkin the Nodos*/
        Fila1 -> Fila2;
        Fila2 -> Fila3;
        Fila3 -> Fila4;
        Fila4 -> Fila5;
        /*Enlazando los nodos de las filas.*/
        Columna1[label = "1", group = 2, fillcolor=yellow]
        Columna2[label = "2", group = 3, fillcolor=yellow]
        Columna3[label = "3", group = 4, fillcolor=yellow]
        Columna4[label = "4", group = 5, fillcolor=yellow]
        Columna5[label = "5", group = 6, fillcolor=yellow]
        /*Enlazando los nodos de las columnas.*/
        Columna1 -> Columna2
        Columna2 -> Columna3
        Columna3 -> Columna4
        Columna4 -> Columna5
    }
}  
    """
    my_file = open("graphviz.dot", "w")
    my_file.write(graphviz)
    my_file.close()

    system("dot -Tpng graphviz.dot -o graphviz.png")  
    startfile("graphviz.png")

def lecturaXML():
    contRows = 0
    contCols = 0
    contMR = 0
    contMF = 0
    fil = 0
    col =0
    fic = 0
    coc = 0
    CodOrg = 0
    
    opendoc = filedialog.askopenfilename(title = "Select",filetypes = ((".xml Files",".xml"),))
    #file_xml=open(opendoc,"r+")
    doc = minidom.parse(opendoc)
        #file_xml = open("Example.xml")
    datosMarte = doc.getElementsByTagName("datosMarte")
    for datosMarte in datosMarte:
        listaOrganismos = datosMarte.getElementsByTagName('listaOrganismos')
        for listaOrganismos in listaOrganismos:
            Organismo = listaOrganismos.getElementsByTagName('organismo')
            for Organismo in Organismo:
                codigo = Organismo.getElementsByTagName('codigo')
                nombre  = Organismo.getElementsByTagName('nombre')

                contRows= str(codigo[0].firstChild.nodeValue)
                contCols= str(nombre[0].firstChild.nodeValue)

                print(str(contRows))
                print(str(contCols))

        
        listadoMuestras = datosMarte.getElementsByTagName('listadoMuestras')
        for listadoMuestras in listadoMuestras:
            muestra = listadoMuestras.getElementsByTagName('muestra')
            for muestra in muestra:
                codigom = muestra.getElementsByTagName('codigo')
                descripcion = muestra.getElementsByTagName('descripcion')
                filas = muestra.getElementsByTagName('filas')
                columnas = muestra.getElementsByTagName('columnas')

                celdaViva = muestra.getElementsByTagName('celdaViva')
                for celdaViva in celdaViva:
                    filaC = celdaViva.getElementsByTagName('fila')
                    coumnac = celdaViva.getElementsByTagName('columna')
                    codigoOrganismo = celdaViva.getElementsByTagName('codigoOrganismo')
                


                contMR= str(codigom[0].firstChild.nodeValue)
                contMF= str(descripcion[0].firstChild.nodeValue)
                fil= str(filas[0].firstChild.nodeValue)
                col= str(columnas[0].firstChild.nodeValue)
                fic = str(columnas[0].firstChild.nodeValue)
                coc = str(columnas[0].firstChild.nodeValue)
                CodOrg = str(columnas[0].firstChild.nodeValue)


                print(str(contMR))
                print(str(contMF))
                print(str(fil))
                print(str(col))
                print(str(fic))
                print(str(coc))
                print(str(CodOrg))

    
        

def generarXML():
        root = ET.Element('datosMarte')
        listOrg = ET.SubElement(root,'listaOrganismos')

        currentO = Organismo.nombre 
        while currentO:
            organism = ET.SubElement(listOrg,'organismo')
            ET.SubElement(organism,'codigo').text=f'{currentO.Organismo.codigo}'
            ET.SubElement(organism,'nombre').text=f'{currentO.Organismo.nombre}'
            currentO = currentO.next_position

        listSamp = ET.SubElement(root,'listadoMuestras')
        Samp = ET.SubElement(listSamp,'muestra')
        ET.SubElement(Samp,'codigo').text
        ET.SubElement(Samp,'descripcion').text
        row = ET.SubElement(Samp,'Filas')
        column = ET.SubElement(Samp,'columnas')
        listLiveCell = ET.SubElement(Samp,'listadoCeldasVivas')









##lecturaXML()
