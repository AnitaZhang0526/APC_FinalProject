import csv
import re
import requests
from bs4 import BeautifulSoup

file = open("../databases/xrd.csv", "w")
writer = csv.writer(file)
header = [
	"2_theta_1",
	"intensity_1",
	"2_theta_2",
	"intensity_2",
	"2_theta_3",
	"intensity_3",
	"material_name",
	"material_formula"
]
writer.writerow(header)

MIN_PAGE_NUM = 1
NUM_RECORDS = 6424
STEP = 100

BASE_URL = "http://www.webmineral.com/MySQL/xray.php?st="

for i in range(1, NUM_RECORDS, STEP):
	url = BASE_URL + str(i)
	print("Fetching", url)
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	table_elements = soup.find_all("table")

	for i, j in enumerate(table_elements[6].find_all("tr")):
		if i == 0:
			continue
		row = []
		for m, n in enumerate(j.find_all("td")):
			if m == 0 or m == 2 or m == 4:
				# 2_theta_1, 2_theta_2, 2_theta_3
				row.append(re.search(r'\((.*?)\)',n.text).group(1))
			else:
				row.append(n.text)
		writer.writerow(row)

file.close()