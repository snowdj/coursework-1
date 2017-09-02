

#--- load library ---#
import numpy
import datetime
from qstkutil import qsdateutil, DataAccess
import pandas

#--- functions ---#
def get_price(symbols, start_day, end_day, close_field = 'close', verbose = 'False'):
    '''
    return prices in pandas dataframe type
    '''
    time_of_day = datetime.timedelta(hours = 16)
    time_stamps = qsdateutil.getNYSEdays(start_day, end_day, time_of_day)
    data_obj = DataAccess.DataAccess('Yahoo')
    if verbose:
        print __name__ + "reading data ..."
    price = data_obj.get_data(time_stamps, symbols, close_field)
    return price


#--- main script ---#
order_array = numpy.loadtxt('orders.csv', delimiter=',', dtype='S10')
cash_start = 1e6 # $1M

# scan orders for symbol set
symbol_set = set([])
for order in order_array:
    symbol_set.add(order[3])

# extract start and end days
first_order_year = int(order_array[0][0])
first_order_month = int(order_array[0][1])
first_order_day = int(order_array[0][2])
start_day = datetime.datetime(first_order_year, first_order_month, first_order_day)
end_day = datetime.datetime(int(order_array[-1][0]), int(order_array[-1][1]), int(order_array[-1][2])+1)

# get price data for all orders
price_data = get_price(list(symbol_set),start_day,end_day,verbose='True')

# go trough orders to update cash and equity values
if first_order_month == 1 and first_order_day == 1:
    day_start = datetime.datetime(first_order_year-1, 12,30,16,0,0)
else:
    day_start = datetime.datetime(first_order_year, 1, 1, 16, 0, 0)
value_start = {'cash':[cash_start]}
for symbol in symbol_set:
    value_start[symbol]=[0.0]
value_df = pandas.DataFrame(value_start, index=[day_start])
print value_df

import pdb

cash = cash_start
order_idx = 0
last_trade_date = day_start
for order in order_array:
    trade_date = datetime.datetime(int(order[0]), int(order[1]), int(order[2]), 16, 0, 0)   
    trade_symbol = order[3]
    trade_price = price_data[trade_symbol][trade_date]
    if order[4] == 'Buy':
        trade_action = 1
    elif order[4] == 'Sell':
        trade_action = -1
    trade_volume = int(order[5])
    
    # update cash
    cash -= trade_action * trade_volume * trade_price
    if trade_date == last_trade_date:
        value_df['cash'][trade_date] = cash
    else:
        value_df = value_df.set_value(trade_date, 'cash', cash)
        
    # update equity values
    for symbol in symbol_set:
        equity_value_updated = False
        equity_value = 0.0
        # update equity value by price change
        if not order_idx == 0 and not trade_date == last_trade_date:
            equity_value += value_df[symbol][last_trade_date]/price_data[symbol][last_trade_date]*price_data[symbol][trade_date]
            equity_value_updated = True
        # update equity value by trading
        if symbol == trade_symbol:
            equity_value += trade_action *trade_volume * price_data[symbol][trade_date]
            equity_value_updated = True
        if equity_value_updated or not trade_date == last_trade_date:
            value_df[symbol][trade_date] = equity_value
        
    order_idx += 1
    last_trade_date = trade_date
    print "\n\n"
    print order
    print value_df



# caculate total value
cash_final = cash
equity_value_final = 0.0
for symbol in symbol_set:
    equity_value_final += value_df[symbol][-1]
fund_final = cash_final + equity_value_final

print("Trading results: Cash $%.2f  Equity $%.2f  Total fund $%.2f" %(cash_final, equity_value_final, fund_final))


