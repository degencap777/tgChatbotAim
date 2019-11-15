#!/usr/bin/python3
import os
import aiml
import logging
from config import config
logging.basicConfig(filename='info.log',level=logging.INFO)
class ChatBot:
    def __init__(self):
        BRAIN_FILE=config.getBrainFileName()
        self.k = aiml.Kernel()
        if os.path.exists(config.getBrainFileName()):
            print("Loading from brain file: " + BRAIN_FILE)
            self.k.loadBrain(BRAIN_FILE)
        else:
            print("Parsing aiml files")
            self.k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
            print("Saving brain file: " + BRAIN_FILE)
            self.k.saveBrain(BRAIN_FILE)

    def getResponseFromBot(self, input):
        logging.info("User: "+ input)
        response = self.k.respond(input)
        logging.info("Tommy: "+ response)
        return response
