from vnpy.event import EventEngine
from vnpy.trader.engine import BaseEngine, MainEngine
from vnpy.gateway.ctp.ctp_gateway import CtpGateway
from vnpy.trader.setting import SETTINGS
from logging import INFO


SETTINGS["log.active"] = True
SETTINGS["log.level"] = INFO
SETTINGS["log.console"] = True


setting = {
    "用户名":"158164",
    "密码":"zlb198838",
    "经纪商代码":"9999",
    "交易服务器":"180.168.146.187:10101",
    "行情服务器":"180.168.146.187:10111",
    "产品名称":"simnow_client_test",
    "授权编码":"0000000000000000",
    "产品信息":"11111"
}

event_engine = EventEngine()
main_engine = MainEngine(event_engine)
main_engine.add_gateway(CtpGateway)
main_engine.connect(setting, "CTP")
