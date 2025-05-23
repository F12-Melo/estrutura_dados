# inicial

Users = ['Admin', 'Admin2', 'Ryan']
Password = [1234, 4321, 1111]
realuser = int(input("Digite seu usuário: "))
realpass = int(input("Digite sua senha: "))
if realuser == Users[0] and realpass == Password[0]:
    print("Acesso Permitido")
elif realuser == Users[1] and realpass == Password[1]:
    print("Acesso Permitido")
elif realuser == Users[2] and realpass == Password[2]:
    print("Acesso Permitido")
else:
    print("Acesso Negado")

# Corrigido pela professora (depois eu usei index aqui está simulando um acerto)
Users = ['luis', 'gaby', 'maria']
Password = ['l123', 'g465', 'm998']

for i in range(3):
  inputuser = input("Digite seu usuário: ")
  inputpass = input("Digite sua senha: ")
  if inputuser not in Users or inputpass not in Password:
      print('Inseridos não estão na lista')
  elif Users.index(inputuser) == Password.index(inputpass):
      print(f'Acesso permitido\nSeja bem-vind(a), {inputuser}.')
  else:
      print('Acesso Negado')

# lista
import numpy as np
Users = np.array(['luis', 'gaby', 'maria'])
Password = np.array(['l123', 'g465', 'm998'])

for i in range(3):
  inputuser = input("Digite seu usuário: ")
  inputpass = input("Digite sua senha: ")
  if inputuser not in Users or inputpass not in Password:
      print('Inseridos não estão na lista')
  elif np.where(Users == inputuser) == np.where(Password == inputpass):
      print(f'Acesso permitido\nSeja bem-vindo(a), {inputuser}.')
      break
  else:
      print('Acesso Negado')

