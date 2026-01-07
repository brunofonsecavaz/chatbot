from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer # cria um treinador de lista

chatbot = ChatBot('BotBruno')  # cria o chatbot com o nome BotBruno

# treinando o chatbot com uma conversa simples
conversa = [ 
    "Oi",
    "Olá, tudo bem?",
    "Tudo sim, e você?",
    "Também estou bem, obrigado por perguntar!",
    "Qual é o seu nome?",
    "Meu nome é BotBruno!",
    "Prazer em te conhecer, BotBruno.",
    "O prazer é meu!"
]

trainer = ListTrainer(chatbot) # cria o treinador de lista
trainer.train(conversa) # treina o chatbot com a conversa definida acima

print("Converse com o BotBruno (digite 'sair' para encerrar):")
while True:
    entrada = input("Você: ")
    if entrada.strip().lower() in ('sair', 'exit', 'quit'): 
        print("Até mais!")
        break

    resposta = chatbot.get_response(entrada) # obtém a resposta do chatbot para responder o usuário
    print("BotBruno:", resposta) # resposta para o usuario