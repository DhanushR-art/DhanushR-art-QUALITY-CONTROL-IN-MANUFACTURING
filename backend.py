# backend.py
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('DefectBot', read_only=True)
trainer = ChatterBotCorpusTrainer(chatbot)

# Train only once if not trained already
# trainer.train('chatterbot.corpus.english')

def get_response(message):
    return str(chatbot.get_response(message))
