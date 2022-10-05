
import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

base_url = "https://en.wikipedia.org/wiki/RuPaul%27s_Drag_Race_All_Stars_(season_7)"
response = requests.get(base_url)
soup = BeautifulSoup(response.text,'lxml')

#check point
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.a)

# returns a list containing all the tables in the HTML
print(soup.find_all('table'))
print(len(soup.find_all('table')))


# to pull out the elements i want from the website
drag_tables = soup.find_all('table',{'class':"wikitable"})

# store info in a list, even though it says str() (check type to confirm :) and invoke the .read_html method from pandas
# shows a count of rows and columns
drag_html = pd.read_html(str(drag_tables))

# print(drag_html)

# # convert list to dataframe
drag_df = pd.DataFrame(drag_html[1])

#checkpoint
print(drag_df.head())

# # make a copy of the info before changes are made
the_drag_df = drag_df.copy()

# i like to review the types of the variables i create
print(type(base_url))
print(type(response))
print(type(soup))
print(type(drag_tables))
print(type(drag_html))
print(type(drag_df))
print(type(the_drag_df))

# import to a csv file for further analysis
drag_df.to_csv(r'30DaysofPythonChallenge\day14_Web_scrape', index = True, header=True)

print(drag_df.head(20))
