import fnmatch
import requests
import re
import os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from lxml import html


while True:
    url = "https://en.oxforddictionaries.com/definition/"
    urlin = input("Enter word to find:\n- ").strip().lower().replace(" ", "")
    if (len(urlin) == 0): continue

    url += urlin
    req = Request(url)

    fail = False
    for x in range(0, 10):
        if (x == 10):
            fail = True
            break

        try:
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            break

        except: continue

    if (fail == True):
        print("Error 404\n\n")
        continue

    contents = soup.findAll(class_="semb")
    definitions = []
    takeaway = 0
    for f in range(len(contents)):
        body = contents[f].select(".iteration, .subsenseIteration, .ind")
        x = 1
        construct = ""
        for item in body:
            if (x % 2 == 0):
                construct += str(item.get_text())
                definitions.append(construct)
                construct = ""
            else: construct += str(item.get_text()) + " - "
            x += 1
        definitions.append("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        takeaway += 1

    word_bank = []
    for item in definitions:
        if (item != ""):
            word_bank.append(item)

    print("╔══════════════════════════════════════════════════════════════════\n║ Word: " + str(urlin) + "\n║ Item count: " + str(len(word_bank)-takeaway) + "\n╠══════════════════════════════════════════════════════════════════\n║ " + '\n║ '.join(word_bank) + "\n╚══════════════════════════════════════════════════════════════════")
    input("Press ENTER to Continue...")
    os.system('cls')
