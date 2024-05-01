#XML desde archivo 
import xml.etree.ElementTree as ET #importamos el módulo que nos permite manipular el archivo XML

#Creamos un bloque try/except/finally
try:
    #abrimos el documento XML con OPEN
    xml_file = open('plants.xml') 
    #este read justo después de la apertura, nos sirve para leer toda la estructura del XML
    #print(xml_file.read())
    #corroboramos que el archivo se pueda leer, si es así imprimimos TRUE de lo contrario imprimimos FALSE 
    if xml_file.readable(): 
        #print(True)
        #almacenamos los datos en una variable y con .read podremos leer el archivo y nos arrojará el elemento CATALOG
        #ya que ese es el elemento que contiene este documento como estructura principal
        xml_data = ET.fromstring(xml_file.read()) 
        lst_plants = xml_data.findall('PLANT') #con este método FINDALL estamos mandando a llamar todos los elementos PLANT y contarlos
        for plant in lst_plants:
            print(f"Nombre: {plant.find('COMMON').text}")
            print(f"Nombre Botánico: {plant.find('BOTANICAL').text}")
            print(f"Zona: {plant.find('ZONE').text}")
            print(f"Tipo de luz: {plant.find('LIGHT').text}")
            print(f"Precio: {plant.find('PRICE').text}")
            print(f"Disponibilidad: {plant.find('AVAILABILITY').text}")
            
        #print(xml_data)
    else: 
        print(False)
#exception para tomar cualquier error
except Exception as err:
    #visualizamos cualquier error en terminal con el print 
    print("Error: ", err) 
    pass
finally:
    xml_file.close() 

