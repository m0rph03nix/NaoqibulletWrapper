#!/usr/bin/env python

__author__ = 'Florian DUPUIS'

import pyttsx3
import time

class ALAnimatedSpeechProxy:

    def __init__(self, qiSession, sim_pepper):
        print("__init__ in ALAnimatedSpeechProxy")

        self.sim_pepper = sim_pepper  
        self.sentence = ['Hello my name is Pepper']

    def afficher_nationalites(self):
        voices = engine.getProperty('voices')
        nationalites = []
        for voice in voices :
            nationalites.append(voice.name)
        print'Nationalities available: \n', nationalites
        return

    def gender_selection(self):
        nation = raw_input('\n Wich Nationality ?: ')
        voices = engine.getProperty('voices')
        voix = ""
        while(voix == ""):
            compteur = 0
            for voice in voices :
                compteur += 1
                if (nation == voice.name):
                    voix = voice
                    compteur -= 1
            if compteur == 69:
                afficher_nationalites()
                nation = raw_input('\n We couldn\'t find your language, please choose one in the list above: ')
        engine.setProperty('voice', voix.id)
        return

    def setSetences(self):
        new_sentence = raw_input("\n Give a sentence for the pepper to say or press q to exit: ")
        while(new_sentence !="q" and new_sentence != "Q"):
            self.sentences.append(new_sentence)
            new_sentence = raw_input("Give a new sentence ou press q to exit:  ")
        return

    def dire_phrases(self):
        for phrase in self.sentences:
            engine.say(phrase)
            time.sleep(2)
        return
