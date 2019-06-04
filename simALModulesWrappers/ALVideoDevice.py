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


class ALVideoDeviceProxy:
    
    def __init__(self, qiSession, sim_pepper):
        print("__init__ in ALVideoDevice")

        self.sim_pepper = sim_pepper  


    def subscribeCamera(self, name, camIndex, res, colorsSpace, fps):
        self.sim_pepper.subscribeCamera(camIndex, res)


    def getImageRemote(self, suscriberID_handle):
        img = self.sim_pepper.getCameraFrame()

        #TODO: reverse algo of https://gist.github.com/takamin/990aa0133919aa58944d

        return img

