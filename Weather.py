'''
Example of web scraping
Program that fetches the weather in the current location
Https://darksky.net/
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser
import datetime

url = "https://darksky.net/"
content = urlopen(url).read()
soup = BeautifulSoup(content, features="html.parser")

now = datetime.datetime.now()

mainloop = True

# prints welcome to the program
print("Welcome to this Weather Station Program!")
# prints info
print("Today: " + str(now.month) + " " + str(now.day) + " " + str(now.year))
# Summary temp
sum_temp = soup.find('span', {'class': 'summary swap'})
print(sum_temp.text)
# Feels like
feels_like = soup.find('span', {'class': 'feels-like-text'})
print("Feels like: " + feels_like.text)
# Low
low = soup.find('span', {'class': 'low-temp-text'})
print("Low: " + low.text)
# High
high = soup.find('span', {'class': 'high-temp-text'})
print("High: " + high.text)
# Summary desc
sum_desc = soup.find('span', {'class': 'currently__summary next swap'})
print("Summary: " + sum_desc.text)


# loops
while mainloop:
	
	# checks for quit event
	user_input = input("What do you want to do now?")
	if user_input == "q":
		print("Bye")
		mainloop = False
	elif user_input == "w":
		# Week summary
		print("Summary for the week!")
		week = soup.find("div", {"id": "week"})
		summary = week.findChild("div", {"class": "summary"})
		print(summary.text)
		# Print each day low and high
		days = week.findChildren("a", {"class": "day"})
		print("Day |  Low  | High")
		for day in days:
			day_name = day.findChild("span", {"class": "name"})
			day_low = day.findChild("span", {"class": "minTemp"})
			day_high = day.findChild("span", {"class": "maxTemp"})
			print(day_name.text + " | " + day_low.text + " | " + day_high.text)
	elif user_input == "o":
		# open web page
		webbrowser.open(url)
	elif user_input == "h":
		print("HELP")
		print("q : quits the program")
		print("w : prints summary for the week")
		print("o : opens the webpage on the browser")
	else:
		print("Invalid input! Please type h for help on commands")
