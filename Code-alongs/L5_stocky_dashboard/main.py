import dash
import dash_bootstrap_components as dbc
import os
from load_data import StockData
from dash import html, dcc # dcc - dash core components
from dash.dependencies import Output, Input

directory_path = os.path.dirname(__file__)
path = os.path.join(directory_path, "stocks_data")

# print(path)

stock_data_object = StockData(path)

# pick one stock 
# print(stock_data_object.stock_dataframe("AAPL"))

symbol_dict = {"AAPL": "Apple", "NVDA": "Nvidia", "TSLA": "Tesla", "IBM": "IBM"}
# create dictionary of dataframes (dictionary of lists of dataframes)
df_dict = {symbol: stock_data_object.stock_dataframe(symbol) for symbol in symbol_dict} # dict loop takes keys, if want values do .items()

stock_options_dropdown = [{"label": name, "value": symbol} for symbol, name in symbol_dict.items()]

ohlc_options = [{"label": option, "value": option} for option in ("open", "high", "low", "close")]

slider_marks = {i: mark for i, mark in enumerate(["1 day", "1 week", "1 month", "3 months", "1 year", "5 years", "Max"])}
print(df_dict.keys())
# print(df_dict["TSLA"]) #list with two dataframes
# print(df_dict["TSLA"][0]) #a dataframe

# create a Dash App
app = dash.Dash(__name__)

app.layout = html.Main([
    html.H1("Techy stocks viewer"),
    html.P("Choose a stock"),
    dcc.Dropdown(
        id = "stockpicker-dropdown",
        options = stock_options_dropdown,
        value = "AAPL",
    ),
    dcc.RadioItems(id = "ohlc-radio", options = ohlc_options, value = "close"),
    dcc.Graph(id = "stock-graph"),
    dcc.Slider(id = "time-slider", min = 0, max = 6, marks = slider_marks, value = 2, step = None)
    ]
)

@app.callback(
    Output("stock-graph", "figure"),
    Input("stockpicker-dropdown")
)

if __name__ == "__main__":
    app.run_server(debug = True)