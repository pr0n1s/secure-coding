#!/usr/bin/env python2

# Author: pr0n1s
# Credits: angr (shellphish)

# CPU Architecture LE/BE?
def getArch(proj):
	return proj.arch

# Entry point of the binary
def getEntry(proj):
	return proj.entry

# Shared objects
def getSharedObjects(proj):
	return proj.loader.shared_objects.items()

# Min address of binary
def getMinAddress(proj):
	return proj.loader.min_addr

# Max address of binary
def getMaxAddress(proj):
	return proj.loader.max_addr

# Stack executable?
def isStackExecable(proj):
	return proj.loader.main_object.execstack

# Symbol by name
def getSymbol(proj, name):
	return proj.loader.find_symbol(name)

def getSegments(proj):
	return proj.loader.main_object.segments

def getSections(proj):
	return proj.loader.main_object.sections
