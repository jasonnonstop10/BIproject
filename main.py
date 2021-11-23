from fastapi import FastAPI
from uncleengineer import thaistock

app = FastAPI()


@app.get("/")
async def root():

    return {"message": "Hello World"}


@app.get("/stock")
async def root():
    stocks = ["ADVANC", "AOT", "AWC", "BAM", "BBL", "BDMS", "BEM", "BGRIM", "BH", "BJC", "BTS", "CBG",
              "COM7", "CPALL", "CPF", "CPN", "CRC", "DELTA", "DTAC", "EA", "EGCO", "GLOBAL", "GPSC", "GULF", "HMPRO", "INTUCH", "IVL",
              "KBANK", "KTB", "KTC", "LH", "MINT", "MTC", "OR", "OSP", "PTT", "PTTEP", "PTTGC", "RATCH", "SAWAD", "SCB", "SCC", "SCGP", "TISCO",
              "TTB", "TOA", "TOP", "TRUE", "TU", "VGI"]
    stockdetall = []
    for stock in stocks:
        stockdetall.append(thaistock(stock))
    return {"data": stockdetall}

# findone stock in ID


@app.get("/stock/{ID}")
async def root(ID: str):
    stock = thaistock(ID)
    return stock
