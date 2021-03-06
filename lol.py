import os
import sys
import glob
	
	
def searchWindows():
	route = '/usr/'# Define la ruta de búsqueda
	files = []  # todos los archivos
	
	posibleFiles = [".a", ".so", ".bin", ".img", ".old", ".jar", ".py", ".sh", ".elf", ".dev"]
    

	  # Busqueda según extensión
	    # Abrir hoja de excel en modo de lectura
	csvFile = open(os.getcwd()+"/arqui.csv", "w")
	    # Encabezados excel
	csvFile.write("Nombre,Tamano (bytes),Valor Hexadecimal, Repeticiones\n")
	for posibleFile in posibleFiles:  # Para cada tipo de archivo(extensión)
	    for f in glob.glob(route+"**/*"+posibleFile, recursive=True):
	            # Buscar por tipo de extensión, usamos el recursive para que se iteren dentro de las carpetas (búsqueda profunda)
	        try:
	            files.append(f)  # añadir el nombre del archivo
	            opened = open(f, "rb")  # abrir en modo de lectura binaria
	            dictionary = dict()  # inicializar un nuevo dusr'ccionario para cada archivo
	            print(opened)  # imprimir archivo
	                # Leer despues de 'b que se antepone al leer en modo binario en python
	            readedFile = opened.readlines()[2:]
	            for line in readedFile:  # para cada linea
	                    # separar por valores hexadecimales
	                for char in str(line).split("\\x"):
	                    if(len(char) == 2):  # tamaño 2 para evitar códigos de xml
	                            # si el valor no está en el dictionario se añade y sus repeticiones valen 1
	                        if(char.upper() not in dictionary):
	                            dictionary[char.upper()] = 1
	                        else:  # si ya existe, se le suma 1 al valor del diccionario
	                            dictionary[char.upper(
	                           	)] = dictionary[char.upper()]+1
	                # obtener tamaño del archivo en bytes
	            size = os.path.getsize(f)
	                # guardar solo nombre.ext del archivo y el tamaño en bytes para la hoja de excel
	            csvFile.write(str(f.split("\\")[-1])+","+str(size)+"\n")
	            for key, value in dictionary.items():  # para cada llave y valor
	                try:
	                        # si se puede convertir a hexadecimal es un valor valido
	                    checkHex = int(key, 16)
	                        # guardar en la tabla
	                    csvFile.write(",,"+str(key)+","+str(value)+"\n")
	                except:
	                    pass
	            opened.close()  # cerrar archivo leído
	        except:
	            print("File probabbly not found")
	    # Not completely necessary, but if u want to print which file is being readed here u have it.
	csvFile.close()  # cerrar archivo de escritura (excel)
	
	return
	
if __name__ == "__main__":
	searchWindows()
	
	