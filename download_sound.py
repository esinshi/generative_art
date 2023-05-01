import youtube_dl

# Set the SoundCloud track URL
soundcloud_track_url = 'https://soundcloud.com/zheeze/claudia'

# Configure the options for downloading audio
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Download the audio track
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([soundcloud_track_url])
