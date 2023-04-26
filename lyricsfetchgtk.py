import gi
from lyricsfetch import fetcher
gi.require_version("Gtk",'3.0')
from gi.repository import Gtk

class mainWin(Gtk.Window):
    def __init__ (self):
        super().__init__(title="Lyrics Fetch")
        Gtk.Window.set_default_size(self, 640,100)

        # Containers
        container1 = Gtk.Box()
        self.add(container1)

        # Widgets

            # Entry Widget
        self.usrEntry = Gtk.Entry()
        self.usrEntry.set_text("")
        self.usrEntry.set_max_length(20)

            # Search Button
        srchBttn = Gtk.Button(label="Search")
        srchBttn.connect("clicked",self.on_click)

            # Alignment Defifnition
        container1.add(self.usrEntry)
        container1.add(srchBttn)


        lyricWindow = Gtk.ScrolledWindow()

        #actions
    def on_click(self,widget):
        artist = self.usrEntry.get_text()
        fetcher(artist)
        

win = mainWin()
win.connect('destroy',Gtk.main_quit)
win.show_all()
Gtk.main()