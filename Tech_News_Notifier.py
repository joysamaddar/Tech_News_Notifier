#! python3
# Tech_News_Notifier.py
# AUTHOR - Joy Samaddar


import requests, bs4, time
from win10toast import ToastNotifier
toaster = ToastNotifier()
last_verge_news = ''
last_cnet_news = ''
last_bbc_news = ''
while True:
    verge_res = requests.get('https://www.theverge.com/tech')
    cnet_res = requests.get('https://www.cnet.com/news/')
    bbc_res = requests.get('https://www.bbc.com/news/technology')
    verge_res.raise_for_status()
    cnet_res.raise_for_status()
    bbc_res.raise_for_status()
    verge = bs4.BeautifulSoup(verge_res.text, 'html.parser')
    cnet = bs4.BeautifulSoup(cnet_res.text, 'html.parser')
    bbc = bs4.BeautifulSoup(bbc_res.text,'html.parser')
    verge_news = verge.select('.c-entry-box--compact__body a')
    cnet_news = cnet.select('.riverPost h5 a')
    bbc_news = bbc.select('.lx-stream-post__header-text')
    verge_news_body = verge_news[0].getText()
    cnet_news_body = cnet_news[0].getText()
    bbc_news_body = bbc_news[0].getText()
    if verge_news_body != last_verge_news:
        last_verge_news = verge_news_body
        toaster.show_toast('VERGE NEWS', verge_news_body, threaded=True,icon_path=None, duration=8)
    time.sleep(200)
    if cnet_news_body != last_cnet_news:
        last_cnet_news = cnet_news_body
        toaster.show_toast('CNET NEWS', cnet_news_body, threaded=True,icon_path=None, duration=8)
    time.sleep(200)
    if bbc_news_body != last_bbc_news:
        last_bbc_news = bbc_news_body
        toaster.show_toast('BBC NEWS', bbc_news_body, threaded=True,icon_path=None, duration=8)
    time.sleep(200)



