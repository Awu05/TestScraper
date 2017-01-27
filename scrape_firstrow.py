from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import webbrowser
from adblockparser import AdblockRules
from subprocess import call


#Converts the python script into an executable, this is for windows
dir = r"C:\Program Files (x86)\Python\My Scripts\Scrape Firstrow\dist"
cmdline = "scrape_firstrow.exe"
rc = call("start cmd /K " + cmdline, cwd=dir, shell=True)

#Trying to apply an adblock filter
raw_rules = []
try:
    with open('easylist.txt') as inputfile:
        for line in inputfile:
            if( ('||' in line) or ('@@' in line)):
                raw_rules.append(line)
except UnicodeDecodeError:
    pass


rules = AdblockRules(raw_rules)

'''
print (len(raw_rules))

a = 1000
while a < 1020:
print (raw_rules[a])
a += 1



raw_rules2 = ["||ads.example.com^", "@@||ads.example.com/notbanner^$~script"]
rules2 = AdblockRules(raw_rules2)


print (rules.should_block("http://103092804.com"))
print (rules2.should_block("http://ads.example.com"))
'''

#Links to scrape
sports = ["http://ifirstrowus.eu/sport/football.html", "http://ifirstrowus.eu/sport/american-football.html", "http://ifirstrowus.eu/sport/basketball.html", "http://ifirstrowus.eu/sport/rugby.html", "http://ifirstrowus.eu/sport/ice-hockey.html", "http://ifirstrowus.eu/sport/boxing-wwe-ufc.html", "http://ifirstrowus.eu/sport/tennis.html", "http://ifirstrowus.eu/sport/motosport.html", "http://ifirstrowus.eu/sport/others.html"]

sports_list = ["Soccor", "Football", "Basketball", "Rugby", "Hockey", "Boxing/WWE/UFC", "Tennis", "Motosport", "Other"]

print("The Sport Listings\n---------------------\n")


p = 0
while p < len(sports):
    print ('{0}) {1}'.format(p, sports_list[p]))
    p += 1

choice = input("Type the number of the sport would you like to watch?: ")

if(int(choice) > (len(sports_list)-1)):
    print("Invalid Input. Please Choose Again.")
else:
    #Used Beautifulsoup to scrape the link
    url = sports[int(choice)]
    #request = urllib.request.Request(url)
    response = urlopen(url)
    soup = BeautifulSoup(response, "html.parser")

    all_links = soup.find_all("a")
    bball_links = []
    for link in all_links:
        #print (link.get("href"))
        a = link.get("href")
        if('/watch' in str(a)):
            #print(a , "It worked")
            bball_links.append(a)

    print ("\nPick from the list of {0} streams:".format(sports_list[int(choice)]))
    print ("------------------------------------------")
    i = 0
    while i < len(bball_links):
        print ('{0}) {1}'.format(i, bball_links[i]))
        i+= 1


    choice2 = input("\nPlease choose your stream: ")

    if(int(choice2) > (len(bball_links)-1)):
        print("Invalid Input. Please Choose Again.")
    else:
        url = 'http://ifirstrowus.eu'
        webbrowser.open_new(url+bball_links[int(choice2)])






'''
URL Of A Stream:
http://ifirstrowus.eu/watch/408918/1/watch-nba-tv.html
'''
