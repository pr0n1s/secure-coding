#!/usr/bin/env python

# Author: pr0n1s
# Credits: angr (shellphish)

import angr

proj = angr.Project('./bo')

print "[*] Simulation in progress: Detecting buffer overflow"
sm = proj.factory.simulation_manager(save_unconstrained=True)

while len(sm.unconstrained) == 0:
	sm.step()

us = sm.unconstrained[0]
crash = us.posix.dumps(0)
print "[*] Simulation completed: Vulnerable"
print "[*] Seg Fault @: {}".format(us)
print "[*] Input length: {}\n[*] Input: {}".format(len(repr(crash).split('\\'))-1 ,repr(crash))
