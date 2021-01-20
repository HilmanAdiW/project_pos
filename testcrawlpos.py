from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd, numpy as np
import math
import pyodbc 
import time

regional=['20004','25004','30004','10004','40004','50004','60004','70704','80004','90004','99004']
nopenlist=[]
for j in range (10,11):
    html = urlopen('http://kantorpos.posindonesia.co.id/unitlayananposlist.php?x_Divre='+regional[j]+'&z_Divre=%3D&cmd=search')
    bsObj = BeautifulSoup(html.read());
    body = bsObj.find('body')
    page = body.find('div', attrs={'class':'ewPager ewRec'}).text
    pageno = page.split("\xa0")[5]
    pagenum =  math.ceil(int(pageno)/20)

    for k in range(1,pagenum+1):
        html = urlopen('http://kantorpos.posindonesia.co.id/unitlayananposlist.php?x_Divre='+regional[j]+'&pageno='+str(k)+'&z_Divre=%3D&cmd=search')
        bsObj = BeautifulSoup(html.read());
        body = bsObj.find('body')
        for row in body.findAll('span', attrs = {'class':'unitlayananpos_Nomor_Dirian'}):
            nopenlist.append(row.text.replace('\n\r\n','').replace('\n',''))