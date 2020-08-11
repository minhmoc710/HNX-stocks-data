import requests
OUTPUT = "OUTPUT/{}.html"
INPUT = "test.txt"
with open(INPUT, 'r') as maCP:
    for CP in maCP:
        headers = {
            'authority': 'www.stockbiz.vn',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.59 Safari/537.36 Edg/85.0.564.30',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'origin': 'https://www.stockbiz.vn',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.stockbiz.vn/Stocks/{}/HistoricalQuotes.aspx'.format(CP.strip()),
            'accept-language': 'en,vi;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        }
        for i in range (1, 39):
            data = [
            ('Cart_ctl00_webPartManager_wp1770166562_wp1427611561_callbackData_Callback_Param', '2017-8-10'),
            ('Cart_ctl00_webPartManager_wp1770166562_wp1427611561_callbackData_Callback_Param', '2020-8-10'),
            ('Cart_ctl00_webPartManager_wp1770166562_wp1427611561_callbackData_Callback_Param', '{}'.format(i)),
            ]

            response = requests.post('https://www.stockbiz.vn/Stocks/AAV/HistoricalQuotes.aspx', headers=headers, data=data)
            with open (OUTPUT.format(CP.strip()), 'a', encoding='utf8') as f:
                f.write(response.text)
            print(CP.strip()+"--finished crawling page {}".format(i))

