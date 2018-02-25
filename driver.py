#!/usr/bin/env python

# Author: pr0n1s
# Credits: angr (shellphish)

import angr, logging

def dowork(sm):
	ss = []
	while len(sm.unconstrained) == 0:
		sm.step()
		ss.append(sm.stashes['active'])
	crash = sm.unconstrained[0].posix.dumps(0)
	return crash, ss

def getblock(proj, entry):
	block = proj.factory.block(entry)
	return block

def getaddr(ss):
	return str(ss[-2][0]).split('@')[1].split('>')[0]

def getinputlen(crash):
	return len(repr(crash).split('\\'))-1

def display(proj, crash, ss):
	print "\nSimulation completed"
	print "********************"
	print "\nSeg Fault @: {}".format(getaddr(ss))
	print "-----------------------"
	print getblock(proj, int(getaddr(ss), 16)).pp()
	print "\n[*] Input length: {}".format(getinputlen(crash))
	print "---------------------"
	print "Input: {}".format(repr(crash))

def main():
	proj = angr.Project('./bo')
	sm = proj.factory.simulation_manager(save_unconstrained=True)
	print "*************************************************"
	print "Simulation in progress: Detecting buffer overflow"
	print "*************************************************"
	crash, ss = dowork(sm)
	display(proj, crash, ss)

if __name__ == '__main__':
	logging.getLogger('angr').setLevel('ERROR')
	main()
