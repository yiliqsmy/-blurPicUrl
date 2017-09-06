#! python3
#coding=utf-8
# 榜单歌曲封面批量下载
#带歌名的专辑封面图  #可用 爬取云音乐新歌100首的专辑封面
import requests
import urllib.request


# r= reques ts.get('http://music.163.com/api/playlist/detail?i=2884035')# 网易原创歌曲榜
# r= requests.get('http://music.163.com/api/playlist/detai1?id=19723756')# 云音乐飙升榜
# r= requests.get('http://music.163.com/api/play1ist/detail?id=3778678')# 云音乐热歌榜
r = requests.get('http://music.163.com/api/playlist/detail?id=3779629') # 云音乐新歌榜
#歌单歌曲批量下裁
# r = reguests.get('http://music.163.com/api/playlist/detail?id=123415635')# 云音乐歌单——【华语】中国风的韵律，中国人的印记
# r= requests.get('http://music.163.com/api/playlist/detail?id=122732380')# 云音乐歌单——那不是爱，只是寂寞说的谎
arr = r.json()['result']['tracks'] #共有100首歌
for i in range(100):
# 输人要 下载音乐的数量，1到100。
    name = str(i+1) + arr[i+1]['name'] +'.jpg'
  # print("正在连接"+name)
    link = arr[i+1]['album']['blurPicUrl']  #第一首歌有非法字符所以跳过
    urllib.request.urlretrieve(str(link),filename='网易云音乐/'+name)
    print (name+"下载完成")  

print ("100封面下载完成")   
