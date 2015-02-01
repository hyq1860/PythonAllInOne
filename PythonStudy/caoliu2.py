import urllib3
import re
import sys
import bs4
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')
baseurl = 'http://wo.yao.cl/'
url = 'http://wo.yao.cl/thread0806.php?fid=4&page='

def write(string,page):
    f = open('D:/PythonStudio/caoliu/'+ unicode(page) +'.md','a')
    f.write(string)
    f.close()

for page in range(1,20):
    proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url + str(page))
    string = unicode(response.read(),'gbk').encode('utf-8')
    soup = BeautifulSoup(string)
    counter = soup.find_all("td", "tal f10 y-style")

    for count in counter:
        comment_num = count.find(text = re.compile(r'\d+'))

        if int(comment_num) > 500:
            count_pre = count.previous_sibling.previous_sibling.previous_sibling.previous_sibling
            name = count_pre.find('a').get_text() 
            name1 = name.encode('utf-8')
            innerurl = baseurl + count_pre.a['href']
            # print name1
            # print url
            # print comment_num
            # print "\n"
            output = '[' + name1 + ']' + '(' + innerurl + ')' + '   ' + comment_num + '\n\n\n'
            write(output,page)
