# ---- Passos para o QuickSort----
# Selecionar um pivô;
# Selecionar elemento maior e menor que o pivô
# Realocar os elementos

def quicksort(lista):
  if len(lista) == 0: return lista
  # Seleção pivô
  pivo = lista[0]
  
  # Definição de elementos maior e menor que o pivô recursivamente
  frente = quicksort([menor for menor in lista[1:] if menor <= pivo])
  tras = quicksort([maior for maior in lista[1:] if maior > pivo])
  
  # Reposicionando valores
  return frente + [pivo] + tras
