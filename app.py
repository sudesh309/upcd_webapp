#!/usr/bin/python

from flask import Flask, render_template, redirect

app = Flask(__name__)
device = open("/dev/USBDev251", "w+")
myList = [[0,1,2], [], []]

def removeIO(peripheral):
	myList[0].remove(int(peripheral))

def ioOn(peripheral):
	device.write("I" + peripheral)
	device.flush()

def ioOff(peripheral):
	device.write("i" + peripheral)
	device.flush()

@app.route("/")
def root():
   return render_template('main.html', descList = myList)

@app.route("/<peripheral>/<command>")
def handler(peripheral, command):
	if command == "remove":
		removeIO(peripheral)
	if command == "on":
		ioOn(peripheral)
	if command == "off":
		ioOff(peripheral)
	return redirect("/")



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
