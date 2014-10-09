#!/usr/bin/python

message = "my name is xusong, i am from china!"

trans = ''
i = len(message) - 1

while i >= 0:
	trans = trans + message[i]
	i = i - 1
print trans
