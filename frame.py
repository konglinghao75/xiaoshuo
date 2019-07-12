# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 09:23:26 2019



@author: klh
"""
import json
import threading
from redis_single import XzxRedis
class Frame:
    
    def __init__(self, feature_obj):
        
        self.feature_obj = feature_obj  #传一个feature_sczprc实例
        
        self.r = XzxRedis().r
        
        self.queue_name = feature_obj.show_book_url_redis_queue_name#远程redis队列的名称
        
        self.book_queue_name = feature_obj.book_info_redis_queue_name
        
        self.create_show_book_url_redis_queue()
        
    def create_show_book_url_redis_queue(self):
        
        '''
        将feature_obj中的get_all_show_book_url()方法返回的链接添加到redis队列中
        如果添加过则pass
        '''
        
    
        if not self.r.exists(self.queue_name):
            
            queue_list = self.feature_obj.get_all_show_book_url()
        
            self.r.rpush(self.queue_name, *queue_list)
            
    def create_show_book_url_info(self):
        
        show_url = self.r.lpop(self.queue_name)
        
        if show_url != None:#如果队列里有值
            
            info = self.feature_obj.get_show_book_url_info(show_url)
            
            self.r.rpush(self.book_queue_name, json.dumps(info))
            
    def work(self):
        
        
        
        while True:
            
            self.create_show_book_url_info()
            
    def main(self):
        
        for i in range(5):
            
            t = threading.Thread(target = self.work)
            
            t.start()
        
        
if __name__ == '__main__':
    
    from feature_sczprc import FeatureSczprc
    
    obj = FeatureSczprc()
    
    x = Frame(obj)
    
    x.create_show_book_url_info('https://m.sczprc.com/sort/1_1/')
    
    
    r = XzxRedis().r
    
    
