#!/usr/bin/python -tt
import sys
import subprocess
import time
import os



def fastboot_function(device, usb_attrs):

	cmd1 = 'fastboot'+usb_attrs+'getvar product'
	scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan1)
	time.sleep(2)

	if len(scan1) == 0 :
		print("Device Validation Failed, \nExit! ")

	elif scan1.find('WT6755_66_SZ_') >= 0:
		print('Yunicorn ('+device+')')

	else :
		print('Device Not '+device+', \nExit!')


if __name__ == '__main__':

	fastboot_function(sys.argv[0], sys.argv[1])
