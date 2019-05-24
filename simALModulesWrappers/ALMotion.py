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


import qi


class ALMotionProxy:
    
    def __init__(self, sim_pepper):
        print("__init__ in ALMotionProxy")

        self.sim_pepper = sim_pepper  


    def move(self, x, y, theta):
        self.sim_pepper.move(x, y, theta)

    def moveTo(self, x, y, theta):
        self.sim_pepper.moveTo(x, y, theta)        

    def setAngles(self, joint_names, joint_values, percentage_speed):
        self.sim_pepper.setAngles(joint_names, joint_values, percentage_speed)         

    def getAngles(self, joint_names, useSensors):
        return self.sim_pepper.getAnglesPosition( joint_names )		

    def isRunning(self):
        return True    

