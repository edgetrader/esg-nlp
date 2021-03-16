import os
from datetime import date
from dateutil.relativedelta import relativedelta

def getFilelist(foldername):
    filelist = []

    for dirname, _, filenames in os.walk(foldername):
        for filename in filenames:
            filelist.append(os.path.join(dirname, filename))

    return filelist

def createfolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)    