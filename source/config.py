class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    STATIONS = { 
        "classic1" : "http://radio.promosat.com:8018/listen.pls",
        "chill1" : "http://99.198.118.250:8241/listen.pls",
        "chill2" : "http://uk4.internet-radio.com:8049/listen.pls",
	"chill3" : "http://199.233.234.34:25373/listen.pls",
	"chill4" : "http://wwfm.streamguys1.com:80/live.m3u",
	"chill5" : "http://91.121.38.100:8220/listen.pls",
        "dance1" : "http://hirschmilch.de:7000/listen.pls",
        "talk1" : "http://176.31.98.109:4962/listen.pls",
        "talk2" : "http://69.46.24.226:7006/listen.pls",
        "talk3" : "http://74.50.122.103:7372/listen.pls",
        "biblia3" : "http://de1.internet-radio.com:8268/listen.pls",
        "biblia2" : "http://listen.wofr.org:8888/kjv.m3u",
        "biblia1" : "http://149.56.157.81:8700/listen.pls",
        "bolero2" : "http://192.99.83.154:8024/listen.pls",
	"ambient1" : "http://uk5.internet-radio.com:8347/listen.pls",
	"ambient2" : "http://uk5.internet-radio.com:8260/listen.pls",
	"ambient3" : "http://149.56.234.138:8136/listen.pls",
	"ambient4" : "http://uk5.internet-radio.com:8260/listen.pls",
	"ambient5" : "http://198.27.120.235:8850/listen.pls",
	"reggae1" : "http://us5.internet-radio.com:8487/listen.pls",
	"reggae2" : "http://us4.internet-radio.com:8157/listen.pls",
	"npr1" : "http://91.121.205.70:7232/listen.pls"
    }
