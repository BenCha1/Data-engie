import yfinance as yf
import pandas as pd
import sqlalchemy as sqla
import numpy as np

Data = pd.DataFrame()

def rendement(ticker):
    df=Data[ticker]
    df=df.tail(2)
    r=(df[1]/df[0]-1)
    return r
def Vol_moyenne(ticker):
    df=Data[ticker]
    v=np.std(df)
    return v

def volatilite(ticker):
    df=Data[ticker]
    L=list(df.tail(7))
    v=np.std(L)
    return v



Tickers=[]
Rendements=[]
Volatilite_moyenne=[]
Volatilite=[]


microsoft = "MSFT"
apple = "AAPL"
tesla = "TSLA"
google = "GOOG"
spy = "SPY"


data_aapl = pd.DataFrame(yf.download(apple, start = "2017-01-01", end = "2022-11-14"))[["Close"]].rename(columns = {"Close":"AAPL"})
data_msft = pd.DataFrame(yf.download(microsoft, start = "2017-01-01", end = "2022-11-14"))[["Close"]].rename(columns = {"Close":"MSFT"})
data_tsla = pd.DataFrame(yf.download(tesla, start = "2017-01-01", end = "2022-11-14"))[["Close"]].rename(columns = {"Close":"TSLA"})
data_google = pd.DataFrame(yf.download(google, start = "2017-01-01", end = "2022-11-14"))[["Close"]].rename(columns = {"Close":"GOOG"})
data_snp = pd.DataFrame(yf.download(spy, start = "2017-01-01", end = "2022-11-14"))[["Close"]].rename(columns = {"Close":"SPY"})


data_finale_true = data_aapl.join(data_msft).join(data_tsla).join(data_google).join(data_snp)

ticker_liste = ["AAPL", "MSFT", "GOOG", "TSLA", "SPY"]
Data = data_finale_true.copy()



for ticker in ticker_liste:
    Tickers.append(ticker)
    Rendements.append(rendement(ticker))
    Volatilite_moyenne.append(Vol_moyenne(ticker))
    Volatilite.append(volatilite(ticker))
    
df = pd.DataFrame([ Rendements,Volatilite_moyenne,Volatilite],
               columns =Tickers)

Index=["Rendement ajd","Volatilite moyenne historique","Volatilite recente"]

df["stats"] = Index

data_finale_true.to_csv("raw_final_true.csv")

data_finale_true = data_finale_true.reset_index()

URI  = "mysql://root:master2@localhost/data"
con = sqla.create_engine(URI)

data_stats = df.copy()

data_stats.to_csv("modified_true.csv")

data_finale_true.to_sql(name = "raw_true", con = con, if_exists = "append", index = False)
data_stats.to_sql(name = "modified", con = con, if_exists = "append", index = False)

