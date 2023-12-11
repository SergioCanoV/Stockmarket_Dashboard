import requests
import pandas as pd
import plotly.graph_objects as go
import json
from datetime import timedelta, datetime as dt
import os
from os.path import exists

params = {
    'access_key': '___________________________',
    'date_from': '2023-01-01T00:00:00+0000',
    'date_to': '2023-12-10T00:00:00+0000',
    'limit': '950'
}

def storeJson(dataJson):
    current_datetime = dt.now()
    json_object = json.dumps(dataJson, indent=4)
    with open('./prices_data/{}-{}-{}-{}_{}.json'.format(current_datetime.year, current_datetime.month,
                                                         current_datetime.day, current_datetime.hour,
                                                         get_variable_name(dataJson)), "w") as outfile:
        outfile.write(json_object)
    return None

# Function to get variable names as strings
def get_variable_name(variable):
    for name in globals():
        if id(globals()[name]) == id(variable):
            return name
    for name in locals():
        if id(locals()[name]) == id(variable):
            return name
    return None

files = os.listdir('./prices_data')
# Validate that you can request new data
if files == []:
    api_result1 = requests.get('http://api.marketstack.com/v1/tickers/aapl/eod', params)
    api_result2 = requests.get('http://api.marketstack.com/v1/tickers/amzn/eod', params)
    api_result3 = requests.get('http://api.marketstack.com/v1/tickers/msft/eod', params)
    api_result4 = requests.get('http://api.marketstack.com/v1/tickers/nvda/eod', params)
    api_result5 = requests.get('http://api.marketstack.com/v1/tickers/lyft/eod', params)
    api_result6 = requests.get('http://api.marketstack.com/v1/tickers/wbd/eod', params)
    api_result7 = requests.get('http://api.marketstack.com/v1/tickers/tsla/eod', params)
    api_result8 = requests.get('http://api.marketstack.com/v1/tickers/para/eod', params)
    api_result9 = requests.get('http://api.marketstack.com/v1/tickers/meta/eod', params)
    api_result10 = requests.get('http://api.marketstack.com/v1/tickers/intc/eod', params)
    api_response1 = api_result1.json()
    api_response2 = api_result2.json()
    api_response3 = api_result3.json()
    api_response4 = api_result4.json()
    api_response5 = api_result5.json()
    api_response6 = api_result6.json()
    api_response7 = api_result7.json()
    api_response8 = api_result8.json()
    api_response9 = api_result9.json()
    api_response10 = api_result10.json()
    storeJson(api_response1)
    storeJson(api_response2)
    storeJson(api_response3)
    storeJson(api_response4)
    storeJson(api_response5)
    storeJson(api_response6)
    storeJson(api_response7)
    storeJson(api_response8)
    storeJson(api_response9)
    storeJson(api_response10)
    # Import JSON files to dataframes
    files2 = os.listdir('./prices_data')
    f = open('./prices_data/{}'.format(files2[0]))
    api1 = json.load(f)
    f = open('./prices_data/{}'.format(files2[1]))
    api2 = json.load(f)
    f = open('./prices_data/{}'.format(files2[2]))
    api3 = json.load(f)
    f = open('./prices_data/{}'.format(files2[3]))
    api4 = json.load(f)
    f = open('./prices_data/{}'.format(files2[4]))
    api5 = json.load(f)
    f = open('./prices_data/{}'.format(files2[5]))
    api6 = json.load(f)
    f = open('./prices_data/{}'.format(files2[6]))
    api7 = json.load(f)
    f = open('./prices_data/{}'.format(files2[7]))
    api8 = json.load(f)
    f = open('./prices_data/{}'.format(files2[8]))
    api9 = json.load(f)
    f = open('./prices_data/{}'.format(files2[9]))
    api10 = json.load(f)
    f.close()
else:
    files = os.listdir('./prices_data')
    if files[0][10:12] != dt.now().hour:
        api_result1 = requests.get('http://api.marketstack.com/v1/tickers/aapl/eod', params)
        api_result2 = requests.get('http://api.marketstack.com/v1/tickers/amzn/eod', params)
        api_result3 = requests.get('http://api.marketstack.com/v1/tickers/msft/eod', params)
        api_result4 = requests.get('http://api.marketstack.com/v1/tickers/nvda/eod', params)
        api_result5 = requests.get('http://api.marketstack.com/v1/tickers/lyft/eod', params)
        api_result6 = requests.get('http://api.marketstack.com/v1/tickers/wbd/eod', params)
        api_result7 = requests.get('http://api.marketstack.com/v1/tickers/tsla/eod', params)
        api_result8 = requests.get('http://api.marketstack.com/v1/tickers/para/eod', params)
        api_result9 = requests.get('http://api.marketstack.com/v1/tickers/meta/eod', params)
        api_result10 = requests.get('http://api.marketstack.com/v1/tickers/intc/eod', params)
        api_response1 = api_result1.json()
        api_response2 = api_result2.json()
        api_response3 = api_result3.json()
        api_response4 = api_result4.json()
        api_response5 = api_result5.json()
        api_response6 = api_result6.json()
        api_response7 = api_result7.json()
        api_response8 = api_result8.json()
        api_response9 = api_result9.json()
        api_response10 = api_result10.json()
        # Removing old JSON files
        for file in files:
            os.remove('./prices_data/{}'.format(file))
        # Function to store json files to avoid multiple API calls
        storeJson(api_response1)
        storeJson(api_response2)
        storeJson(api_response3)
        storeJson(api_response4)
        storeJson(api_response5)
        storeJson(api_response6)
        storeJson(api_response7)
        storeJson(api_response8)
        storeJson(api_response9)
        storeJson(api_response10)
        # Importing the JSON files
        files3 = os.listdir('./prices_data')
        f = open('./prices_data/{}'.format(files3[0]))
        api1 = json.load(f)
        f = open('./prices_data/{}'.format(files3[1]))
        api2 = json.load(f)
        f = open('./prices_data/{}'.format(files3[2]))
        api3 = json.load(f)
        f = open('./prices_data/{}'.format(files3[3]))
        api4 = json.load(f)
        f = open('./prices_data/{}'.format(files3[4]))
        api5 = json.load(f)
        f = open('./prices_data/{}'.format(files3[5]))
        api6 = json.load(f)
        f = open('./prices_data/{}'.format(files3[6]))
        api7 = json.load(f)
        f = open('./prices_data/{}'.format(files3[7]))
        api8 = json.load(f)
        f = open('./prices_data/{}'.format(files3[8]))
        api9 = json.load(f)
        f = open('./prices_data/{}'.format(files3[9]))
        api10 = json.load(f)
        f.close()
    else:
        # Importing the JSON files
        files3 = os.listdir('./prices_data')
        f = open('./prices_data/{}'.format(files3[0]))
        api1 = json.load(f)
        f = open('./prices_data/{}'.format(files3[1]))
        api2 = json.load(f)
        f = open('./prices_data/{}'.format(files3[2]))
        api3 = json.load(f)
        f = open('./prices_data/{}'.format(files3[3]))
        api4 = json.load(f)
        f = open('./prices_data/{}'.format(files3[4]))
        api5 = json.load(f)
        f = open('./prices_data/{}'.format(files3[5]))
        api6 = json.load(f)
        f = open('./prices_data/{}'.format(files3[6]))
        api7 = json.load(f)
        f = open('./prices_data/{}'.format(files3[7]))
        api8 = json.load(f)
        f = open('./prices_data/{}'.format(files3[8]))
        api9 = json.load(f)
        f = open('./prices_data/{}'.format(files3[9]))
        api10 = json.load(f)
        f.close()

list_companies = [api1, api2, api3, api4, api5, api6, api7, api8, api9, api10]

def api_response(api_company):
    return pd.DataFrame(api_company['data'])


temp_list = []
for i in range(0, len(list_companies)):
    temp_list.append(api_response(list_companies[i]))
df_temp = pd.concat(temp_list)
df_temp2 = df_temp['eod'].apply(pd.Series)
df_temp2['avg'] = (df_temp2.high+df_temp2.low)/2
df_temp2[['date2','time']] = df_temp2['date'].str.split('T', expand=True)
df_temp2.drop('date',axis=1,inplace=True)
df_temp2.rename(columns={'date2':'date'},inplace=True)
df_temp2['date'] = pd.to_datetime(df_temp2['date'])

def tableRender(company):
    temp = df_temp2.loc[:,['date','symbol','avg','high','low','open','close','volume']].sort_values('date',ascending=False)
    temp = temp.loc[(temp.date >= pd.to_datetime(dt.now().date() - timedelta(days=14))) & (temp.symbol == company)]#.set_index('date')
    # temp.index.name = None
    temp_obj = temp.select_dtypes(['object'])
    temp[temp_obj.columns] = temp_obj.apply(lambda x: x.str.strip())
    return temp

def candlestick_graph(company):
    fig = go.Figure(data=[go.Candlestick(x=df_temp2['date']
                                         , open=df_temp2.loc[df_temp2.symbol == company].open
                                         , high=df_temp2.loc[df_temp2.symbol == company].high
                                         , low=df_temp2.loc[df_temp2.symbol == company].low
                                         , close=df_temp2.loc[df_temp2.symbol == company].close)])
    fig.update(layout_xaxis_rangeslider_visible=False)
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0)
                      , height=297
                      )
    # fig.show()
    return fig
# candlestick_graph('META')
