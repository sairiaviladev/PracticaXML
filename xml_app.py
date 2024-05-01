#XML
#Tag - valor - en - arbol 
#el email tiee un atributo denominado hide por ende se llama de manera diferente, en este caso con el método get
import xml.etree.ElementTree as ET

user = '''
    <datos>
        <nombre>Angel</nombre> 
        <apellido>Perez</apellido>   
        <telefono>9713493867</telefono>
        <email hide="yes" />
    </datos>
'''
xml_data = ET.fromstring(user)
#print (xml_data)

print(f"Nombre: {xml_data.find('nombre').text}")
print(f"Apellido: {xml_data.find('apellido').text}")
print(f"Teléfono: {xml_data.find('telefono').text}")
print(f"Email: {xml_data.find('email').get('hide')}") #atributo hide


    