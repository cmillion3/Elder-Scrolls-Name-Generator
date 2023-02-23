import UESPnames as name
import random

# These functions take the list of prefixes and suffixes from UESPnames.py and form a name.


def altgenm():
    for i in range(5):
        print(random.choice(name.altmpre) + random.choice(name.altmsuf))


def arggenm():
    for i in range(5):
        print(random.choice(name.argmpre) + random.choice(name.argmsuf))


def bosgenm():
    for i in range(5):
        print(random.choice(name.bosmpre) + random.choice(name.bosmsuf))


def bregenm():
    for i in range(5):
        print(random.choice(name.brempre) + random.choice(name.bremsuf))


def dungenm():
    for i in range(5):
        print(random.choice(name.dunmpre) + random.choice(name.dunmsuf))


def khagenm():
    for i in range(5):
        print(random.choice(name.khampre) + random.choice(name.khamsuf))


def nordgenm():
    for i in range(5):
        print(random.choice(name.normpre) + random.choice(name.normsuf))


def redgenm():
    answer = input("Sometimes, redguard names have suffixes, but other times they do not. Would  you like a suffix? "
                   "(Recommended)(Y/N): ")
    if answer.lower() == "y":
        for i in range(5):
            print(random.choice(name.redmpre) + random.choice(name.redmv) + random.choice(name.redmc) +
                  random.choice(name.redmsuf))
    else:
        for i in range(5):
            print(random.choice(name.redmpre) + random.choice(name.redmv) + random.choice(name.redmc))


def altgenf():
    for i in range(5):
        print(random.choice(name.altfpre) + random.choice(name.altfsuf))


def arggenf():
    for i in range(5):
        print(random.choice(name.argfpre) + random.choice(name.argfsuf))


def bosgenf():
    for i in range(5):
        print(random.choice(name.bosfpre) + random.choice(name.bosfsuf))


def bregenf():
    for i in range(5):
        print(random.choice(name.brefpre) + random.choice(name.brefsuf))


def dungenf():
    for i in range(5):
        print(random.choice(name.dunfpre) + random.choice(name.dunfsuf))


def khagenf():
    for i in range(5):
        print(random.choice(name.khafpre) + random.choice(name.khafsuf))


def nordgenf():
    for i in range(5):
        print(random.choice(name.norfpre) + random.choice(name.norfsuf))


def redgenf():
    answer = input("Sometimes, female Redguard names have an extra suffix, Would you like an extra suffix? (Y/N): ")
    if answer.lower() == "y":
        for i in range(5):
            print(random.choice(name.redfpre) + random.choice(name.redfv) + random.choice(name.redfc) +
                  random.choice(name.redfsuf) + random.choice(name.redfsuf2))
    else:
        for i in range(5):
            print(random.choice(name.redfpre) + random.choice(name.redfv) + random.choice(name.redfc) +
                  random.choice(name.redfsuf2))
