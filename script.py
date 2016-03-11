#!/user/bin/env python

#print "This line will be printed."

import csv
import cgi
import os, sys


# function to get the complete output file name 
def getOutputFileName(path, platform, language):

	if platform == "android":
		return path + "/" + "string_" + language + ".xml"
	if platform == "ios":
		return path + "/" + "string_" + language + ".strings"
	return path + "/" + "string_" + language + ".resw"


#function to get the template name
def getTemplateFileName(platform):

	print "getTemplateFileName  ",platform
	if platform == "android":
		return "template_android.xml"
	if platform == "ios":
		return "template_ios.strings"

	return "template_window.resw"


clear = lambda: os.system('clear')
clear()


platforms = sys.argv
platforms.pop(0)

if not platforms:
	platforms = ['android', 'ios', 'window']


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

	if not (platform == "android" or platform == "ios" or platform == "window"):
		print "\n\n********Invalid argument for platform name  \"", platform , "\" .********"
		print "Please selecte only in \"android\",\"ios\" or \"window\".\n\n"
		continue

	for language_tab, language in enumerate(available_language):

		if(language is ""):
			continue

		outFileName = os.getcwd() + "/" + platform
		if not os.path.exists(outFileName):
			os.mkdir(outFileName)

		outFileName = getOutputFileName(outFileName, platform, language);

		print "\n=================", platform , "================="
		with open(outFileName, "wt") as fout:
			templateFileName = getTemplateFileName(platform)
			with open(templateFileName, "rt") as fin:
				for line in fin:

					f = open(csv_input_file)
					csv_f = csv.reader(f)

					replaced = False
					for row in csv_f:

#						str = ' '.join(row)
#						str = cgi.escape(str)

						rfrom = row[0].strip()
						rto = cgi.escape(row[language_tab+1])

						if platform == "android" or platform == "window":
							if ">" + rfrom + "<" in line: 

								line = line.replace(rfrom,rto)
								line = line.replace('&lt;','<')
								line = line.replace('&gt;','>')
								fout.write(line)
								print "replacing " , rfrom , " with " , rto

								replaced = True
						elif platform == "ios":
							if "\"" + rfrom + "\"" in line: 
								line = line.replace(rfrom,rto)
								fout.write(line)
								print "replacing " , rfrom , " with " , rto

								replaced = True
					if( not replaced):
						fout.write(line)

print "============================  FINISH  ============================\n"

