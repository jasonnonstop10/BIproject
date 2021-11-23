from bs4 import BeautifulSoup
import requests
import concurrent.futures


def get_stock(stock):
    allstock = {}
    for name in stock:
        url = "http://siamchart.com/stock-info/" + name + "/"
        res = requests.get(url)
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


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(get_stock)
