#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    crashTimes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    f = open(filename, 'r')
    toParse = list(csv.reader(f))
    toParse = toParse[1:]
    for row in toParse:
        if not row[1]:
            continue
        if '\'' in row[1]:
            continue
        if '.' in row[1]:
            continue
        if 'c' in row[1]:
            continue
        thisTime = row[1].split(":")
        if(not (len(thisTime) == 2)):
            continue
    
        thisHour = thisTime[0]
        intHour = int(thisHour)
        if (intHour > 23 or intHour < 0):
            continue
        crashTimes[intHour] = crashTimes[intHour] + 1
    return crashTimes


def weigh_pokemons(filename, checkWeight):
    with open(filename) as f:
        pokeTable = json.load(f)
    returnList = []
    for row in pokeTable['pokemon']:
        weightSplit = row['weight'].split(" ")
        weight = float(weightSplit[0])
        if (weight == checkWeight):
            returnList.append(row['name'])
    return returnList

def single_type_candy_count(filename):
    with open(filename) as f:
        pokeTable = json.load(f)
    sum = 0
    for row in pokeTable['pokemon']:
        if len(row['type']) == 1:
            if ('candy_count' in row):
                sum = sum + row['candy_count']
    return sum

def reflections_and_projections(points):
    points[1,:] = 1 - (points[1,:] - 1)
    points = np.vstack((-points[1,:],points[0,:]))
    multArr = np.array([[1, 3], [3, 9]], np.int32)
    points = (1/10) * np.matmul(multArr,points)
    return points

def normalize(image):
    max = np.max(image)
    min = np.min(image)
    retImage = (255/(max-min)) * (image - min)
    return retImage

def sigmoid_normalize(image, a):
    retImage = 255 / (1 + np.exp( -(1/a) * (image - 128)))
    return retImage
