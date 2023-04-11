import csv
import sys
import requests
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from bs4 import BeautifulSoup
#I have created our own browser and extracted all the lectures of Bhagavad Gita. The CSV link has also been provided."
#1-This is a Python program that uses PyQt5 and BeautifulSoup libraries to extract data from a website and save it as a CSV file.
#2-The program opens a web page in a QWebEngineView widget, and allows the user to navigate to other pages using a navigation bar.
# When the user navigates to a specific URL, the program extracts data from a table on the page and saves it as a CSV file.


  #/html/body/div[3]/div/div[2]/div[4]/div[1]/a
  #/html/body/div[3]/div/div[2]
  #//*[@id="content"]/div/div[2]/div[4]/div[1]

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://prabhupadavani.org/transcriptions/?audio=Has+audio&type=Bhagavad-gita'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navigation_bar = QToolBar()
        self.addToolBar(navigation_bar)

        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navigation_bar.addAction(back_button)

        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navigation_bar.addAction(forward_button)

        reload_button = QAction('Reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navigation_bar.addAction(reload_button)

        home_button = QAction('Home', self)
        home_button.triggered.connect(self.navigate_home)
        navigation_bar.addAction(home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigation_bar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://prabhupadavani.org/transcriptions/?audio=Has+audio&type=Bhagavad-gita'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())
        if q.toString() == 'https://prabhupadavani.org/transcriptions/?audio=Has+audio&type=Bhagavad-gita':
            self.extract_data()

    def extract_data(self):
        html = self.browser.page().toHtml(lambda data: self.process_html(data))

    def process_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', {'class': 'table table-striped table-hover'})
        rows = table.findAll('tr')
        with open('data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'Speaker', 'Date', 'Description', 'Language'])
            for row in rows:
                cols = row.findAll('td')
                if len(cols) == 5:
                    title = cols[0].text.strip()
                    speaker = cols[1].text.strip()
                    date = cols[2].text.strip()
                    description = cols[3].text.strip()
                    language = cols[4].text.strip()
                    writer.writerow([title, speaker, date, description, language])


app = QApplication(sys.argv)
QApplication.setApplicationName('Prabhupada_Warriors')
main = Window()
app.exec_()



# from lxml import html
# import requests
# import csv

# url = 'https://prabhupadavani.org/transcriptions/?audio=Has+audio&type=Bhagavad-gita'
# page = requests.get(url)
# tree = html.fromstring(page.content)

# rows = tree.xpath('//*[@id="content"]/div/div[2]/div[4]/div[1]/table/tbody/tr')
# with open('data1.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Title', 'Speaker', 'Date', 'Description', 'Language'])
#     for row in rows:
#         cols = row.xpath('td')
#         if len(cols) == 5:
#             title = cols[0].text_content().strip()
#             speaker = cols[1].text_content().strip()
#             date = cols[2].text_content().strip()
#             description = cols[3].text_content().strip()
#             language = cols[4].text_content().strip()
#             writer.writerow([title, speaker, date, description, language])
