"""
--------------------------------------------------------------
Alan Marchiori - Aug 2015
Bucknell University
--------------------------------------------------------------

Views alarm clock i/o trace files using a web browser.

File format is text-based with one event per line.

Each line is fixed width:

             BUZZER
             ---------\
                       \
            ALARM      |
            ---------\ |
                     | |
       timestamp     | |   Led1    Led2    Led3    Led4
|-------- 21 ------| | | |--7--| |--7--| |--7--| |--7--|
                   0 0 0 0000000 0000000 0000000 0000000

Sample traces are in the /examples folder.

Images were generated with the makedigits.py script and are stored in
the /static folder.

HTML templates (Jinja2) are in the templates folder.

"""

from flask import Flask, render_template
import os.path
import logging
import os
import argparse

logging.basicConfig(level = logging.DEBUG)
DEBUG = True
SECRET_KEY = 'not very secret'
WORKING_FOLDER = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = os.path.join(WORKING_FOLDER, './examples')
static_folder = 'static'
static_url_path = 'static'

app = Flask (__name__)
app.config.from_object(__name__)

@app.route("/")
def main():
    logging.debug("access to main!")
    files = os.listdir(FILE_PATH)
    logging.debug("Showing files: " + str (files))
    return render_template('main.html',
                           files = files)

@app.route("/show/<path:filename>", defaults = {'line': 1})
@app.route("/show/<path:filename>/<int:line>")
def show(filename, line):
    local_filename = os.path.join(FILE_PATH, filename)
    # on a real server, cache this.
    with open (local_filename, 'r') as f:
        data = f.read().strip().split('\n')

    if line == 1:
        prevline = len(data)
    else:
        prevline = line - 1
    if line == len(data):
        nextline = 1
    else:
        nextline = line + 1

    # convert line from 1-based to 0-based on access.
    p = data[line - 1].strip().split()
    # parse timestamp as base 10 (default)
    ts = int(p[0])

    # parse remaining arguments
    alarm, buz = map(lambda x: int(x, 2), p[1:3])
    digits = p[3:7]
    if len(p) > 7:
      additionFeatures = True
      isAM = p[7] if p[7].isdigit() else -1
      plus = p[8] if p[8].isdigit() else -1
      minus = p[9] if p[9].isdigit() else -1
      alarmEnabled = p[10] if p[10].isdigit() else -1
      turnOffAlarm = p[11] if p[11].isdigit() else -1
    else:
      additionFeatures = False
      isAM = -1
      plus = -1
      minus = -1
      alarmEnabled = -1
      turnOffAlarm = -1


    return render_template("show.html",
                           filename = filename,
                           lineno = line,
                           prevline = prevline,
                           nextline = nextline,
                           totallines = len(data),
                           ts = ts,
                           alarm = alarm,
                           buz = buz,
                           digits = digits,
                           additionFeatures = additionFeatures,
                           isAM = int(isAM),
                           plus = int(plus), 
                           minus = int(minus),
                           alarmEnabled = int(alarmEnabled),
                           turnOffAlarm = int(turnOffAlarm),
                           data = p)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "-port", dest="port", type=int, help="port number", default=5000)
    arg = parser.parse_args()
    app.run(host='0.0.0.0', port=arg.port)
