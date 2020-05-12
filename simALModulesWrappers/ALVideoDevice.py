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
        self.sim_pepper.subscribeCamera(camIndex, res)
        


    def getImageRemote(self, suscriberID_handle):
        Frames = []
        image = np.zeros((height, width, 3), np.uint8)
        img = self.sim_pepper.getFrame()
        size = img.shape
        height = size[0]
        width = size[1]
        values = map(chr, list(img))
        i = 0
        for y in range(0, height):
            for x in range(0, width):
                image.itemset((y, x, 0), values[i + 0])
                image.itemset((y, x, 1), values[i + 1])
                image.itemset((y, x, 2), values[i + 2])
                i += 3

        t_usec = qi.clockNow()/1000
        CamId = self.sim_pepper.getCameraId()
        
        Frames[0][0] = width
        Frames[0][1] = height
        Frames[0][2] = 2
        Frames[0][3] = "kYUV422ColorSpace"
        Frames[0][4] = t_usec / 1000000
        Frames[0][5] = t_usec % 1000000
        Frames[0][6] = image
        Frames[0][7] = CamId
        Frames[0][8] = -0,4712389
        Frames[0][9] = 0,38397244
        Frames[0][10] = 0,4712389
        Frames[0][11] = -0,38397244

        return Frames

