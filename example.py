#!/usr/bin/env python

import sys

import qi

from qibullet import SimulationManager
from qibullet import PepperVirtual
from NaoqibulletWrapper import NaoqibulletWrapper
    
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

# wrap qi App Session with Simulated Pepper     
wrap = NaoqibulletWrapper(qiApp, pepperSim) # /!\ keep wrap instance to keep thread

# code example : move head and move base
qiSession = qiApp.session
motionService = qiSession.service("ALMotion")  
motionService.setAngles(["HeadPitch", "HeadYaw"], [-1,-1], [1,1]) 
motionService.moveTo(1, 1, 1.57)

# block until stop is called.
qiApp.run()

# close nicely
wrap.close()