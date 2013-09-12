#!/usr/bin/python
# (c) 2013 Trever L. Adams
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

# This is a simple translation of a function found at:
# http://en.wikipedia.org/wiki/Maidenhead_Locator_System
# (c) 2012 Chris Ruvolo.  Licensed under a 2-clause BSD license.
def latlon2gs(lat, lon):
	grid = ""
        five60 = float(5)/float(60)
 
	lon = lon + 180
	lat = lat + 90
 
	grid += chr(ord('A') + int(lon / 20))
	grid += chr(ord('A') + int(lat / 10))
	grid += chr(ord('0') + int((lon % 20)/2))
	grid += chr(ord('0') + int((lat % 10)/1))
	grid += chr(ord('a') + int((lon - (int(lon/2)*2)) / (five60)))
	grid += chr(ord('a') + int((lat - (int(lat/1)*1)) / (2.5/60)))
 
	return grid

db_files = {}

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

ensure_dir("./gsdb/")
f=open("db.csv", "r")
line = f.readline() # Trash CSV header
line = f.readline()
while line:
	words = line.split()
	gs = latlon2gs(float(words[1]), float(words[2]))
	gs = gs[0:6]
	try:
		if(db_files[gs]):
			db_files[gs].write(words[0] + "\t" + words[1] + "\t" + words[2] + "\n")
	except:
		if(len(db_files) > 100):
			for key, item in db_files.items():
				db_files[key].close()
				del db_files[key]

		if os.path.exists("./gsdb/" + gs + ".csv"):
			db_files[gs] = open("./gsdb/" + gs + ".csv", "a+b")
		else:
			db_files[gs] = open("./gsdb/" + gs + ".csv", "w+b")
			db_files[gs].truncate
			db_files[gs].write("bssid\tlat\tlon\n")
	line = f.readline()

f.close()
