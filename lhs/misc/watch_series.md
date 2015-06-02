Watch Series
============

'watch_series' - Watch TV series in your native video player.


Synopsis
--------

```bash
$ watch_series series season episode [dl]
```


Description
-----------

watch_series downloads the specified episode of a series from a website and
plays it in your local media player. The default media player is set to mpv.

### How to use

The first argument should be a series name in the format the website uses to
access it. The second argument should be the season number to pull from, and
the third argument should be the episode to download. The fourth argument is
optional and can be used to download the file instead of playing it.

### How it works

This script takes the base url (specified at the beginning of the script), the
series name, the season, and the episode then builds the page url from that.
The page content is downloaded with 'curl' then inspected.

In the script is a list of video sites to try (like videoweed, novamov,
etc...). The page is searched for each of the sites, the first hit returns the
link to the video page. That link is passed to 'youtube-dl', which either
downloads the video itself, or generates the URL necessary to pass to 'mpv' to
play the video.


Options
-------

-   dl: If the fourth argument is set to 'dl', the episode will be downloaded to
    "\$XDG_MEDIA_DIR/series/\$WS_SERIES_NAME", where "\$WS_SERIES_NAME" holds the
    name of the series.

Any extra arguments (past 4) will be passed to the media player.


Environment
-----------

-   XDG_MEDIA_DIR:  If set, the script will download to "\$XDG_MEDIA_DIR/series"
    if 'dl' is specified. If not set, the default is "\$HOME/media/series".

-   XDG_MEDIA_PLAYER:   If set, the script will use the given command as the
    media player. If not set the default is 'mpv'.


Examples
--------

Watch Parks and Recreation, Season 2, Episode 12

```bash
$ watch_series 'parks_and_recreation' 2 12
```

Watch House, Season 3, Episode 4

```bash
$ watch_series 'house' 3 4
```

Download Parks and Recreation, Season 2, Episode 12

```bash
$ watch_series 'parks_and_recreation' 2 12 dl
```


Known Issues
------------

### Site URL Changes

This script breaks any time the site url changes (so when it gets taken down).
To fix it, simply Google 'watch series online' and figure out what the new url
is and replace the line 'URL=' at the beginning of the script with the new one.

### Site format Changes

If the site format changes (it displays links differently), the script may also
break. Because it's largely based on heuristics, this means you have to figure
out how the new format breaks the parsing and fix it.


Dependencies
------------

### Hard

-   [youtube-dl](http://rg3.github.io/youtube-dl/): Program which parses
    webpages and grabs the URL for a video playing on that webpage.

### Soft

-   [curl](http://curl.haxx.se/): Program which grabs a webpage and prints it to
    stdout. This is a soft dependency because the program could be made to work
    with wget instead.
-   [mpv](http://mpv.io/): Simple media player which is a form of mplayer2 and
    MPlayer. This is a soft dependency because the program could be made to work
    with any media player, or made to download the videos with youtube-dl
    instead.
