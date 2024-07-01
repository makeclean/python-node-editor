#!/usr/env/python3

from statistics import variance
import netCDF4 as nc
import numpy as np

class ExodusReader:
    def __init__(self,filename):
        self.filename = filename
        self.side_sets = []
        self.side_count = 0
        self.block_names = []
        self.block_count = 0
    
    def read(self):    
        self.mesh = nc.Dataset(self.filename)
    
        side_names = self.mesh.variables['ss_names']
        for i in side_names:
            side_name = ''.join(np.char.decode(i))
            if side_name == "":
                self.side_count += 1
                side_name = str(self.side_count)
            self.side_sets.append(side_name)

        block_names = self.mesh.variables['eb_names']
        for i in block_names:
            block_name = ''.join(np.char.decode(i))
            if block_name == "":
                self.block_count += 1
                block_name = str(self.block_count)
            self.block_names.append(block_name)

