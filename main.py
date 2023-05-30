import sys
import gi
import lyricsFetchApi
import styling

gi.require_version('Gtk','4.0')
gi.require_version('Adw','1')
from gi.repository import Adw,Gtk
from lyricsFetchApi import fetcher
from styling import app_resources



global builder,window
builder = Gtk.Builder()
builder.add_from_file('lyricsFetchGtk')
app_resources()


class lyricsApp(Adw.Application):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.connect('activate',self.on_activate)

    def on_activate(self,app):

    # Fetched objects
        self.window = builder.get_object("mainWin")
        usrEntry = builder.get_object("usrSong")
        saveState = builder.get_object("saveState")
        self.titleCont = builder.get_object("titlesCont")
        self.lyricCont = builder.get_object("lyricsCont")
        
    # Handler connections
        usrEntry.connect('activate',self.onUsrEntry)
        saveState.connect('toggled',self.onSaveStateTrue)
        self.window.set_application(self)
        self.window.present()

    # Styling Prefs
        maincont = builder.get_object("mainCont")
        self.titlehead = builder.get_object("titlesCont")
        searchCont = builder.get_object("searchCont")
        self.lyricsCont = builder.get_object("lyricsCont")

        self.titlehead.set_css_classes(['titleContainer'])
        searchCont.set_css_classes(['searchContainer'])
        self.lyricsCont.set_css_classes(['lyricsContainer'])
        usrEntry.set_css_classes(['searchbar'])
        maincont.set_css_classes(['mainContainer'])
    # Widget Handlers
    def onUsrEntry(self,usrEntry):

        titleBuff = self.titleCont.get_buffer()
        lyricbuff = self.lyricCont.get_buffer()

        usrSong=usrEntry.get_text()
        fetcher(title=usrSong)
        self.lyricsCont.set_css_classes(['afterFetch'])
        titleBuff.set_text(lyricsFetchApi.musicDetails)
        lyricbuff.set_text(lyricsFetchApi.fetchedLyrics)

        
    def onSaveStateTrue(self,saveState):
        lyricsFetchApi.saveState =True
        print(f"Savestate is set to : {lyricsFetchApi.saveState}")




app = lyricsApp(application_id="com.imnotndesh.lyricsfetchGtk")
app.run(sys.argv)