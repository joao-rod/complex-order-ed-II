from os import system

from src.menu import get_menu
from src.click_button_enter import click_enter
from src.results import response

while True:
  option = get_menu()
  
  if option == '1':
    system('clear')
    response('CONFIRMADOS')
    click_enter()
  elif option == '2':
    system('clear')
    response('INTERNADOS')
    click_enter()
  elif option == '3':
    system('clear')
    response('RECUPERADOS')
    click_enter()
  elif option == '4':
    system('clear')
    response('OBITOS')
    click_enter()
  elif option == '5':
    click_enter()
    break
  else:
    print('Valor inválido...')
    click_enter()
  