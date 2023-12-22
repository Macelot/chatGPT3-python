import openai
import time

# Defina sua chave de API
openai.api_key = 'sua-key'

# Marca o tempo de início
tempo_inicio = time.time()

# Faça uma chamada para o modelo
resposta = openai.Completion.create(
  engine="text-davinci-003",  # GPT-3.5 Turbo é baseado no mecanismo text-davinci-003
  prompt="Calcule o IMC, peso= 70 altura=1.75",
  max_tokens=150
)
# Exiba a resposta gerada
print(resposta.choices[0].text.strip())

# Marca o tempo de término
tempo_fim = time.time()

# calcula o tempo 
tempo_execucao = tempo_fim - tempo_inicio

# Exiba o tempo de processamento
print(f"Tempo de execução: {tempo_execucao} segundos")
