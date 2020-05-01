#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CREATE TABLE bilibili (
#   id int(8) unsigned NOT NULL AUTO_INCREMENT,
#   view int(9) NOT NULL COMMENT '播放总数',
#   follower int(9) NOT NULL COMMENT '被关注数',
#   likes int(9) NOT NULL COMMENT '点赞数',
#   video_count int(9) NOT NULL COMMENT '视频数',
#   PRIMARY KEY (id)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
import os,requests,json,pymysql
class spider(object):
    """docstring for zs_spider"""
    def __init__(self):
    # create connection object
        self.conn = pymysql.connect(host='192.168.28.140',port=3306,user='test',passwd='test123',db='test',charset='utf8')
        self.cursor = self.conn.cursor()
        self.headers = {
            "user-agent": "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)",
            "referer":"https://space.bilibili.com/164106011/video",
            }
        self.vmid = "164106011"
    def __del__(self):
    # close connection object
        self.cursor.close()
        self.conn.close()
    def insert_testdata(self):
        sql = """select count(*) from bilibili;"""
        self.cursor.execute(sql)
        countNum = self.cursor.fetchall()[0][0]
        if countNum <= 5:
            for i in range(5 - countNum):
                self.insert_to_database(1000*i,10*i,10*i,1*i)
                self.conn.commit()
                print("已插入测试数据")
        
    def insert_to_database(self,view,follower,likes,video_count):
    # 
        sql = """INSERT INTO bilibili (view,follower,likes,video_count) VALUES ( %d, %d,%d, %d) """
        data = (view,follower,likes,video_count)
        self.cursor.execute(sql % data)
        print("已插入今日数据")
    def select_data(self):
        sql = """select * from bilibili order by id DESC limit 6;"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def spider_get_data(self):
        follower = json.loads(requests.get("https://api.bilibili.com/x/relation/stat?vmid="+self.vmid,headers=self.headers).text)["data"]["follower"]
        upstat = json.loads(requests.get("https://api.bilibili.com/x/space/upstat?mid="+self.vmid,headers=self.headers).text)["data"]
        view = upstat["archive"]["view"]
        likes = upstat["likes"]
        video_count = json.loads(requests.get("http://api.bilibili.com/x/space/navnum?mid="+self.vmid,headers=self.headers).text)["data"]["video"]
        self.insert_to_database(view,follower,likes,video_count)
        self.conn.commit()
def main():
    bilibili = spider()
    # bilibili.spider()

if __name__ == '__main__':
    main()