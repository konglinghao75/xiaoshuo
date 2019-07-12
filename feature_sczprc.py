# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 08:58:30 2019

伤城中文的特征函数
https://www.sczprc.com/




@author: klh
"""
from spider import Spider

feature_name = 'FeatureSczprc'



class FeatureSczprc:
    
    show_book_url_redis_queue_name = 'Sczprc_queue_name'
    
    book_info_redis_queue_name = 'Sczprc_book_info'
    
    domain = 'm.sczprc.com'
    
    host = 'https://m.sczprc.com'
    
    def __init__(self, proxy = False):
        '''
        proxy: 默认开启代理，False为关闭代理
        
        '''
        self.spider = Spider(proxy)
        
        
        
    
    def get_all_show_book_url(self):
        
        url = 'https://m.sczprc.com/sort/{}_{}/'
        
        list_1 = [url.format(1, i) for i in range(1, 291)]
#        list_2 = [url.format(2, i) for i in range(1, 75)]
#        list_3 = [url.format(3, i) for i in range(1, 611)]
        
        return list_1
    
    def get_show_book_url_info(self, show_book_url):
        
        regexs = dict(
                
            
            info = '<p class="line"><a href="#">\[(.*?)\]</a><a href="(.*?)" class="blue">(.*?)</a>/<a href="/author/.*?">(.*?)</a></p>'
                
                )
        
        info = self.spider.get_info(show_book_url, **regexs)
        
        assert bool(info['info']) == True
        
        info['info'] = [{'type': i[0],'url': self.host + i[1], 'name': i[2], 'author': i[3]} for i in info['info']]
  
        
        return info
        
        
        
        
        
        
    

if __name__ == '__main__': 
    
    x = FeatureSczprc(proxy = True)
    
#    list_info = x.get_all_show_book_url()
    
    info = x.get_show_book_url_info('https://m.sczprc.com/sort/1_1/')

        

