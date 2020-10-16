import re


def map_genre(genre):
    #if track_genre contains "hip hop", label it as "rap/hip-hop"
    if re.search("hip hop", genre):
        return "rap/hip-hop"
    #if track_genre contains "rap", label it as "rap/hip-hop"
    elif re.search("rap", genre):
        return "rap/hip-hop"
    #if track_genre contains "pop", label it as "pop"
    elif re.search("pop", genre):
        return "pop"
    #if track_genre contains "rock", label it as "rock"
    elif re.search("rock", genre):
        return "rock"
    #if track_genre contains "country", label it as "country"
    elif re.search("country", genre):
        return "country"
    #any other genre will just be left as is
    else:
        return genre