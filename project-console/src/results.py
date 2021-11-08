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
  # print(dados)
    
  return dados


# Retorna os dados organizados em tela ao usuário
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def response(filename):
  values = []
  print('Aguarde um momento...')
  
  # Abertura dos arquivos e processamento dos dados
  data = get_values(open_file(filename))
  for value in data.values():
    values.append(value)
  result = quicksort(values)

  # Organização dos dados em tela
  print(f'\n\nÍndices organizados do maior ao menor numero de casos de {filename} por macroregião\n')
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
          print(f'MACROREGIÃO NÃO REGISTRADA!! Mas conta com {data[key]} casos')
          continue
        # Impressão de todos os dados em tela
        print(f'{key} com {data[key]} casos')