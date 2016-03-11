#!/user/bin/env python

#print "This line will be printed."

import csv
import cgi
import os, sys


clear = lambda: os.system('clear')
clear()


platforms = sys.argv
platforms.pop(0)

if not platforms:
	platforms = ['android', 'ios', 'window']

#			print "\n\n********Invalid argument for platform name  \"", arg , "\" .********"
#			print "Please selecte only in \"android\",\"ios\" or \"window\".\n\n"


available_language = []
csv_input_file = 'data.csv'


# check for available languages to create files
f = open(csv_input_file)
csv_f = list(csv.reader(f))

for row in csv_f:
	for language_tab, language in enumerate(row):
		if(language_tab == 0):
			continue
		'''
		if(language.strip() is ""):
			print "*ERROR* Source CSV title should not be blank"
			exit()
		'''
		#print language.strip()	
		available_language.append(language)
	break



print "============================  START  ============================"

for idx, platform in enumerate(platforms):

	for language_tab, language in enumerate(available_language):

		if(language is ""):
			continue

		outFileName = os.getcwd() + "/" + platform
		if not os.path.exists(outFileName):
			os.mkdir(outFileName)

		outFileName = platform + "/" + "string_" + language + ".xml"

		print "\n=================", outFileName , "================="
		with open(outFileName, "wt") as fout:
			with open("strings.xml", "rt") as fin:
				for line in fin:

					f = open(csv_input_file)
					csv_f = csv.reader(f)

					replaced = False
					for row in csv_f:

#						str = ' '.join(row)
#						str = cgi.escape(str)

						rfrom = row[0].strip()
						rto = cgi.escape(row[language_tab+1])


						if ">" + rfrom + "<" in line: 

							line = line.replace(rfrom,rto)
							line = line.replace('&lt;','<')
							line = line.replace('&gt;','>')
							fout.write(line)
							print "replacing " , rfrom , " with " , rto

							replaced = True
					if( not replaced):
						fout.write(line)

print "============================  FINISH  ============================\n"