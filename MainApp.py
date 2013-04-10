# -*- encoding=utf8 -*-
from src.main.handler.RegexpHandler import RegexpHandler
from src.main.action.HitsStatsAction import HitsStatsAction


handler = RegexpHandler(r"^\[.*SystemOut.*Req\sUrl:/perbank/(.*\.do).*$")

filenames = [
	'raw/20130308/61/SystemOut_13.03.08_08.25.52.log',
	'raw/20130308/61/SystemOut_13.03.08_08.35.42.log',
	'raw/20130308/62/SystemOut_13.03.08_08.25.26.log',
	'raw/20130308/62/SystemOut_13.03.08_08.40.28.log',
]
#创建点击率分析报告
machine = HitsStatsAction(handler, "report.txt", *filenames)
machine.action(single_report=True, output_format="操作名称: {0}, 点击次数: {1}")

#创建单客户行为报告

#创建时间切分报告