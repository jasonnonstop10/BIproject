from fastapi import FastAPI
import stock_financials as sf
import stock_statics as ss
import stock_detail as sd

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
stock = ["ADVANC", "AOT", "BBL", "BDMS", "BEM", "BGRIM", "BH", "BJC", "BTS", "CBG", "COM7", "CPALL", "CPF", "CPN",
         "CRC", "DELTA", "DTAC", "EA", "EGCO", "GLOBAL", "GPSC", "GULF", "HMPRO", "INTUCH", "IRPC", "IVL", "KBANK", "KCE", "KTB", "KTC", "LH", "MINT", "MTC", "OR", "OSP", "PTT", "PTTEP", "PTTGC", "RATCH", "SAWAD", "SCB", "SCC", "SCGP", "STA", "STGT", "TISCO", "TOP", "TRUE", "TU"]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/stock/financials/{stock_name}")
async def stock_financials(stock_name: str):
    stock_name = stock_name.upper()
    return sf.get_stockname(stock_name)


@app.get("/stock/statics")
async def stock_statics():
    return ss.get_statics()


@app.get("/stock/statics/{stock_name}")
async def stock_statics(stock_name: str):
    return ss.get_staticsfindone(stock_name)


@app.get("/stock/detail/")
async def stock_detail():
    return sd.get_detailALL()


@app.get("/stock/detail/{stock_name}")
async def stock_detail(stock_name: str):
    stock_name = stock_name.upper()
    return sd.get_detail(stock_name)
