from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


ButtonBack = KeyboardButton('🔙 Головне меню')
# Main Menu
ButtonEntryInformation = KeyboardButton('🪡 Ввести параметри тіла')
ButtonWievLinks = ('🧷 Посилання')
MainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(ButtonEntryInformation, ButtonWievLinks)
# Requests customer information

# Links Menu
ButtonWievInsta = ('📷 Instagram')
ButtonWievTikTok = ('📺 TikTok')
LinksMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(ButtonWievInsta, ButtonWievTikTok, ButtonBack)