import azapi
action = 0
API = azapi.AZlyrics('google')
saveState = False
def fetcher(title):
    API.title = title
    API.getLyrics(save= saveState, ext='lrc')
    global fetchedLyrics
    global musicDetails
    fetchedLyrics =(f"{API.lyrics}\n")
    musicDetails = (f"{API.title} by {API.artist}")
    return fetchedLyrics,musicDetails
