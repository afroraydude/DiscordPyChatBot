import discord
import asyncio
import sys
try:
        from configparser import ConfigParser
except ImportError:
        from ConfigParser import ConfigParser  # ver. < 3.

from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer

chatbot = ChatBot('bot', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

chatbot.set_trainer(ListTrainer)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.train(conversation)

client = discord.Client()

config = ConfigParser()

config.read('config.ini')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    messageContent = message.content
    print (messageContent)

    response = chatbot.get_response(messageContent)

    await client.send_message(message.channel, response)

botToUse = sys.argv[1]

token = config.get('main', botToUse)

client.run(token)