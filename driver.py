#!/usr/bin/env python

# Author: pr0n1s
# Credits: angr (shellphish)

import angr

proj = angr.Project('./bo')

print "[*] Simulation in progress: Detecting buffer overflow"
print "[*] *************************************************"
sm = proj.factory.simulation_manager(save_unconstrained=True)

ss = []
while len(sm.unconstrained) == 0:
	sm.step()
	ss.append(sm.stashes['active'])

crash = sm.unconstrained[0].posix.dumps(0)

print "[*] Simulation completed"
print "[*] ********************"
print "[*] Seg Fault @: {}".format(simstates[-2])
print "[*] -------------------------------------"
print "[*] Trace:"
print "[*] ------"
for s in ss:
	print "\t{}".format(s)
print "[*] Input length: {}".format(len(repr(crash).split('\\'))-1)
print "[*] -----------------"
print "[*] Input: {}".format(repr(crash))
