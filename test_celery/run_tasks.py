from .tasks import longtime_add
import time
if __name__ == '__main__':
    url = ['http://search.shopping.naver.com/detail/detail.nhn?nv_mid=8949671261', 'http://search.shopping.naver.com/detail/detail.nhn?nv_mid=9135216776']
    for i in url:
       result = longtime_add.delay(i)
       print 'Task end'
