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

def getsegfault(ss):
	return ss[-2]

def getinputlen(crash):
	return len(repr(crash).split('\\'))-1

def display(crash, ss):
  print "[*] Simulation completed"
  print "[*] ********************"
  print "[*] Seg Fault @: {}".format(getsegfault(ss))
  print "[*] -------------------------------------"
  print "[*] Trace:"
  print "[*] ------"
  for s in ss:
    print "\t{}".format(s)
  print "[*] Input length: {}".format(getinputlen(crash))
  print "[*] -----------------"
  print "[*] Input: {}".format(repr(crash))

def main():
	proj = angr.Project('./bo')
	sm = proj.factory.simulation_manager(save_unconstrained=True)

	print "[*] Simulation in progress: Detecting buffer overflow"
	print "[*] *************************************************"
	crash, ss = dowork(sm)
	display(crash, ss)

if __name__ == '__main__':
	logging.getLogger('angr').setLevel('ERROR')
	main()
