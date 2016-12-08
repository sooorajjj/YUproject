#!/usr/bin/python -tt
import sys
from sys import platform as _platform
import os
import subprocess
import time



def validation(device, flash_script_path, qfil_path):

	cmd1 = 'adb devices'
	scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan1)

	time.sleep(8)

	cmd2 = 'adb shell mount /system && adb shell grep -m 1  "^ro.build.display.wtid=" /system/build.prop'
	scan2 = str(subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT).strip())
	substr_scan = scan2[22:] #len(scan)-2
	print(substr_scan +' String length : ' + str(len(substr_scan)))

	time.sleep(3)
	cmd3 = 'adb shell grep -m 1  "^ro.product.model=" /system/build.prop'
	scan3 = str(subprocess.check_output(cmd3, shell=True, stderr=subprocess.STDOUT).strip())
	substr_scan3 = scan3[17:] #len(scan)-2

	if len(substr_scan3) == 0 :
		print("Device Validation Failed, \nExit! ")



	elif device.find(substr_scan3) >= 0:



		if substr_scan.find('125') >= 0:
			print('Unsigned Device')


			if _platform == 'linux' or _platform == 'linux2':
				build_type_path = os.path.join(flash_script_path, 'UnSigned')
				flash_script_module = os.path.join(build_type_path, 'flash.sh')
				subprocess.call(['source '+flash_script_module+' '+build_type_path], shell=True)

			elif _platform == 'darwin':
				print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')

			elif _platform == 'win32':
				print('Found '+_platform+'\n'+'')
				build_type_path = os.path.join(flash_script_path, 'UnSigned')
				flash_script_module = os.path.join(build_type_path, 'flash_all.bat')
				subprocess.Popen(flash_script_module+' '+build_type_path+'\/', stderr=subprocess.STDOUT).communicate()

			else :
				print('Unable to recognise this OS')
		

		elif substr_scan.find('126') >= 0:
			print('Signed Device')

			if _platform == 'linux' or _platform == 'linux2':
				print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')
			elif _platform == 'darwin':
				print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')
			elif _platform == 'win32':
				print('Found '+_platform+'\n'+'')
				qfil_module = os.path.join(qfil_path, 'QFIL.exe')
				build_type_path = os.path.join(flash_script_path, 'Signed')

				arg1 = ' -Mode=1 '
				arg2 = '-COM=6 '
				arg3 = '-SEARCHPATH="'+ build_type_path +'" '
				arg4 = '-Sahara=true;"'+ build_type_path +'\prog_emmc_FireHose_8916.mbn" '
				arg5 = '-RawProgram=rawprogram_unsparse.xml '
				arg6 = '-patch=patch0.xml '

				print('------------[ Detach Your Device From Pc, Get it into Download Mode, And Reconnect it Now ]------------')
				print('-----------[ Program is about to lunch QFIL tool with all the Firmwares loaded for YU4771+ ]-----------')
				print('-------[ You Only need To Select the Port And Flat Build option in QFIL Tool and press Download]-------')
				wait_for_user_input = raw_input('Press ENTER to Lunch QFIL tool:')

				# sys.argv = [arg1, arg2, arg3, arg4, arg5, arg6]
				os.system(qfil_module + arg1 + arg2 + arg3 + arg4 + arg5 + arg6)
				# subprocess.Popen([qfil_module + ' Mode=1 -COM=6 -SEARCHPATH="' + str(build_type_path) + '" -Sahara=true;"'+ str(build_type_path) + '\prog_emmc_FireHose_8916.mbn" -RawProgram=rawprogram_unsparse.xml -patch=patch0.xml'])
				# subprocess.call([qfil_module, arg1, arg2, arg3, arg4, arg5, arg6])

			else :
				print('Unable to recognise this OS')


		else :
			print('Unknown Model of Yuphoria')


	else :
		print('Device Not '+device+', \nExit!')


def fastboot_function(usb_attrs, recoveries_path):

	cmd = 'fastboot'+usb_attrs+'boot '+os.path.join(recoveries_path, 'twrp-yuphoria.img')
	scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan)
	time.sleep(20)


if __name__ == '__main__':
	fastboot_function(sys.argv[1], sys.argv[4])
	validation(sys.argv[0], sys.argv[5], sys.argv[6])
