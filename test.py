from ctypes import resize
import os
from urllib.parse import unquote
import requests
from tqdm import tqdm
import time

OS_SEP = os.sep

headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
root = os.getcwd()
num = 0
with open (root +'/wrong_url.txt',"a") as f3:
    #用来存放无效url
    
    with open(root +'/value_url.txt',"r",encoding = "utf-8") as f1:
        #读取已经去重的url
        for url in tqdm(f1):
            for i in range(10):
                try:
                    res = requests.get(url[:-1], headers=headers)
                    # print(res.headers)
                    
                    filename = res.headers['Content-Disposition'].split('=')[-1]
                    realname = unquote(filename)

                    trc_name = os.path.join(root, 'file', realname)
                    with open(trc_name,"wb+") as f2:
                        f2.write(res.content)

                except KeyError as e:
                    print('KeyError:', e,'返回值中没有content-disposition，对应的url为：',url[:-1])
                    f3.write(url)
                    break
                except ConnectionError as e:
                    if i >= 9:
                        print('ConnectionError:', e,'对应的url为：',url[:-1])
                    else:
                        time.sleep(0.5)
                # except Exception as e:
                #     num += 1
                #     print(num,e)
                else:
                    time.sleep(0.1)
                    break
                    







