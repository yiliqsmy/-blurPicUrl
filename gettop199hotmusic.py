#! python3 可用
#coding=utf-8
# 可用 爬取网易原创歌曲榜100首，只有歌名
#一首歌曲，一换行
import requests
def writeToTxt(list_name, file_path):
    try:
        fp = open(file_path, "w", encoding='utf-8')
        for item in list_name:
            fp.write(str(item) + "\n")  #list中一项占一行
        fp.close()
    except IOError:
        print("打开文件失败")


if __name__ == "__main__":
    r = requests.get('http://music.163.com/api/playlist/detail?id=3778678')  # 云音乐热歌榜
    arr = r.json()['result']['tracks']  # 共有1200首歌
    content = []
    for i in range(199):
        # 输人要 下载音乐的数量，1到200。
        namelist = arr[i]['name']
        song_name =str(i + 1) + '.' +namelist
        content.append(song_name)
    print(content)
    file_path = r"199hotsong.txt"
    writeToTxt(content, file_path)
    print("199歌名下载完成")
