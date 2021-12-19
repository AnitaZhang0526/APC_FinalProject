# scrape_xrd.py
# 
# This script populates the local XRD peak-matching database.
# It scrapes the website webmineral.com to populate a local csv
# file. The csv file will be stored under version control and
# the expectation is that this script will only be run if the 
# database needs to be updated with new data from the website.

import csv
import re
import requests
from bs4 import BeautifulSoup

# ---------- CONSTANTS ---------- #

# File path of the local database
FILE_PATH = "../databases/xrd.csv"

# Base url of the website to be scraped
BASE_URL = "http://www.webmineral.com/MySQL/xray.php?st="

# Number of expected records from the webmineral.com
# This dicates how many pages will be scraped and 
# should be manually updated if the number of records
# on webmineral.com changes.
NUM_RECORDS = 6424

# Number of records per page on webmineral.com
RECORDS_PER_PAGE = 100

HEADER_ROW = [
    "2_theta_1",
    "intensity_1",
    "2_theta_2",
    "intensity_2",
    "2_theta_3",
    "intensity_3",
    "material_name",
    "material_formula"
]

# ---------- END CONSTANTS ---------- #


# Open csv file
file = open(FILE_PATH, "w")
writer = csv.writer(file)

# Write header row to csv
writer.writerow(HEADER_ROW)

# Keep track of materials that have already been added to the database
# to avoid duplicates
seen_materials = []

# Fetch each page and write records to csv
for i in range(1, NUM_RECORDS, RECORDS_PER_PAGE):

    # Fetch the page
    url = BASE_URL + str(i)
    print("Fetching", url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Get table with XRD data
    table = soup.find_all("table")[6]

    # Loop through each row in table
    for i, j in enumerate(table.find_all("tr")):

        # Skip the header row
        if i == 0:
            continue

        # Create a list to store row data to write to csv
        row = []

        # Get a list of all td elements in the row
        tds = j.find_all("td")

        # If this material has already been added to the database,
        # don't add it again.
        material_name = tds[6]
        if material_name in seen_materials:
            continue;

        # Keep track of materials that have already been added to the database
        seen_materials.append(material_name)

        # Loop through each cell in the row
        for m, n in enumerate(tds):

            # The data for 2_theta_{1,2,3} needs to be parsed
            if m == 0 or m == 2 or m == 4:
                row.append(re.search(r'\((.*?)\)',n.text).group(1))
            # All other cells can be stored as-is
            else:
                row.append(n.text)

        # Don't add rows with non-float data in columns that should
        # have floats (2_thetas and intensities)
        bad_data = False
        for cell in row[:6]:
            try:
                float(cell)
            except ValueError:
                bad_data = True

        if not bad_data:
            # Write row to csv
            writer.writerow(row)

# Close csv file
file.close()