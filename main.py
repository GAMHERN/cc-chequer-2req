from stripe import *
import requests
import pyfiglet
name = pyfiglet.figlet_format(" CHECKER  2REQ ")
print(name)
print('Escrito por @GAMHERN')
print(' ')
print('Formato de las tarjetas')
print('421316xxxxxxxxxx|00|00|000')
print(' ')

filename = input("Introduzaca el nombre del archivo: ")

try:
    ccs = open(filename)

except:
    print( "No se encontro el archivo" + filename )
    print(' ')
    print('1 Error encontrado')

readcc = ccs.readlines()
print(' ')
print(str(len(readcc)) + ' CCs Encontradas')
print(' ')
print(' Chequeo iniciado ')
print(' ')

head1={
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Pragma':'no-cache',
	'Accept':'*/*',
	}
response1 = requests.get('https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US',headers=head1).json()
for x in response1['results']:
	print('[*] Recopilando Informacion')
name=x['name']['first']
second=x['name']['last']
ciudad=x['location']['city']
estado=x['location']['state']
pais=x['location']['country']
codigo_postal=x['location']['postcode']
email=(name+second+'98109@gmail.com').lower()
fullname=name+' '+second
print(' ')
print('[*] ' + 'Nombre: ' +name + ' √')
print(' ')
print('[*] ' + 'Apellido: ' +second + ' √')
print(' ')
print('[*] ' + 'Email: ' +email + ' √')
print(' ')
print('[*] ' + 'Nombre Completo: ' +fullname + ' √')
print(' ')
print('[*] Ciudad: ' + ciudad + ' √')
print(' ')
print('[*] Estado: ' +estado + ' √')
print(' ')
print('[*] Pais: ' +pais + ' √')
print(' ')

def checks():
    x = 0
    for i in readcc:
        main(i)
        x += 1
    print(' ')
    print(str(x)+' Chequeo completado ' + 'No hay errores econtrados')
    print(' ')

checks()
ccs.close()






