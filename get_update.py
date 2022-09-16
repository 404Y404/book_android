import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

base=open("base.py",'w')
options = webdriver.ChromeOptions()
options.add_argument('headless')
#chrome_options=options
browser = webdriver.Chrome(chrome_options=options)
base.write("base={")
def selen(link):
	try:
		browser.get(link)
		return(str(browser.find_element(By.CSS_SELECTOR, '[id="jp_audio_0"]').get_attribute("src")))
	except:
		pass
start_link="https://audioknigi.media/author/%D0%94%D0%BE%D0%BD%D1%86%D0%BE%D0%B2%D0%B0%20%D0%94%D0%B0%D1%80%D1%8C%D1%8F/page{}/"

for i in range(1,8):
	r=requests.get(start_link.format(str(i)))
	soup=BeautifulSoup(r.text, "html.parser")
	books=soup.select(".topic-title>a")
	for book in books:
		link=selen(book.get('href'))
		if link!=None:
			base.write(f"'{book.text}':'{link}', ")
	print(f'страница {i} добавлена')
base.write("'':''}")
browser.quit()