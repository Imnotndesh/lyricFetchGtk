import gi
gi.require_version("Gtk","3.0")
import lyricsFetchApi

from gi.repository import Gtk
from lyricsFetchApi import fetcher

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
    def on_usrSong_activate(self,usrSong):
        self.song = usrSong.get_text()

        fetcher(title=self.song)
        lyricsText.set_text(lyricsFetchApi.fetchedLyrics)


    def on_saveToFile_toggled(self,saveToFile):
        lyricsFetchApi.saveState = True
        print(f"Savestate is set to :{lyricsFetchApi.saveState}")
        
    
global builder
builder = Gtk.Builder()
builder.add_from_file("lyricsFetchUi.glade")
window = builder.get_object("mainWin")
global lyricsText
lyricsText = builder.get_object("lyricText")
builder.connect_signals(Handler())
window.show_all()
Gtk.main()