# Get toke from the environment variable
import os
from telegram import Bot
token = os.getenv("TOKEN")

bot = Bot(token)
CHAT_ID = "988528730"


file_path = 'audio.ogg'
response = bot.send_audio(CHAT_ID, file_path)
print(response)

"""
file_path = 'audio.mp3'
response = bot.send_audio(CHAT_ID, file_path)
print(response)

file_path = 'video.mp4'
response = bot.send_video(CHAT_ID, file_path)
print(response)

file_path = 'logo.png'
response = bot.send_photo(CHAT_ID, file_path)
print(response)

file_path = 'document.docx'
response = bot.send_document(CHAT_ID, file_path)
print(response)

"""

