import PySimpleGUI as sg
from src.results import show_in_window

layout = [
  [
    sg.Text(
      'Clique em algum dos botões para ver as informações.',
      background_color='#1D1C2D',
      text_color='#e3e3e3',
      font='"Fira Code" 12', 
      size=(35, 0)
    )
  ],
  
  [
    sg.Text(
      key='space',
      background_color='#1D1C2D',
      size=(0, 1)
    )
  ],
  
  [
    sg.Button(
      'Confirmados',
      button_color='#9670FF',
      size=(15, 2),
      font='"Fira Code" 12'
    ),
  
    sg.Button(
      'Internações',
      key='Internados',
      button_color='#9670FF',
      size=(15, 2),
      font='"Fira Code" 12'
    )
  ],
  
  [
    sg.Button(
      'Recuperados',
      button_color='#9670FF',
      size=(15, 2),
      font='"Fira Code" 12'
    ),

    sg.Button(
      'Obitos',
      button_color='#9670FF',
      size=(15, 2),
      font='"Fira Code" 12'
    )
  ],
  
  [
    sg.Button(
      'Sair da aplicação',
      key='exit',
      button_color='#DB0109',
      size=(38, 2),
      font='"Fira Code" 12'
    )
  ],
  
  [
    sg.Text(
      'Aguarde um momento...',
      key='load',
      visible=False,
      background_color='#1D1C2D',
      size=(0, 1)
    )
  ]
]

window = sg.Window(
  'Análise de dados do COVID - Macroregiões MG',
  layout,
  background_color='#1D1C2D',
  size=(390, 300),
  location=(350, 250)
)

while True:
  valid = bool
  events, values = window.read()
  if events == sg.WINDOW_CLOSED or events == 'exit':
    break
  
  if events == 'Confirmados':
    window['load'].update(visible=True)
    window.refresh()
    show_in_window('CONFIRMADOS')
    window['load'].update(visible=False)
    
  elif events == 'Internados':
    window['load'].update(visible=True)
    window.refresh()
    show_in_window('INTERNADOS')
    window['load'].update(visible=False)
    
  elif events == 'Recuperados':
    window['load'].update(visible=True)
    window.refresh()
    show_in_window('RECUPERADOS')
    window['load'].update(visible=False)
     
  elif events == 'Obitos':
    window['load'].update(visible=True)
    window.refresh()
    show_in_window('OBITOS')
    window['load'].update(visible=False)
