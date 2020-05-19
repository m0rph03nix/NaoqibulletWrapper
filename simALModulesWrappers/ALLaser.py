#!/usr/bin/env python

__author__ = 'Florian DUPUIS'


class ALLaserProxy:

    def __init__(self, qiSession, sim_pepper):
        print("__init__ in ALLaser")

        self.sim_pepper = sim_pepper  

    def laserON(self):
        self.sim_pepper.subscribe()

    def laserOFF(self):
        self.sim_pepper.unsubscribe()