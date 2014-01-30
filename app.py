#!/usr/bin/python

from flask import Flask, render_template, redirect, request
import subprocess

def ioRemove(peripheral):
	subprocess.check_output(["./reader", "/dev/USBDev251", "P" + peripheral + "000"])
	return "P" + peripheral + "000"

def ioOn(peripheral):
	subprocess.check_output(["./reader", "/dev/USBDev251", "I" + peripheral])

def ioOff(peripheral):
	subprocess.check_output(["./reader", "/dev/USBDev251", "i" + peripheral])

def ioProbe(peripheral):
	return subprocess.check_output(["./reader", "/dev/USBDev251", "L" + str(peripheral)])

def ioAdd():
	perinum = request.form["ioperipheral"]
	port = request.form["ioport"]
	pin = request.form["iopin"]
	mode = request.form["imode"]
	subprocess.check_output(["./reader", "/dev/USBDev251", "P" + perinum + port + pin + mode])
	

app = Flask(__name__)
device = "/dev/USBDev251"

myList = [[0,1,2], [], []]
		
@app.route("/", methods=["GET", "POST"])
def root():
	if request.method == "POST":
		if request.form['submit'] == "addio":
			ioAdd()	
	ioList = []
	for peripheral in myList[0]:
		if ioProbe(peripheral) != "000":
			ioList.append(peripheral)
	return render_template('main.html', ioList = ioList, descList = myList)

@app.route("/<peripheral>/<command>")
def handler(peripheral, command):
	if command == "removeio":
		ioRemove(peripheral)
	if command == "on":
		ioOn(peripheral)
	if command == "off":
		ioOff(peripheral)
	return redirect("/")



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
