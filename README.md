# yahoo_fin

Fork of yahoo_fin package from http://theautomatic.net/yahoo_fin-documentation/ with support for intraday data retrieval.


### ***What is yahoo_fin?***

Yahoo_fin is a Python 3 package to scrape historical stock 
price data, as well as to provide current information on market caps, 
dividend yields, and which stocks comprise the major exchanges. 
Additional functionality includes scraping income statements, balance 
sheets, cash flows, holder information, and analyst data. The package 
includes the ability to get live stock prices, capture cryptocurrency 
data, and get the most actively traded stocks on a current trading day.


### ***Requirements***

Yahoo_fin requires the following packages to be installed:
```
ftplib
io
pandas
requests
requests_html
```

With the exception of **requests_html**, these dependencies come pre-installed with [Anaconda](https://www.continuum.io/downloads). **requests_html** requires Python 3.6+ and is needed for several of the functions in **yahoo_fin**. To install **requests_html**, you can use pip:

`pip install requests_html`

If you wish to make multiple requests using a user-agent rotator is advised. Install with:

`pip install random_user_agent`

### ***Installing***
Create a Python package with:

`python3 setup.py sdist bdist_wheel`

and install:

`pip3 install dist/yahoo_fin-0.8.5-py3-none-any.whl`

### ***Methods***

The yahoo_fin package has two modules. These are called *stock_info* and *options*.  *stock_info* has the below primary methods.

**[get_analysts_info](https://github.com/CarlosManuelRodr/yahoo-fin#get_analysts_info)**
**[get_balance_sheet](https://github.com/CarlosManuelRodr/yahoo-fin#get_balance_sheet)**
**[get_cash_flow](https://github.com/CarlosManuelRodr/yahoo-fin#get_cash_flow)**
**[get_data](https://github.com/CarlosManuelRodr/yahoo-fin#get_data)**
**[get_day_gainers](https://github.com/CarlosManuelRodr/yahoo-fin#get_day_gainers)**
**[get_day_losers](https://github.com/CarlosManuelRodr/yahoo-fin#get_day_losers)**
**[get_day_most_active](https://github.com/CarlosManuelRodr/yahoo-fin#get_day_most_active)**
**[get_holders](https://github.com/CarlosManuelRodr/yahoo-fin#get_holders)**
**[get_income_statement](https://github.com/CarlosManuelRodr/yahoo-fin#get_income_statement)**
**[get_live_price](https://github.com/CarlosManuelRodr/yahoo-fin#get_live_price)**
**[get_quote_table](https://github.com/CarlosManuelRodr/yahoo-fin#get_quote_table)**
**[get_top_crypto](https://github.com/CarlosManuelRodr/yahoo-fin#get_top_crypto)**
**[get_stats](https://github.com/CarlosManuelRodr/yahoo-fin#get_stats)**
**[tickers_dow](https://github.com/CarlosManuelRodr/yahoo-fin#tickers_dow)**
**[tickers_nasdaq](https://github.com/CarlosManuelRodr/yahoo-fin#tickers_nasdaq)**
**[tickers_other](https://github.com/CarlosManuelRodr/yahoo-fin#tickers_other)**
**[tickers_sp500](https://github.com/CarlosManuelRodr/yahoo-fin#tickers_sp500)**

The methods for *options* are listed below:

**[get_calls](https://github.com/CarlosManuelRodr/yahoo-fin#get_calls)**
**[get_expiration_dates](https://github.com/CarlosManuelRodr/yahoo-fin#get_expiration_dates)**
**[get_options_chain](https://github.com/CarlosManuelRodr/yahoo-fin#get_options_chain)**
**[get_puts](https://github.com/CarlosManuelRodr/yahoo-fin#get_puts)**

## **<u>stock_info module</u>**

Any method from yahoo_fin’s *stock_info* module can be imported by running the follow line, with *get_analysts_info* replaced with the method of choice.

```
from yahoo_fin.stock_info import get_analysts_info
```

Alternatively, all methods can be imported at once like so:

```
from yahoo_fin.stock_info import *
```

### ***get_analysts_info(ticker)***

Scrapes data from the Analysts page for the input ticker from Yahoo Finance (e.g. [https://finance.yahoo.com/quote/NFLX/analysts?p=NFLX](https://finance.yahoo.com/quote/NFLX/analysts?p=NFLX). This includes information on earnings estimates, EPS trends / revisions etc.

Returns a dictionary containing the tables visible on the ‘Analysts’ page.

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input. 
```

**Example**

`get_analysts_info('nflx')`


### ***get_balance_sheet(ticker)***

Scrapes the balance sheet for the input ticker from Yahoo Finance (e.g. [https://finance.yahoo.com/quote/NFLX/balance-sheet?p=NFLX](https://finance.yahoo.com/quote/NFLX/balance-sheet?p=NFLX).

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input. 
```

**Example**

`get_balance_sheet('nflx')`

### ***get_cash_flow(ticker)***

Scrapes the cash flow statement for the input ticker from Yahoo Finance (e.g. [https://finance.yahoo.com/quote/NFLX/cash-flow?p=NFLX](https://finance.yahoo.com/quote/NFLX/cash-flow?p=NFLX).

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input. 
```

**Example**

`get_cash_flow(``'nflx'``)`

### ***get_data(ticker,*** ***start_date = None, end_date = None, index_as_date = True, interval = “1d”)***

Downloads historical price data of a stock into a pandas data frame. 
Offers the functionality to pull daily, weekly, or monthly data.

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  
This is the only required argument.

start_date

The date the price history should begin.

end_date

The date the price history should end.

index_as_date

Default is True.  If index_as_date = True, then the index of the returned data frame is the date associated with each record.  
Otherwise, the date is returned as its own column.

interval

Default is "1d", or daily.  This parameter specifies the interval in which to return the data.  The default value of "1d" returns daily historical data.  Input "1wk" for weekly data, "1mo" for monthly data or "1m" for intraday data.  Any other input for the interval parameter will result in an error. When using "1m" start_date and end_date are ignored since only the last trading day is available.
```

**Example**

`msft_data = get_data('msft')`


If you want to filter by a date range, you can just add a value for the start_date and / or end_date parameters, like below:


`from1999 = get_data('msft' , start_date = '01/01/1999')`

`few_days = get_data('msft' , start_date = '01/01/1999' , end_date = '01/10/1999')`

Get intraday, weekly or monthly historical price data:

`intraday_data = get_data("msft", interval = "1m")`

`weekly_data = get_data("msft", interval = "1wk")`

`monthly_data = get_data("msft", interval = "1mo")`

### ***get_day_gainers()***

Scrapes the top 100 (at most) stocks with the largest gains (on the given trading day) from Yahoo Finance (see [https://finance.yahoo.com/gainers](https://finance.yahoo.com/gainers)).

**Example**

`get_day_gainers()`


### ***get_day_losers()***

Scrapes the top 100 (at most) worst performing stocks (on the given trading day) from Yahoo Finance (see [https://finance.yahoo.com/losers](https://finance.yahoo.com/losers)).

**Example**

`get_day_losers()`


### ***get_day_most_active()***

Scrapes the top 100 most active stocks (on the given trading day) from Yahoo Finance (see [https://finance.yahoo.com/most-active](https://finance.yahoo.com/most-active)).

**Example**

`get_day_most_active()`


### ***get_holders(ticker)***

Scrapes data from the Holders tab from Yahoo Finance (e.g. [https://finance.yahoo.com/quote/NFLX/holders?p=NFLX](https://finance.yahoo.com/quote/NFLX/holders?p=NFLX) for an input ticker.

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input. 
```

**Example**

`get_holders('nflx')`


### ***get_income_statement(ticker)***

Scrapes the income statement for the input ticker, which includes information on Price / Sales, P/E, and moving averages (e.g. [https://finance.yahoo.com/quote/NFLX/financials?p=NFLX](https://finance.yahoo.com/quote/NFLX/financials?p=NFLX).

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input. 
```

**Example**

`get_income_statement('nflx')`


### ***get_live_price(ticker)***

Scrapes the live quote price for the input ticker.

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input. 
```

**Example**

`get_live_price('nflx')`


### ***get_quote_table(ticker , dict_result = True)***

Scrapes the primary table found on the quote page of an input ticker from Yahoo Finance (e.g. [https://finance.yahoo.com/quote/AAPL?p=AAPL](https://finance.yahoo.com/quote/AAPL?p=AAPL))

The following fields with their corresponding values are returned:

```
1y Target Est
52 Week Range
Ask
Volume
Beta
Bid
Days Range
Dividend & Yield
EPS (TTM)
Earnings Date
Ex-Dividend Date
Market Cap
Open
PE Ratio (TTM)
Previous Close
Quote Price
Volume
```


**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input. 

dict_result

Default is True.  If True, the function returns the results in a dict format.  Otherwise, the results are returned in a data frame.
```  
**Example**

`get_quote_table('aapl')`

### ***get_top_crypto(ticker)***

Scrapes data for top 100 cryptocurrencies by market cap (see [https://finance.yahoo.com/cryptocurrencies](https://finance.yahoo.com/cryptocurrencies)).

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input. 
```

**Example**

`get_stats('nflx')`

### ***get_stats(ticker)***

Scrapes data off the statistics page for the input ticker, which 
includes information on Price / Sales, P/E, and moving averages (e.g. [https://finance.yahoo.com/quote/NFLX/key-statistics?p=NFLX](https://finance.yahoo.com/quote/NFLX/key-statistics?p=NFLX).

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input. 
``` 

**Example**

`get_stats('nflx')`

### ***tickers_dow()***

Returns a list of tickers currently listed on the Dow Jones.  No 
parameters need to be passed.  The tickers are scraped from Yahoo 
Finance (see [https://finance.yahoo.com/quote/%5EDJI/components?p=%5EDJI](https://finance.yahoo.com/quote/%5EDJI/components?p=%5EDJI).

**Example**

`tickers = tickers_dow()`

### ***tickers_nasdaq()***

Returns a list of tickers currently listed on the NASDAQ.  No parameters need to be passed.  This method, along with *tickers_other*, works by scraping text files from [ftp://ftp.nasdaqtrader.com/SymbolDirectory/](ftp://ftp.nasdaqtrader.com/SymbolDirectory/).

*tickers_nasdaq *scrapes the **nasdaqlisted.txt** file from the link above, while *tickers_other* scrapes the **otherlisted.txt** file.

**Example**

`tickers = tickers_nasdaq()`

### ***tickers_other()***

See above description for *tickers_nasdaq*.

**Example**

`tickers = tickers_other()`

### ***tickers_sp500()***

Returns a list of tickers currently listed in the S&P 500.  The data for this is scraped from Wikipedia:

[https://en.wikipedia.org/wiki/List_of_S%26P_500_companies](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)

**Example**

`tickers = tickers_sp500()`

## **<u>options module</u>**

We can import any method from *options* module like this:

`from yahoo_fin.options import get_options_chain`


Just replace **get_options_chain** with any other method. Also, we can import all methods at once like so:

`from yahoo_fin.options import *`

### ***get_calls(ticker, date = None)***

Scrapes call options data for the input ticker from Yahoo Finance (e.g. [https://finance.yahoo.com/quote/NFLX/options?p=NFLX](https://finance.yahoo.com/quote/NFLX/options?p=NFLX).

Returns a pandas data frame containing the call options data for the given ticker and expiration date.

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input. 

date

Expiration date.  Default is None, which will return the earliest upcoming expiration date's data.
``` 

**Example**

`get_calls(``'nflx'``)`

`get_calls(``'nflx'``,` `'06/19/2020'``)`


### ***get_expiration_dates(ticker)***

Scrapes expiration dates for the input ticker from Yahoo Finance (e.g. [https://finance.yahoo.com/quote/NFLX/options?p=NFLX](https://finance.yahoo.com/quote/NFLX/options?p=NFLX).

Returns a list of expiration dates for the input ticker. This list 
is based off the drop-down selection box on the options data webpage for
 the input ticker.

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input. 
``` 

**Example**

`get_expiration_dates(``'nflx'``)`

`get_expiration_dates(``'amzn'``)`


### ***get_options_chain(ticker, date)***

Scrapes calls and puts tables for the input ticker from Yahoo Finance (e.g. [https://finance.yahoo.com/quote/NFLX/options?p=NFLX](https://finance.yahoo.com/quote/NFLX/options?p=NFLX).

Returns a dictionary with two data frames. The keys of the dictionary are labeled *calls* (which maps to the calls data table) and *puts* (which maps to the puts data table).

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input.  

date

Expiration date.  Default is None, which will return the earliest upcoming expiration date's data.
```

**Example**

```
# get data on the earliest upcoming expiration date
get_options_chain('nflx')
```

```
# specify an expiration date
get_options_chain('amzn', '03/15/2019')
```


### ***get_puts(ticker, date = None)***

Scrapes put options data for the input ticker from Yahoo Finance (e.g. [https://finance.yahoo.com/quote/NFLX/options?p=NFLX](https://finance.yahoo.com/quote/NFLX/options?p=NFLX).

Returns a pandas data frame containing the put options data for the given ticker and expiration date.

**Possible parameters**

```
ticker

Stock ticker (e.g. 'MSFT', 'AMZN', etc.).  Case insensitive.  Required as input.  

date

Expiration date.  Default is None, which will return the earliest upcoming expiration date's data.
```

**Example**

`get_puts('nflx')`

`get_puts('nflx','06/19/2020')`