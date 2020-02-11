import tushare as ts
import pandas as pd
import datetime
import os
from datetime import datetime,timedelta
from dateutil.parser import parse
import numpy as np 
import time
A=pd.DataFrame(list(range(6)))
B=pd.DataFrame(list(range(3,8)))
AB=pd.concat([A,B],axis=0)
print(AB)
token = '37a185a5deb9251d6c544db5c0ac8a1cc00d7fe5d75a149a0c3103b1'
pro = ts.pro_api(token)
ticker='000622'
path = 'D:/The Road For Finacial Statics/Python/02.Learning Materrials/02.Data/02.daily_BarData'
filename = path + '/' + ticker + '.csv'

stock_history_data = pd.read_csv(filename,index_col=0,header=0)
stock_history_data.sort_values('trade_date',inplace=True)
print(stock_history_data.dtypes.tolist())
print(stock_history_data.columns.tolist())
# print(stock_history_data.select_dtypes(include=["int64"])

start_date = datetime.strptime(str(stock_history_data.iloc[-1, :]['trade_date']), '%Y%m%d') + timedelta(hours=24)
start_date = datetime.strftime(start_date, "%Y%m%d")
print(type(start_date))
end_date = datetime.strftime(datetime.now(), '%Y%m%d')
print(type(end_date))
print(type(datetime.now()))
data = pro.daily(
          ts_code=ticker+'.SZ',
          start_date=start_date,
          end_date=end_date
)
data.sort_values('trade_date',inplace=True)

if data.empty == True:
     outputflag = False
else:
  
     print(data.dtypes)
     start_date = datetime.strptime(str(data.iloc[-1, :]['trade_date']), '%Y%m%d') + timedelta(hours=24)
     start_date = datetime.strftime(start_date, "%Y%m%d")
   
     print(data.iloc[-1,:]['trade_date'])
     stock_history_data.append(data,ignore_index=False)
     AA=pd.concat([stock_history_data,data])
     AA['trade_date']=pd.to_datetime(AA['trade_date'],format='%Y/%m/%d')
     print(AA['trade_date'].dtype == 'datetime64[ns]')
     print(AA.dtypes)
     print(len(AA))
     stock_history_data.sort_values('trade_date',inplace=True)
     print(stock_history_data.head(10))     