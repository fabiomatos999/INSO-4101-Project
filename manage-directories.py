#!/usr/bin/env python3

import os
from datetime import datetime
import shutil
import subprocess

class sellerInformation:
    name = ""
    email = ""
    phoneNumber = ""
    address = ""
    score = ""
    reviews = ""
    def __init__(self, name : str,email : str,phoneNumber : str):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber


class shoeEntry:
    pictures = []
    video = []
    seller = sellerInformation
    name = ""
    brand = ""
    dateAdded = datetime.now()
    def __init__(self, pictures : list, video: list, seller: sellerInformation):
        self.pictures = pictures
        self.video = video
        self.seller = seller


def crate_folder_structure(id : str, entry : shoeEntry):
    path = os.path.join(os.getcwd() ,"entries", id)
    x = 0
    os.makedirs(path,0x777,True)
    for picture in entry.pictures:
        dest = path + "/" + "P" + str(x) + os.path.splitext(picture)[1]
        os.rename(picture,dest)
        x+=1
    x = 0
    for video in entry.video:
        dest = path + "/" + "V" + str(x) + os.path.splitext(video)[1]
        shutil.move(video,dest)
        x+=1

    return None

pictures = [os.path.abspath("test1.png"),os.path.abspath("test2.png")]
videos = [os.path.abspath("Yuuki Yuuna wa Yusha de Aru OP.mkv")]
seller = sellerInformation("UwU", "uwu@uwu.uwu", "1800-uwu-uwu")
shoe = shoeEntry(pictures, videos, seller)
crate_folder_structure("10",shoe)
