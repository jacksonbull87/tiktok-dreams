
import requests
import re
import pandas as pd


def get_api_token(REFRESH_TOKEN):
    api_url = 'https://api.chartmetric.com/api/token'
    
    response = requests.post(url=api_url, data={'refreshtoken' : REFRESH_TOKEN}, 
                             json={'Content-Type' : 'application/json'})
    results = response.json()
    api_token = results['token']
    return api_token

##################################################################################
def search(api_token, track_name, artist_name, search_type='tracks', limit=10):
    #returns dataframe of all tracks that satisfy user search criteria
    response = requests.get(url='https://api.chartmetric.com/api/search',
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}, 
                            params={'q':track_name, 'type':search_type, 'limit':limit})
    if response.status_code == 200:

        data = response.json()
        track = data['obj']
        
        data_bucket = []
        for item in track['tracks']:

            if re.match(track_name.lower(), item['name'].lower()) and re.match(artist_name.lower(), item['artist_names'][0].lower()):
                track_tuple = (item['isrc'], item['name'], item['cm_track'], item['artist_names'][0], item['album_names'][0], 
                              item['release_dates'][0])
                data_bucket.append(track_tuple)

                print("isrc #: ", item['isrc'])
                print("track name : ", item['name'])
                print("chartmetric ID : ", item['cm_track'])
                print("artist name : ", item['artist_names'][0])
                print("album name : ", item['album_names'][0])
                print("release date : ", item['release_dates'][0])
                print('\n')

        return pd.DataFrame(data_bucket, columns=['isrc', 'track', 'chartmetric id', 'artist', 'album', 'release date'])
    else:
        pass

def get_track_metadata(api_token, cm_track_id):
    #cm_track_id refers to the chartmetric track id associated with the song
    #returns a dictionary('id', 'name', 'isrc', 'image_url', 'duration_ms', 'composer_name', 
    #'artists', 'albums', 'tags', 'cm_audio_features', 'release_date', 'lastfm', 'cm_statistics')
    response = requests.get(url='https://api.chartmetric.com/api/track/{}'.format(cm_track_id),
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}
                                )
    if response.status_code == 200:

        data = response.json()
        track = data['obj']
    else:
        pass
    return track

def get_chart_data(api_token, cm_track_id, chart_type, date):
    #refer to https://api.chartmetric.com/apidoc/#api-Track-getTrackCharts for allowed values for chart_type
    #date == YYYY-MM-DD
    #returns a list of dictionaries with chart data for each date
    response = requests.get(url='https://api.chartmetric.com/api/track/{}/{}/charts'.format(cm_track_id, chart_type),
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}, params={'since': date}
                                )
    if response.status_code == 200:
        data = response.json()
        chart = data['obj']
        return chart['data']

def get_tiktok_chart_data(api_token, chart_type, date, interval, limit=100):
    #for apitoken import get_import_token
    #for chart_type, accepted values include 'tracks', 'videos', 'users'
    #date == YYYY-MM-DD
    #for interval, accepted values include 'daily', 'weekly'
    #returns a list of song metadata
    response = requests.get(url='https://api.chartmetric.com/api/charts/tiktok/{}'.format(chart_type),
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}, params={'date': date, 'interval': interval, 'limit': limit}
                                )
    if response.status_code == 200:
        data = response.json()
        chart = data['obj']
        return chart['data']


def get_track_chart(api_token, cm_id, chart_type, since):
    response = requests.get(url='https://api.chartmetric.com/api/track/{}/{}/charts'.format(cm_id, chart_type),
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}, params={'since':since}
                                )
    if response.status_code == 200:
        data = response.json()
        chart = data['obj']
        return chart['data']
    else:
        print("Artist ID: ", cm_id)
        print(response.status_code)
        print(response.text)


def get_track_playlist(api_token, cm_id, platform, status, since, limit):
    response = requests.get(url='https://api.chartmetric.com/api/track/{}/{}/{}/playlists'.format(cm_id, platform, status),
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}, params={'since':since, 'limit': limit}
                                )
    if response.status_code == 200:
        data = response.json()
        chart = data['obj']
        return chart
    else:
        print("Artist ID: ", cm_id)
        print(response.status_code)
        print(response.text)


def get_artist_id(api_token, q, search_type):
    #return tuple (artist name, artist cm id)
    response = requests.get(url='https://api.chartmetric.com/api/search',
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}, params={'q': q, 'type': search_type}
                                )
    if response.status_code == 200:
        data = response.json()
        try:
            chart = data['obj']
            for artist in chart['artists']:
                if re.fullmatch(q.lower(), artist['name'].lower()):
                    # print(artist['name'])
                    # print('Chartmetric ID: ',artist['id'])
                    return artist['id']
                else:
                    continue
            
        except TypeError:
            return "None"
    else:
        print(response.status_code)
        print(response.text)

def get_fan_metrics(api_token, cm_artist_id, source, since_date, field=None):
    #returns a list of dictionaries, each item being a different timestamp
    response = requests.get(url='https://api.chartmetric.com/api/artist/{}/stat/{}'.format(cm_artist_id, source),
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}, params={'since': since_date, 'field': field}
                                )
    if response.status_code == 200:
        data = response.json()
        try:
            chart = data['obj']
            return chart
            
        except TypeError:
            return "None"
    else:
        print("Artist ID: ", cm_artist_id)
        print(response.status_code)
        print(response.text)

def get_instagram_audience(api_token, cm_artist_id):
    #returns a list of dictionaries, each item being a different timestamp
    response = requests.get(url='https://api.chartmetric.com/api/artist/{}/instagram-audience-stats'.format(cm_artist_id),
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}
                                )
    if response.status_code == 200:
        data = response.json()
        try:
            chart = data['obj']
            return chart
            
        except TypeError:
            return "None"
    else:
        print(cm_artist_id)
        print(response.status_code)
        print(response.text)

