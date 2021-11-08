import PySimpleGUI as sg

from src._open import open_file
from src.order import quicksort

# Obtém a lista de macro-regiões
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def get_macro_regioes(data):
  lista_regioes = []
  for row in data:
    lista_regioes.append(row[-1])
  # Elimina duplicatas
  macro_regioes = list(dict.fromkeys(lista_regioes))
  
  return macro_regioes
    
    
# Faz o somatório de cada uma das macro-regiões
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def get_values(data):
  dados = {}
  macro_regioes = get_macro_regioes(data)
  for line in macro_regioes:
    total_casos = 0
    for row in data:
      if row[-1] == line.upper():
        total_casos += int(row[1])
    dados.update({line: total_casos})
    
  return dados


# Retorna os dados organizados em tela ao usuário
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def response(filename):
  values = []
  results = []
  
  # Abertura dos arquivos e processamento dos dados
  data = get_values(open_file(filename))
  for value in data.values():
    values.append(value)
  result = quicksort(values)

  # Organização dos dados em tela
  for i in range(len(result) - 1, -1, -1):
    for key in data.keys():
      if data[key] == result[i]:
        
        # OBS: Nos arquivos csv há uma linha de cabeçalho
        # Ao salvar os dados como dicionário, o valor do cabeçalho também é salvo
        # O próximo escopo ignora essa linha ao mostrar os dados ao usuário
        if key == 'Macro':
          continue
        # Em alguns arquivos csv há campos de macroregião sem preenchimento
        # O próximo escopo trata esse erro mostrando uma mensagem alternativa
        if key == '':
          results.append(['MACROREGIÃO NÃO REGISTRADA', data[key]])
          continue
        results.append([key, data[key]])

  return results


def show_in_window(request_filename):
  # Formatação dos dados para a interface gráfica
  def format_data(data):
    datas = []
    for i in range(len(data)):
      datas.append(f'{i + 1}º - {data[i][0]} com {data[i][1]} casos.')
    return '\n'.join(datas)
  
  data = response(request_filename)
  layout = [
    [
      sg.Text(
        f'Índices organizados do maior ao menor numero de casos de COVID por macroregião:\n\n{request_filename}',
        background_color='#1D1C2D',
        text_color='#e3e3e3',
        font='"Fira Code" 12', 
        size=(50, 0)
      )
    ],
    
    [
      sg.Text(
        f'{format_data(data)}',
        background_color='#1D1C2D',
        text_color='#e3e3e3',
        font='"Fira Code" 12', 
        size=(60, 0)
      )
    ]
  ]
    
  window = sg.Window(
    f'Casos {request_filename} por Macro-região',
    layout, 
    background_color='#1D1C2D',
    size=(540, 430),
    location=(735, 50)
  )

  while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
      break