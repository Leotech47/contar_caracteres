def contar_caracteres(string):
  """Conta a frequência de cada caractere em uma string.

  Args:
    string: A string de entrada.

  Returns:
    Um dicionário onde as chaves são os caracteres e os valores são as contagens.
  """

  contador = {}  # Inicializa um dicionário vazio para armazenar as contagens

  for caractere in string:
    if caractere in contador:
      contador[caractere] += 1  # Incrementa a contagem se o caractere já existe
    else:
      contador[caractere] = 1  # Adiciona o caractere ao dicionário com contagem 1

  return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)
