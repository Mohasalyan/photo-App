import os

def getFilters():
    filters = []
    for i in os.listdir('images/Filters'):
        filters.append({'src':f"images/Filters/{i}",'name':f"{i.split('.')[0]}"})
    return filters


def getFrames():
    frames =[]
    for i in os.listdir('images/Frames'):
        frames.append({'src':f"images/Frames/{i}",'name':f"{i.split('.')[0]}"})
    return frames

def getStickers():
    stickers=[]
    for i in os.listdir('images/Stickers'):
        stickers.append({'src':f"images/Stickers/{i}",'name':f"{i.split('.')[0]}"})
    return stickers