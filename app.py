#!/usr/bin/python

from flask import Flask, render_template, redirect
import subprocess

def ioRemove(peripheral):
	myList[0].remove(int(peripheral))

def ioOn(peripheral):
	subprocess.check_output(["./reader", "/dev/USBDev251", "I" + peripheral])

def ioOff(peripheral):
	subprocess.check_output(["./reader", "/dev/USBDev251", "i" + peripheral])

def ioProbe(peripheral):
	return subprocess.check_output(["./reader", "/dev/USBDev251", "L" + str(peripheral)])

app = Flask(__name__)
device = "/dev/USBDev251"

myList = [[0,1,2], [], []]
ioList = []

for peripheral in myList[0]:
	if ioProbe(peripheral) != "000":
		ioList.append(peripheral)
		
@app.route("/")
def root():
   return render_template('main.html', ioList = ioList, descList = myList)

@app.route("/<peripheral>/<command>")
def handler(peripheral, command):
	if command == "remove":
		ioRemove(peripheral)
	if command == "on":
		ioOn(peripheral)
	if command == "off":
		ioOff(peripheral)
	return redirect("/")



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
