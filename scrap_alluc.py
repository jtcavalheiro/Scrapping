import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request
import urllib

class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
        
    def on_page_load(self):
        self.app.quit()
        
url = 'http://www.alluc.ee/stream/'
query = 'game'
url = url + query

client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')

block = soup.select("div[class=title]")

for post in block:
	print (post.getText(), post.a.get('href'))