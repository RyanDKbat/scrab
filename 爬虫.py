from selenium import webdriver
import csv

# 网易云音乐的第一个歌单url
url = 'http://music.163.com/#/discover/playlist/' \
      '?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
# PhantomJS接口创建webdriver
 driver = webdriver.PhantomJS()

 csv_file = open("playlist.csv","w",newline='')
 writer = csv

