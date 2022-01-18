"""
 -*- coding: utf-8 -*-
 author： Hao Hu
 @date   2022/1/18 10:32 PM
"""

# coding:utf-8
import requests
import urllib3
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_all_websites():
    # url = "https://www.baidu.com"
    web_list = []
    with open('./web.txt','r') as f:
        contents = f.readlines()
    for sample in contents:
        web_list.append(sample)
    # for url in web_list:
    #     html_content = requests.get(url).text
    #     soup = BeautifulSoup(html_content, "html.parser")
    #     # find_all会将所有满足条件的值取出，组成一个list
    #     link_nodes = soup.find_all("a")
    #     for node in link_nodes:
    #         print(node.get("href"))

    return web_list



def visit_website():
    http = urllib3.PoolManager(num_pools=5, headers={'User-Agent': 'ABCDE'})
    web_list = get_all_websites()
    for str in tqdm(web_list):
        # web_list为存储了网址的列表，通过http.request可以访问指定的网址
        resp1 = http.request('GET', str)


visit_website()