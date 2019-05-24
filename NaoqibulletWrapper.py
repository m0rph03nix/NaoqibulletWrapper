#!/usr/bin/env python

__author__ =        'Raphael LEBER'
__copyright__ = """

    Copyright 2019, CPE Lyon, Raphael LEBER

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License."""
    
__license__ =       'Apache 2.0'
__maintainer__ =    'Raphael LEBER'

# http://sametmax.com/creer-un-setup-py-et-mettre-sa-bibliotheque-python-en-ligne-sur-pypi/

import sys
import threading
from time import sleep
import naoqi as n
import numpy as np

import qi

from qibullet import SimulationManager
from qibullet import PepperVirtual

from simALModulesWrappers.ALMotion import ALMotionProxy
from simALModulesWrappers.ALPosture import ALPostureProxy




def debug(msg):
    print(msg)



class NaoqibulletWrapper:
    def __init__(self, qiApp, pepperSim):

        qiApp.start()
        sensorThread = SensorThread(qiApp, pepperSim)

        session = qiApp.session

        # Exit ALMotion Service
        
        #if(motionService.isRunning):
        try:
            motionService = session.service("ALMotion")
            motionService.stop()
            motionService.exit() # NOTE : Makes an exception but works !!!
        except RuntimeError:
            pass

        # Exit ALPosture Service
        
        #if(postureService.isRunning):
        try:
            postureService = session.service("ALPosture")
            postureService.stop()
            postureService.exit() # NOTE : Makes an exception but works !!!
        except RuntimeError:
            pass                

        #sleep(2)

        # Register service ALMotion
        simMotionService = ALMotionProxy(pepperSim)
        session.registerService("ALMotion", simMotionService)
        debug("Starting ALMotion")

        # Register service ALPosture
        simPostureService = ALPostureProxy(pepperSim)
        session.registerService("ALPosture", simPostureService)
        debug("Starting ALPosture")

        # Start sensor thread
        sensorThread.start()


        qiApp.run()

        sensorThread.join()


        debug("NaoqibulletWrapper init done")



class SensorThread(threading.Thread):
    def __init__(self, qiApp, pepperSim):
        threading.Thread.__init__(self)
        self.qiSession = qiApp.session
        self.pepper = pepperSim
    
    def run(self):

        almemService = self.qiSession.service("ALMemory")
        motionService = self.qiSession.service("ALMotion")

        while( motionService.isRunning() ):
            frontLaser = self.pepper.getFrontLaserValue()
            rightLaser = self.pepper.getRightLaserValue()
            leftLaser = self.pepper.getLeftLaserValue()
            #print frontLaser

            #TODO : Convertion
            # https://github.com/ros-naoqi/naoqi_driver/blob/d12752d0025ec90b3de81bcf9f393a7f01ebe480/src/converters/laser.cpp
            # A partir de la ligne 165. Faire le reverse !

            almemService.insertData("test", 1)

            sleep(0.1)
        
        #TODO: Loop to write sensor data into ALMemory

        debug("SensorThread exiting")






if __name__ == '__main__':

    # qi App Session
    qiApp = qi.Application(sys.argv)  

    # Bullet Simulator
    simulation_manager = SimulationManager()
    client_id = simulation_manager.launchSimulation(gui=True)
    pepperSim = simulation_manager.spawnPepper(
        client_id,
        translation = [0, 0, 0],
        quaternion = [0, 0, 0, 1],
        spawn_ground_plane = True)        
    
    NaoqibulletWrapper(qiApp, pepperSim)
