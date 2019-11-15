#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Suhas More
# Email: moresuhas010@gmail.com
# Twitter: @suhas0101

import os
import logging
import telegram
from config import config
from handlers import custome
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def getBot():
    return telegram.Bot(token=config.getBotToken())

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def start():
    """Start the bot."""
    updater = Updater(config.getBotToken(), use_context=True)

    dispatcher = updater.dispatcher

    customeHandlers = custome.CusotmeHandlers()

    # custome command handlers
    dispatcher.add_handler(CommandHandler("howsthejosh", customeHandlers.josh))
    
    # Set and Unset Timer
    dispatcher.add_handler(CommandHandler("settimer", customeHandlers.setTimer, pass_args=True, pass_job_queue=True, pass_chat_data=True))
    dispatcher.add_handler(CommandHandler("resettimer", customeHandlers.unsetTimer, pass_chat_data=True))

    # cummunicate with aiml bot
    dispatcher.add_handler(MessageHandler(Filters.text, customeHandlers.default))

    # log all errors if any
    dispatcher.add_error_handler(error)

    # Start
    updater.start_polling()

    updater.idle()

