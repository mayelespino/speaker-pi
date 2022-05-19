class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    STATIONS = { 
        "chill1" : "http://99.198.118.250:8241/listen.pls",
        "chill2" : "http://192.99.17.12:4516/listen.pls",
        "chill3" : "http://192.99.17.12:4950/listen.pls",
        "dance1" : "http://uk4.internet-radio.com:8049/listen.pls",
        "dance2" : "http://hirschmilch.de:7000/listen.pls",
        "talk1" : "http://176.31.98.109:4962/listen.pls",
        "talk2" : "http://69.46.24.226:7006/listen.pls",
        "talk3" : "http://74.50.122.103:7372/listen.pls",
        "talk4" : "http://95.211.3.65:9185/listen.pls",
	"mcgee1" : "http://198.178.123.5:9486/listen.pls",
        "mcgee2" : "http://149.56.157.81:8700/listen.pls",
        "biblia1" : "http://149.56.157.81:8700/listen.pls",
        "biblia2" : "http://69.30.202.98:9400/listen.pls",
        "bolero1" : "http://46.4.33.73:8028/listen.pls",
        "bolero2" : "http://192.99.83.154:8024/listen.pls",
        "gregorian" : "http://66.70.249.70:5464/listen.pls",
	"noise1" : "http://uk5.internet-radio.com:8260/listen.pls"
    }
