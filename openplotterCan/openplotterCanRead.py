#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2019 by Sailoog <https://github.com/openplotter/openplotter-can>
# 
# Openplotter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
# Openplotter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openplotter. If not, see <http://www.gnu.org/licenses/>.
import subprocess, configparser, time

def main():
	exists = False
	data_conf = configparser.ConfigParser()
	conf_file = '.openplotter/openplotter.conf'
	data_conf.read(conf_file)
	items = data_conf.get('CAN', 'canable')
	try: devices = eval(items)
	except: devices = []
	for i in devices:
		exists = True
		subprocess.Popen(['slcand','-o','-s5','-S','921600',i[0],i[1]])
		time.sleep(1)
		subprocess.Popen(['ip', 'link', 'set', i[1], 'up'])
	while exists:
		time.sleep(10)

if __name__ == '__main__':
	main()
