
'''
@author: Tony (Ning) Liu
@contact: tonyningliu@gmail.com
@summary: Simple backtest. Combining event finder and market simulator.
'''


#--- import library ---#
# standard library
import numpy
import datetime
import copy

# 3rd party library
import pandas

# local library (QSTK)
from qstkutil import qsdateutil, DataAccess




#--- globals ---#
start_date = (2008, 1, 1)
end_date = (2009, 12, 31)
data_source = 'Yahoo'
symbol_list_file = 'sp5002012'
market_symbol = 'SPY'
price_limit = 9.0
cash_start = 100000




#--- functions ---#

def get_price(symbols, start_day, end_day, close_field = 'close', data_source = 'Yahoo', verbose = 'False'):
    '''
    return prices in pandas dataframe type
    '''
    time_of_day = datetime.timedelta(hours = 16)
    time_stamps = qsdateutil.getNYSEdays(start_day, end_day, time_of_day)
    data_obj = DataAccess.DataAccess(data_source)
    if verbose:
        print __name__ + " is reading data from %s..." %data_source
    market_data = data_obj.get_data(time_stamps, symbols, close_field)
    if verbose:
        print __name__ + "finished reading data."
    return market_data


def find_events(market_data, price_limit, market_symbol = None, verbose = False):
    '''
    Find all the events based on market_data (price, volume, etc) and strategy definition.
    Output event matrix, in which '1' indicates an event.
    '''
    
    # Completing the Data - Removing the NaN values from the Matrix
    # market_data = (market_data.fillna(method='ffill')).fillna(method='backfill')

    # Calculating Daily Returns for the Market
    # tsu.returnize0(market_data.values)
    # SPYValues=market_data[marketSymbol]

    # Calculating the Returns of the Stock Relative to the Market 
    # So if a Stock went up 5% and the Market rised 3%. The the return relative to market is 2% 
    #mktneutDM = market_data - market_data[marketSymbol]

    # Searching for events based on strategy and fill '1' in the event matrix
    # Event description: stock falls below price_limit.
    if verbose:
        print __name__ + " is searching events"
    event_df = pandas.DataFrame(columns = market_data.columns, index = market_data.index)
    for symbol in market_data.columns:
        if not symbol == market_symbol:
            for i in range(1, len(market_data.index)):
                if market_data[symbol][i-1] >= price_limit and market_data[symbol][i] < price_limit:
                    event_df[symbol][i] = 1.0  #overwriting by the bit, marking the event
    if verbose:
        print __name__ + "finished searching events."
                    
    return event_df


def gen_orders(event_df, market_symbol = None, verbose = False):
    '''
    Generate orders based on event matrix and strategy.
    '''
    order_df = pandas.DataFrame(0, columns = event_df.columns, index = event_df.index)
    if verbose:
        print __name__ + " is generating order matrix..."
    for i in range(len(event_df.index)):
        for symbol in event_df.columns:
            if event_df[symbol][i] > 0:
                order_df[symbol][i] += 100
                order_df[symbol][min(i+5, len(event_df.index)-1)] -= 100
    if verbose:
        print __name__ + "finished generating order matrix."

    return order_df
        

def sim_engine(order_df, price_data, cash_start, verbose = False):
    '''
    Simulating trading based on order matrix and calculating equity value, cash and return.
    '''
    value_df = pandas.DataFrame(0.0, columns = order_df.columns, index = order_df.index).join(pandas.DataFrame(0, columns = ['cash'], index = order_df.index))
    if verbose:
        print("Backtest simulation started...")
    for time_idx in range(len(order_df.index)):
        if verbose:
            print("Simulating %s" %order_df.index[time_idx])
        if not time_idx == 0: #Copy cash, and update equity values from previous day by market variation
            value_df['cash'][time_idx] = value_df['cash'][time_idx-1]
            for symbol in order_df.columns:
                if not numpy.isnan(price_data[symbol][time_idx]) and not numpy.isnan(price_data[symbol][time_idx-1]):
                    value_df[symbol][time_idx] = value_df[symbol][time_idx-1] * (price_data[symbol][time_idx]/price_data[symbol][time_idx-1])
        else:
            value_df['cash'][time_idx] = cash_start
            
        for symbol in order_df.columns: #update equity value and cash by orders
            if not numpy.isnan(price_data[symbol][time_idx]):
                trading_value = order_df[symbol][time_idx] * price_data[symbol][time_idx]
                value_df[symbol][time_idx] += trading_value
                value_df['cash'][time_idx] -= trading_value

    if verbose:
        print("Simulation finished. Calculating results...")
    
    daily_value = value_df.sum(axis = 1) #sum of cash and equity value for each trading day
    daily_return = numpy.divide(numpy.array(daily_value[1:]), numpy.array(daily_value[:len(daily_value.index)-1])) - 1.0
    sharpe_ratio = numpy.sqrt(252) * daily_return.mean() / daily_return.std()            
    final_portfolio_value = daily_value[daily_value.index[-1]]
    final_cash = value_df['cash'][value_df.index[-1]]
    final_equity_value = final_portfolio_value - final_cash
    ret = final_portfolio_value/float(cash_start) - 1

    if verbose:
        print("Total return: %.2f%%\nSharpe ratio = %.2f\nFinal portfolio value = $%.2f\nFinal cash = $%.2f" %(ret*100.0, sharpe_ratio, final_portfolio_value, final_cash))
    
    return ret, sharpe_ratio, final_portfolio_value, final_cash, final_equity_value, daily_return, daily_value, value_df


            

#--- main script ---#

# Parse date range and symbol list
start_day = datetime.datetime(start_date[0], start_date[1], start_date[2])
end_day = datetime.datetime(end_date[0], end_date[1], end_date[2])

data_obj = DataAccess.DataAccess(data_source)
symbols = data_obj.get_symbols_from_list(symbol_list_file)
symbols.append(market_symbol)

# Get market data
market_data_actual_close = get_price(symbols, start_day, end_day, close_field = 'actual_close', data_source = data_source, verbose = 'True')
#market_data_adj_close = get_price(symbols, start_day, end_day, close_field = 'close', data_source = data_source, verbose = 'True')

# Completing the Data - Removing the NaN values from the Matrix
# Do not fill actual close data for event finder since it may result in more events
#market_data_adj_close = (market_data_adj_close.fillna(method='ffill')).fillna(method='backfill')

# Find events, generate orders, and simulate returns.
event_df = find_events(market_data_actual_close, price_limit, verbose = True)
order_df = gen_orders(event_df, verbose = True)
ret, sharpe_ratio, final_portfolio_value, final_cash, final_equity_value, daily_return, daily_value, value_df = sim_engine(order_df, market_data_actual_close, cash_start, verbose = True)

