import openai

# Configuração da chave de API
openai.api_key = "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"

# Pergunta do usuário
pergunta = input("Digite sua pergunta: ")

# Faz a solicitação à API do OpenAI
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=pergunta,
    max_tokens=100,
    temperature=0.7,
    n=1,
    stop=None
)

# Obtém a resposta da API
resposta = response.choices[0].text.strip()

print("Resposta:", resposta)
