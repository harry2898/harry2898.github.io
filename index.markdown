---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

#layout: home
title: "Harry's Stuff!"
---
# Python Guide
## Get Everything Installed
1. Download the latest version of [Python](https://www.python.org/downloads/)
	- Follow the default install options.
	- Make sure the check box option "add to path" is selected.
2. Download [Wing Pro](https://wingware.com/downloads/wing-pro)
	- Follow the default install options.

## Check that Everything Installed Correctly
1. Check that Python was added to path:
	- Press the "windows" key or press the "start" icon in the lower left of your screen.
	- Type "path".
	- Open "Edit the system enviroment variables".
	- Click "Enviroment Variables..." near the bottom right.
	- Within the top box "User variables for default" double click "Path".
	- At the top you should see:
		- ...\Python\PythonXXX\Scripts\
		- ...\Python\PythonXXX\
		- It does not matter which comes first.
		- "XXX" stands for the version of python installed.
2. Check that Python works:
	- Press the "windows" key or press the "start" icon in the lower left of your screen.
	- Type "powershell".
	- Open "powershell.exe".
	- Type "python" and press enter.
	- You should see a couple lines of output about python and your current line should start with `>>>`
	- Type:
	```python
	print("Hello World")
	```
	- You should see the output: `Hello World`.
	- Congrats you just typed and ran your first Python code!
3. Check that Wing works:
	- Open "Wing Pro X".
		- "X" stands for the version of python installed.
	- Save the file as "wing_test" without parenthesis.
	- Type:
	```python
	x = 69
	print(x)
	```
	- Near the top middle press the green play button to run your code.
	- Click through the text box saving your program.
		- Select the check box to not show the message again.
	- Near the bottom middle you should see the output `69`.
	- Congrats you just ran your first Python program!

## Basics of Programming