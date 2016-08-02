# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 01:08:41 2016

@author: Chris
"""

# Bitbang'd SPI interface with an MCP3008 ADC device
# connections are
# CLK --> SCLK
# DOUT --> MISO
# DIN --> MOSI
# CS --> CEO

import time
import sys
import spidev