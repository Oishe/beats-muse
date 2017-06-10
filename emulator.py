#!/usr/bin/python
# This is a muse emulator
# outputs 4 channels of sine waves at 220Hz
# takes one argument as port number
import liblo, sys, time
import numpy as np

# Starts the server
# using udp connection
# default port 1234

# Takes first arguement as port
try:
    if (sys.argv[1] > 1024):
        port = sys.argv[1]
except IndexError:
    port = 1234

# Establishes conection to the port
try:
    target = liblo.Address(port)
except liblo.AddressError as err:
    print(err)
    sys.exit()

# Same target as muse
# 'ffff' meaning 4 floating points
target_path = '/muse/eeg'
pi = np.pi

# Displays 4 beautiful repeating sine graphs
while True:
    for x in np.linspace(0, 2*pi, 1000):
        # Muse electrodes work at 220Hz
        time.sleep(1/float(220))
        # Can communicate at a slower rate for testing
        # time.sleep(0.5)
        liblo.send(target,
                   target_path,
                   np.sin(x),
                   np.sin(x+pi/2),
                   np.sin(x+pi),
                   np.sin(x-pi/2))
