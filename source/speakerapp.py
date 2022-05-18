from flask import Flask
import subprocess 

app = Flask(__name__)
app.config.from_object("config.ProductionConfig")

#
# Health check
#

@app.route('/')
def root():
    dict = app.config["STATIONS"]
    stations = str(dict).replace(",","<BR/>\n")
    return stations

#
# Internet Radio
#

#
# Volume
#

@app.route('/mute/', methods=['POST'])
def play_mute():
    subprocess.Popen(["/usr/bin/pkill","mplayer","-c"])
    subprocess.Popen(["/usr/bin/pkill","omxplayer","-c"])
    return "play_mute - OK"

@app.route('/100/', methods=['POST'])
def vol_100():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "100%"])
    return "vol_100 - OK"

@app.route('/95/', methods=['POST'])
def vol_95():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "95%"])
    return "vol_95 - OK"

@app.route('/85/', methods=['POST'])
def vol_85():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "85%"])
    return "vol_85 - OK"

@app.route('/75/', methods=['POST'])
def vol_75():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "75%"])
    return "vol_75 - OK"

@app.route('/50/', methods=['POST'])
def vol_50():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "50%"])
    return "vol_50 -OK"

#
# Utils
#
@app.route('/cron/', methods=['POST'])
def util_cron():
    p = subprocess.Popen(["/usr/bin/crontab","-l"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out

@app.route('/date_time/', methods=['POST'])
def util_date_time():
    p = subprocess.Popen(["/bin/date"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out

#
# Play a station
#
@app.route('/play_station/<station>', methods=['POST'])
def play_station(station):
    dict = app.config["STATIONS"]
    if not dict.has_key(station):
       return "unknown station: {}".format(station)
    stat = dict[station]
    subprocess.Popen(["/usr/bin/mplayer","-playlist", stat])
    return "play_station: {} - OK".format(stat)
#
# List stations
#
@app.route('/list_stations/', methods=['GET'])
def list_station():
    stationsDict = app.config["STATIONS"]
    stationList = list(stationsDict.keys()) 
    stationList.sort()
    return ",".join(stationList)

@app.route('/list_nature_stations/', methods=['GET'])
def list_nature_station():
    stationsDict = app.config["NATURE"]
    stationList = list(stationsDict.keys()) 
    stationList.sort()
    return ",".join(stationList)

@app.route('/list_chill_stations/', methods=['GET'])
def list_chill_station():
    stationsDict = app.config["CHILL"]
    stationList = list(stationsDict.keys()) 
    stationList.sort()
    return ",".join(stationList)

@app.route('/list_talk_stations/', methods=['GET'])
def list_talk_station():
    stationsDict = app.config["TALK"]
    stationList = list(stationsDict.keys()) 
    stationList.sort()
    return ",".join(stationList)

@app.route('/list_upbeat_stations/', methods=['GET'])
def list_upbeat_station():
    stationsDict = app.config["UPBEAT"]
    stationList = list(stationsDict.keys()) 
    stationList.sort()
    return ",".join(stationList)

@app.route('/list_bible_stations/', methods=['GET'])
def list_bible_station():
    stationsDict = app.config["BIBLE"]
    stationList = list(stationsDict.keys()) 
    stationList.sort()
    return ",".join(stationList)

#
# MAIN
#
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
