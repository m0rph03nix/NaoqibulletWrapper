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
import numpy as np

class ALVideoDeviceProxy:
    
    def __init__(self, qiSession, sim_pepper):
        print("__init__ in ALVideoDevice")

        self.sim_pepper = sim_pepper  


    def subscribeCamera(self, name, camIndex, res, colorsSpace, fps):
        handle = self.sim_pepper.subscribeCamera(res)
        return handle


    def getImageRemote(self, suscriberID_handle):
        print("start")
        Frames = []
        img = self.sim_pepper.getCameraFrame()
        size = img.shape
        height = size[1]
        width = size[0]
        image = np.zeros((height, width, 3), np.uint8)
        #values = map(chr, list(img))
        #i = 0
        #for y in range(0, height):
        #    for x in range(0, width):
        #        image.itemset((y, x, 0), values[i + 0])
        #        image.itemset((y, x, 1), values[i + 1])
        #        image.itemset((y, x, 2), values[i + 2])
        #        i += 3

        t_usec = qi.clockNow()/1000
        CamId = self.sim_pepper.getCameraLink()
        
        Frames.append(width)
        Frames.append(height)
        Frames.append(2)
        Frames.append("kYUV422ColorSpace")
        Frames.append(t_usec / 1000000)
        Frames.append(t_usec % 1000000)
        Frames.append(img)
        Frames.append(CamId)
        Frames.append(-0.4712389)
        Frames.append(0.38397244)
        Frames.append(0.4712389)
        Frames.append(-0.38397244)

        print(Frames)
        return Frames

