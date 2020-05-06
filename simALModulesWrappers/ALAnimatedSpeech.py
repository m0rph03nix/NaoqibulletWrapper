#!/usr/bin/env python

__author__ = 'Florian DUPUIS'


class ALAnimatedSpeechProxy:

    def __init__(self, qiSession, sim_pepper):
        print("__init__ in ALAnimatedSpeechProxy")

        self.sim_pepper = sim_pepper  

    def say(self, text):
