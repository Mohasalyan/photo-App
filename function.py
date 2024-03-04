import os

def getFilters():
    filters = []
    for i in os.listdir('images/Filters'):
        filters.append({'src':f"images/Filters/{i}",'name':f"{i.split('.')[0]}"})
    return filters



