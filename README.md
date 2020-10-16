# Dreams - Fleetwood Mac
## How a 42 Year Old Song Broke Streaming Records After Viral TikTok Video
<p align="center"> 
<img src="https://media.giphy.com/media/xUOwGmRx1Tu084dBzq/source.gif">
</p>

## Introduction
It was probably 1–2 months ago when I first saw the original tiktok posting that Mick Fleetwood famously recreated. I was doing my usual bedtime routine, aimlessly scrolling through TikTok looking to be entertained. When I landed on 420doggface208's post, it didn't really strike me as anything special at first; no fancy choreographed dance, no jokes, no famous celebrity (yet)…just a guy cruising down the street on a skateboard, drinking Ocean Spray cranberry juice straight out of the carton - all while filming himself for his TikTok followers. But there was something about Stevie Nicks' cool, breezy voice that emphasized 420doggface208's carefree attitude, which I think helped resonate with nearly 5 million viewers. On a platform that is dominated by pop and hip-hop songs, the interesting question here is: How does a 42 year-old classic rock song break streaming records on a platform used mostly by kids who weren't even born when the song was first released?

<p align="center"> 
<img src="https://media.giphy.com/media/WZIafcfdBcZYykqAw5/giphy.gif">
</p>

### Timeline Milestones
- 2020-09-25: 420doggface208 posts original video on TikTok
- 2020-10-05: Mick Fleetwood recreates viral TikTok video

## Daily Spotify Playlist Adds *September*
Since there are multiple versions of Dreams available on Spotify, we're going to combine the trends from both track into one barplot.
The visualization below illustrates a side-by-side comparison of the daily total playlist adds


### Insights
- On September 25, the number of playlist adds **increased by 225%** compared to the day before
- Before the original post, the median # of daily playlist adds was 1; After, the median # was 6.5
    - **The median number of daily playlist adds increased by 550%!**

![](/images/median_playlist_adds.jpeg)

![](/images/spotify_playlistadds_bothdreams.png)

## Daily Spotify Reach *September*
After comparing the daily total number of followers of playlists that added each track, the playlists that added the 2004 Remastered
version had a significantly larger reach. So in order to visualize it, I had to rescale the y-axis (total reach) by taking the natural log.

![](/images/spotify_dailyreachlog_bothdreams.png)

There's a clear upward trend in the amount of playlist followers that both tracks are being exposed to. Let take a closer look
by creating a pivot table that shows us the median reach of both versions of the song *before* and *after* the viral TikTok video.

![](/images/pt_before_after_median_reach.png)

### Insights
After analyzing both charts, it's clear that @420doggface280's post on 9-25 initiated a domino effect of compounding growth starting 2 days later. Even though the greated hits version was added to more playlists on 9-27, 
the total number of followers that the remastered version was exposed to is +10,000% more than the reach of the greatest hits version...Not Even A Contest!


## Next Steps
There are multiple directions we can go from here, but that depends on the question being asked. IMO, with today's top 40 market being dominated by pop and hip-hop songs, are we starting to see a resurgence in rock songs or is this just a fluke? In order to find the answer, we'll need to gather historical data on the USA Top 50 playlist and then take a look at how the distribution of genre has changed over time.
However, the api I am using to collect data doesn't permit historical access to the USA Spotify Top 50. But I do have access to historical Top 200 data.
So let's  grab every weekly Spotify Top 200 chart from January 5th, 2020 (Sunday) and September 13th, 2020 (Wednesday); each chart is separated by a 7-day period.

Step 1: Create a list of dates we can make our api call with

`date_list = [str(x)[:10] for x in list(pd.date_range(start="2020-01-01",end="2020-10-15", freq="W"))]`

Step 2: Loop through `date_list` and extract every Spotify Top 200 Chart in the USA region, parse it, and save each chart as a separate csv file.

![](/images/getting_top200_data.png)

Step 3: Look at the value counts for `historic_top200usa['track_genre']`.
As you can see below, the genre tags can get quite specific. Most people probably don't know the difference between "pop" and "post-teen pop" or 
"philly rap" or "nyc rap". 

![](/images/genre_value_counts.png)

Step 4: Using the power of Regex, I created a helper function that labels each track as either "pop", "rap/hip-hop", "country", "rock" using regex


`import map_genre`

`historic_top200usa['major genre'] = historic_top200usa['track_genre'].apply(lambda x: map_genre(str(x)))`

![](/images/total_genre_counts.png)