#!/user/bin/env python

#print "This line will be printed."

import xml.etree.ElementTree as ET
import csv
import cgi
import os, sys



available_language = [];
platform = "android"
csv_input_file = 'test.csv'


clear = lambda: os.system('clear')
clear()

print "============================  START  ============================"


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



for language_tab, language in enumerate(available_language):

	if(language is ""):
		continue

	outFileName = os.getcwd() + "/" +platform
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

					str = ' '.join(row)
					str = cgi.escape(str)

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