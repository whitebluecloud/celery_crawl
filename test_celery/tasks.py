from __future__ import absolute_import
from test_celery.celery import app
import time,requests
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient

client = MongoClient('10.149.169.184', 27018)
db = client.mongodb_test
collection = db.celery_test
post = db.test
@app.task(bind=True,default_retry_delay=10) # set a retry delay, 10 equal to 10s
def longtime_add(self,i):
    print 'long time task begins'
    try:
        r = requests.get(i)
        target_page = bs(r.content, 'html.parser')
        tbl_lst = target_page.find('table', class_='tbl_lst')
        tbl_lst_tbody = tbl_lst.find('tbody')
        shop_list_tr = tbl_lst_tbody.find_all('tr')
        if(len(shop_list_tr) > 0):
          for shop in shop_list_tr:
            shop_name = ''
            site_item_id = shop['data-nv-mid']
            shop_item_id = shop['data-mall-pid']
            post.insert({'status':r.status_code,'shop_item_id':shop_item_id,'site_item_id':site_item_id,"create_time":time.time()})
        print 'long time task finished'
    except Exception as exc:
        raise self.retry(exc=exc)
    return r.status_code

@app.task(bind=True,default_retry_delay=10)
def test(self,target_page):
    print 'price_compare_detail start'
    print(target_page)
    
