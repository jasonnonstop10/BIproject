from fastapi import FastAPI
import stock_detall as sd
import stock_statics as ss
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://bipython.herokuapp.com/",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
stock = ["ADVANC", "AOT", "BBL", "BDMS", "BEM", "BGRIM", "BH", "BJC", "BTS", "CBG", "COM7", "CPALL", "CPF", "CPN",
         "CRC", "DELTA", "DTAC", "EA", "EGCO", "GLOBAL", "GPSC", "GULF", "HMPRO", "INTUCH", "IRPC", "IVL", "KBANK", "KCE", "KTB", "KTC", "LH", "MINT", "MTC", "OR", "OSP", "PTT", "PTTEP", "PTTGC", "RATCH", "SAWAD", "SCB", "SCC", "SCGP", "STA", "STGT", "TISCO", "TOP", "TRUE", "TU"]


@app.get("/")
async def root():

    return {"message": "Hello World"}


@app.get("/stock/detall")
async def stock_detall():

    return sd.get_stock(stock)


@app.get("/stock/detall/{stock_name}")
async def stock_detall(stock_name: str):
    stock_name = stock_name.upper()
    return sd.get_stockname(stock_name)


@app.get("/stock/statics")
async def stock_statics():
    return ss.get_statics()


@ app.get("/stock/statics/{stock_name}")
async def stock_statics(stock_name: str):
    return ss.get_staticsfindone(stock_name)
