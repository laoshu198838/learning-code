from vnpy.event import EventEngine,Event
from vnpy.trader.engine import BaseEngine, MainEngine
from vnpy.gateway.ctp.ctp_gateway import CtpGateway
from vnpy.trader.event import EVENT_LOG,EVENT_TICK
from vnpy.trader.object import SubscribeRequest,ContractData
from vnpy.trader.constant import Exchange

setting = {
    "用户名":"158164",
    "密码":"zlb198838",
    "经纪商代码": "9999",
    "交易服务器": "180.168.146.187:10101",
    "行情服务器": "180.168.146.187:10111",
    "产品名称": "simnow_client_test",
    "授权编码": "0000000000000000",
    "产品信息": "11111"
}
def process_tick_event(event: Event):
    tick = event.data
    print(tick)
    print("--"*40)

contract = ContractData(
    symbol="zn1910",
    exchange=Exchange("SHFE"),
    gateway_name="CTP",
    name="SHFE",
    product="SHFE",
    size=100,
    pricetick=2.0,
)

event_engine = EventEngine()
event_engine.register(EVENT_TICK, process_tick_event) #注册事件
main_engine = MainEngine(event_engine)
main_engine.add_gateway(CtpGateway)
main_engine.connect(setting, "CTP")
main_engine.subscribe(contract,"CTP") #订阅行情