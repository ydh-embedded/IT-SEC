from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


#SECTION - TOKEN

TOKEN Final ='7493318142:AAGp9nDF9QD-VAFdZIxMJe5uzXHoiahdZoM' 
BOT_USERNAME: Final = '@SecReport_Bot'









#SECTION - Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Thanks for chatting with me! I am a banana!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a banana! Please type something so I want to response!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a costum command!')
    
    
    
    
    
    
    
    
    
#SECTION - Response

def handle_response(text: str) = str:
        processed: str = text.lower()
        
        if 'hello' in processed:
            return 'Hey there!'
        
        if 'how are you' in processed:
            return 'I am good!'
        
        if 'i love python' in processed:
            return 'Remember to subscribe!'
        
        return 'I od not understand what yu type in - please repeat'
    
        async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        
         message_type: str = update.message.chat.type
         text: str = update.message.text
        
        print(f'User({update.message.chat.id}) in {message_type}: "{text}"')
        
        if message_type == 'group':
            if BOT_USERNAME in text:
                new_text: str = text.replace(BOT_USERNAME , '' ).strip()
                response: str = handle_response(new_text)
            else:
                return
        else: 
            response: str = handle_response(text)
            
        print ('Bot:' , response )
        await update.message.reply_text(response)
        
        async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
            print(f'Update {update} caused error {context.error}')
            