import azapi
action = 0
API = azapi.AZlyrics('google', accuracy=0.5)

def fetcher(artist):
    API.artist = artist
    API.getLyrics(save=True, ext='lrc')
    print(f"{API.lyrics}\n")
    print(f"{API.title} by {API.artist}")
