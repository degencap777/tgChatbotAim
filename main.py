#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Author: Suhas R More
# Email: iam@suhasmore.in
# Twitter: @suhas0101

from tel import telegrambot
from chatbot import chatbot


def intialiseAimlChatbot():
    aimlChatBot = chatbot.ChatBot()

def main():
    intialiseAimlChatbot()
    telegrambot.start()

if __name__ == '__main__':
    main()
