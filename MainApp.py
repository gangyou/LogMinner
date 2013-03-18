from src.main.LineHandler import LineHandler
from src.main.MinningResult import MinningResult
from src.main.MinnerMachine import MinnerMachine


handler = LineHandler(r"^\[.*SystemOut.*Req\sUrl:/perbank/(.*\.do).*$")
# filenames = []
# for i in range(26,36):
# 	filenames.append("data/08" + str(i) + ".log")

filenames = [
	'raw/20130308/61/SystemOut_13.03.08_08.25.52.log',
	'raw/20130308/61/SystemOut_13.03.08_08.35.42.log',
	'raw/20130308/62/SystemOut_13.03.08_08.25.26.log',
	'raw/20130308/62/SystemOut_13.03.08_08.40.28.log',
]
machine = MinnerMachine(handler, *filenames)
machine.action()
