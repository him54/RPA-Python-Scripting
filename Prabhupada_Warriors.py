import csv
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import 
from bs4 import BeautifulSoup
import requests


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://prabhupadavani.org/audio/'))
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

        data_button = QAction('Extract Data', self)
        data_button.triggered.connect(self.extract_data)
        navigation_bar.addAction(data_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigation_bar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://prabhupadavani.org/audio/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def extract_data(self):
        # Extract Bhagavad Gita lectures data
        self.extract_lectures_data('Bhagavad Gita', 'https://prabhupadavani.org/audio/bhagavad-gita')

        # Extract Srimad Bhagavatam lectures data
        self.extract_lectures_data('Srimad Bhagavatam', 'https://prabhupadavani.org/audio/srimad-bhagavatam')

    def extract_lectures_data(self, category, url):
        # Create a BeautifulSoup object by requesting the website content
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        # Extract links to all audio recordings
        links = []
        for div in soup.find_all('div', {'class': 'media-library-single'}):
            link = div.find('a').get('href')
            links.append(link)

        # Extract data from each recording and save to a CSV file
        filename = category.lower().replace(' ', '_') + '_data.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Speaker', 'Date', 'Length'])

            for link in links:
                # Load individual recording page
                html = requests.get(link).text
                soup = BeautifulSoup(html, 'html.parser')

                # Extract desired data from page
                title = soup.find('h2', {'class': 'media-library-title'}).text.strip()
                speaker = soup.find('div', {'class': 'media-library-meta-speaker'}).text.strip()
                date = soup.find('div', {'class': 'media-library-meta-date'}).text.strip()
                length = soup.find('div', {'class': 'media-library-meta-length'}).text.strip()

                # Write data to CSV file
                writer.writerow([title, speaker, date, length])

app = QApplication(sys.argv)
QApplication.setApplicationName('Prabhupada_Warriors')
main = Window()
app.exec_()
