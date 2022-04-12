import json
import pyttsx3
from random_word import RandomWords
from datetime import date
 
class Speech:
    def text2Speech(self, audio):
        # Having the initial constructor of pyttsx3 
        # and having the sapi5 in it as a parameter
        engine = pyttsx3.init('sapi5')

        # Calling the getter and setter of pyttsx3
        voices = engine.getProperty('voices')

        # Method for the speaking of the assistant
        engine.setProperty('voice', voices[0].id)
        # Method to set the rate of speech
        engine.setProperty("rate", 148)
        engine.say(audio)
        engine.runAndWait()

class Vocab:
    def wordOfDay(self, word, meaning):
        s = Speech()
        print("\nWord of the day is " + "'" + word + "'.")
        print("The meaning of the word " + word + " is: {" + meaning + "}\n\n")
        audio1 = "Word of the day is " + word
        s.text2Speech(audio1)
        audio2 = "It means " + meaning
        s.text2Speech(audio2)

if __name__ == '__main__':
    today = date.today()
    r = RandomWords()
    dic = r.word_of_the_day(date=str(today))
    dic = json.loads(dic)
    word = dic["word"]
    lst = dic["definations"]
    meaning = lst[0]['text']
    V = Vocab()
    V.wordOfDay(word, meaning)