#!/usr/bin/python -tt
import sys
from sys import platform as _platform
import subprocess
import os
import devices
import Tools
import time


def select_device(project_path):
	print(' \n'.join(devices.list))# or try commented way

	selected_device_index = int(raw_input('Select a device model to continue :'))
	device = devices.device_list[selected_device_index]
	usb_attrs = devices.usb_attrs_list[selected_device_index]
	tools_path = os.path.join(project_path, 'Tools')
	firmwares_path = os.path.join(project_path, 'Firmwares')
	flash_script_path = os.path.join(firmwares_path, device)
	recovery_path = os.path.join(tools_path, 'Recoveries')
	device_module_path = os.path.join(tools_path, device)
	sys.argv = [device, usb_attrs, project_path, tools_path, recovery_path, flash_script_path]# Contains modelNo, we can set more arguments,
	execfile(device_module_path+'.py')#it will be available in execfile[Target] __main__


def os_platform():

	if _platform == 'linux' or _platform == 'linux2':
		print('========Linux=========')
		project_path = str(subprocess.check_output('pwd', shell=True).strip()) + '/'
		select_device(project_path)

	elif _platform == 'darwin':
		print('========OSX=========')
		print('No Support For OSX yet')
	
	elif _platform == 'win32':
		print('========Windows=========')
		print('No Support for Windows yet')
	    # project_path = 'C:\\working\\'

	else :
		print('Unable to recognise this OS')


if __name__ == '__main__':
	global device
	global project_path
	global tools_path
	global firmwares_path
	global flash_script_path
	global recovery_path
	global device_module_path
	os_platform()