#!/usr/bin/env python

"""
All my Groovy stack traces have all this Java from either the Groovy implementation or
Oracle's JDK methods calling other JDK methods.

This obscures my view of the stack, because I usually don't care about this internal stuff.

"""

import fileinput

lastWasEmpty = False

for line in fileinput.input():
	if (line.find(".java:") == -1) and (line.find("Native Method") == -1):
		if lastWasEmpty == True:
			print
			lastWasEmpty = False
		print line,
	else:
		lastWasEmpty = True
		print ".",
