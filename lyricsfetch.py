import azapi
action = 0
API = azapi.AZlyrics('google', accuracy=0.5)
def fetcher(artist):
    API.artist = artist
    API.getLyrics(save=False, ext='lrc')
    global fetchedLyrics
    global musicDetails
    fetchedLyrics =(f"{API.lyrics}\n")
    musicDetails = (f"{API.title} by {API.artist}")
    return fetchedLyrics,musicDetails
