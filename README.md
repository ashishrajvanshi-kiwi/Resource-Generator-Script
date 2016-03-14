# RESOURCE GENERATOR SCRIPT

## Intro

Resource generator script is helpful in creating the string resource file for multiple language support. It allows the user to create multiple resource file of multiple laguage support in just one go automatically.

## Prerequisites
- Template resource file with predefined guidlines.
- CSV file that contain all language support info

### Software requirements
- Terminal
- OS (IOS , Linux)
- Python framework (csv, cgi, os, sys)

## Guidlines

- Template resource file name should be as follows
     - For Android should be named as "template_android"
     - For Ios should be named as "template_ios"
     - For window should be named as "template_window"
- CSV file which contain all language support info, will be common for all platform and its name should be "data.csv".

## Support

This script provide the support for creating resource file for below languages
- Android
- Ios
- Windows



## How it works



## How to use

Below is the format of command to create the resource file

- Create resource for all platforms

		eg:-	$ python script.py  
	It will create the resource file in all supported platforms

- You can specify for which platform you want to generate the resource file

		eg:-	$ python script.py android
				$ python script.py ios
				$ python script.py window
	It will create the resource file in specified supported platform 

- You can also specify more than one platform

		eg:-	$ python script.py android ios
				$ python script.py ios window
				$ python script.py android window
	It will create the resource file in specified platforms



## Contributors
- Ashish Rajvanshi (ashish.rajvanshi@kiwitech.com)
- Manoj Chauhan (manoj@kiwitech.com)

**Free Software, Hell Yeah!**
