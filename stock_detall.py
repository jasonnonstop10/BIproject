from bs4 import BeautifulSoup
import requests
import concurrent.futures

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}


def get_stock(stock):
    allstock = {}
    for name in stock:
        url = "http://siamchart.com/stock-info/" + name + "/"
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        # find div id page
        page = soup.find('div', id='page')
        #  find table td
        td = page.find_all('td')
        # remove td tag
        td = [i.text for i in td]

        tdhead = td[:9]
        tdbody = td[9:]
        # data[0] = "name": name
        data = {"name": name}
        #  mapping 1-8 json format data {'tdhead': 'tdbody'}
        data.update(dict(zip(tdhead, tdbody)))
        allstock[name] = data
    # return json format data
    return allstock


def get_stockname(stockname):
    url = "http://siamchart.com/stock-info/" + stockname + "/"
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    # find div id page
    page = soup.find('div', id='page')
    #  find table td
    td = page.find_all('td')
    # remove td tag
    td = [i.text for i in td]

    tdhead = td[:9]
    tdbody = td[9:]
    # data[0] = "name": name
    data = {"name": stockname}
    #  mapping 1-8 json format data {'tdhead': 'tdbody'}
    data.update(dict(zip(tdhead, tdbody)))
    return data


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(get_stock)
