from os import system
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from listaM import *
from ORG import *
from celda import *

class Menu:

    muestraAnalizada:Muestra

    def __init__(self) -> None:
        self.opciones=[
            'Abrir muestra',
            'Graficar muestra',
            'Procesar Organismo',
            '----',
            '----',
            'Acerca de',
            'Salir'
        ]

    def mostrar(self,error:bool) -> None:
        system("cls")
        
        print('        ****************************           ')
        print('        *         IPC2 D           *          ')
        print('        *        Proyecto 1        *          ')
        print('        *        Analisis          *          ')
        print('        ****************************          \n')

        i = 0

        
        for opcion in self.opciones:
            i = i + 1
            print("\t",i," - "+opcion)
        
        if(error):
            print('\n            OPCION INCORRECTA!!               ')

        opcion = input('\nEscribe tu opcion: ')
        self.ejecutarOpcion(opcion)
        
    
    def pausa(self):
        espera = input('Presiona cualquier tecla para continuar...\n')     
        self.mostrar(False)

    def ejecutarOpcion(self,opcion:str) -> None:
        if(opcion=='1'):
            filename = askopenfilename()
            objetoXml = minidom.parse(filename)
            self.procesarInformacion(objetoXml)
            self.pausa()
        elif(opcion=='2'):
            self.graficarMuestra()
            self.pausa()
        elif(opcion=='3'):
            self.graficarMuestra()
            self.pausa()    
        elif(opcion=='6'):
                print("USAC")
                print("Facultad de Ingeniería")
                print("Henry Alexnder García Montúfar")
                print("201407049")
                print("IPC 2 D")
                self.pausa()  
        elif(opcion=='7'):
            exit()
            self.pausa()
             
        else:
            self.mostrar()

    def procesarInformacion(self, objetoXML):
 
        coleccionX  = objetoXML.getElementsByTagName('columnas')
        coleccionY  = objetoXML.getElementsByTagName('filas')
        muestra     = objetoXML.getElementsByTagName('muestra')

        codigoMuestra       = muestra[0].childNodes[1].firstChild.data 
        descripcionMuestra  = muestra[0].childNodes[3].firstChild.data 

        dimensionX = coleccionX[0].childNodes[0].data
        dimensionY = coleccionY[0].childNodes[0].data

        nuevaMuestra  =  Muestra(codigoMuestra,descripcionMuestra,dimensionX,dimensionY)

        organismosXML = objetoXML.getElementsByTagName('organismo')

        letra = 65
        for organismo in organismosXML:

            codigo = organismo.childNodes[1].firstChild.data
            nombre = organismo.childNodes[3].firstChild.data
            nuevoOrganismo = Organismo(codigo,nombre,letra)
            nuevaMuestra.listaOrganismos.agregar_al_inicio(nuevoOrganismo)
            letra = letra + 1

        celdasVivasXML = objetoXML.getElementsByTagName('celdaViva')

        for celdaViva in celdasVivasXML:

            fila            = celdaViva.childNodes[1].firstChild.data
            columna         = celdaViva.childNodes[3].firstChild.data
            codigoOrganismo = celdaViva.childNodes[5].firstChild.data

            nuevaCeldaViva  = CeldaViva(codigoOrganismo,columna,fila)

            nuevaMuestra.listaCeldasVivas.agregar_al_inicio(nuevaCeldaViva)

        self.muestraAnalizada = nuevaMuestra

    

    def graficarMuestra(self):
        
        x   = self.muestraAnalizada.dimensionX
        y   = self.muestraAnalizada.dimensionY

        codigoGraphiz = """
            digraph structs {
                node [shape=record];
                MATRIZ [
                    label="
                    
        """
        cuentaX = -1
        cuentaY = -1
        while (cuentaX < int(x)):
            if(cuentaY == -1):
                codigoGraphiz=codigoGraphiz+'{x,y'
            else:
                codigoGraphiz=codigoGraphiz+'{'+str(cuentaX)
            
            cuentaY = 0
            
            while (cuentaY < int(y)):
                
                if(cuentaX == -1):
                    codigoGraphiz=codigoGraphiz+'|'+str(cuentaY)
                else:
                    listaCeldasVivas  = self.muestraAnalizada.listaCeldasVivas
                    nodoActual = listaCeldasVivas.cabeza

                    codigoOrganismo = ""
                    while nodoActual != None:
                       
                        celdaViva:CeldaViva = nodoActual.dato
                        coordenadaX = celdaViva.x
                        coordenadaY = celdaViva.y
                        
                        if (int(cuentaX)==int(coordenadaX) and int(cuentaY) == int(coordenadaY)):
                            
                            inicio = self.muestraAnalizada.listaOrganismos.cabeza
                            while(inicio!=None):
                                organismo:Organismo = inicio.dato
                                
                                if(celdaViva.organismo==organismo.codigo):
                                    codigoOrganismo='|'+chr(organismo.letra)
                                    break
                                inicio=inicio.siguiente
                            break
                        else:
                            codigoOrganismo='|'
                        nodoActual = nodoActual.siguiente

                    codigoGraphiz = codigoGraphiz + codigoOrganismo
                cuentaY = cuentaY + 1
                
            cuentaX = cuentaX + 1
            
            if(cuentaX == int(x)):
                codigoGraphiz=codigoGraphiz+'}'
            else:
                codigoGraphiz=codigoGraphiz+'}|'

        codigoGraphiz =codigoGraphiz+ """
                        "];
        """
        inicio = self.muestraAnalizada.listaOrganismos.cabeza
        codigoGraphiz =codigoGraphiz+"\""
        while(inicio!=None):
            organismo:Organismo = inicio.dato
            codigoGraphiz =codigoGraphiz +chr(organismo.letra)+"-"+organismo.codigo+"\n"
            inicio=inicio.siguiente
        codigoGraphiz =codigoGraphiz+ """
                        \"}     
        """
        archivo = open("./img/muestra.txt","w")
        archivo.write(codigoGraphiz)
        print("Creando imagen...")
        system("\"C:\\Users\\Alex\\Desktop\\Proyecto 1 IPC2\\IPC2_Proyecto1-201407049\\img\\generarImagen.bat\"")

