#!/usr/bin/env python3

import os
from datetime import datetime

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

def create_directory(id: str, entry: shoeEntry) -> shoeEntry:
    path = os.path.join(os.getcwd(),"entries")
    index = 0
    id_dir = os.path.join(path,str(id))
    ret_pictures = []
    ret_videos = []
    os.umask(0)
    os.makedirs(id_dir,0o777,True)
    for picture in entry.pictures:
        picture_path = os.path.join(id_dir,str("P"+str(index)+os.path.splitext(picture)[1]))
        ret_pictures.append(picture_path)
        os.rename(picture,picture_path)
        index += 1
    index = 0
    for video in entry.video:
        video_path = os.path.join(id_dir,str("V"+str(index)+os.path.splitext(video)[1]))
        ret_videos.append(video_path)
        os.rename(video,video_path)
        index += 1
    entry.pictures = ret_pictures
    entry.video = ret_videos
    return entry