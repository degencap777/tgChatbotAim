import os
def getBotToken():
    return os.environ["CHATBOTID"]
    
def getChatId():
    return os.environ["CHATID"]
    
def getBrainFileName():
    return "brain.dump"