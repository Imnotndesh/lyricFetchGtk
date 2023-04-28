import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import lyricsfetch
from lyricsfetch import fetcher

class sampleList(Gtk.Window):
    def __init__(self):
        super().__init__(title="Sample ListBox")
        self.set_border_width(10)
        self.set_size_request(640,400)

        cont1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing =5)
        self.add(cont1)
        # First Listbox
        list1 = Gtk.ListBox()
        list1.set_selection_mode(Gtk.SelectionMode.NONE)
        cont1.pack_start(list1,True,True,0)

            # Header space 
        headerRow = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        headerRow.add(hbox)
            #contents
        hLabel = Gtk.Label(label="Enter song name to find lyrics...")
        hbox.pack_start(hLabel,True,True,0)
        list1.add(headerRow)


            # First row
        inputRow = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        inputRow.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)
                #contents
        self.usrInput = Gtk.Entry()
        vbox.pack_start(self.usrInput,True,True,0)
        bttn1 = Gtk.Button(label="search")
        bttn1.props.valign= Gtk.Align.CENTER
        hbox.pack_start(bttn1,False,True,0)
        bttn1.connect("clicked",self.on_click)
        list1.add(inputRow)

            # Second Row
        lyricRow = Gtk.Box()
                # Contents
        lyricOutput = Gtk.ScrolledWindow()
        lyricOutput.set_hexpand(True)
        lyricOutput.set_max_content_height(300)


        self.lyricText = Gtk.TextView()
        self.lyricText.set_editable(False)
        self.lyricText.set_wrap_mode(Gtk.WrapMode.WORD)
        self.textbuffer = self.lyricText.get_buffer()
        
        lyricOutput.add(self.lyricText)
        lyricRow.add(lyricOutput)
        list1.add(lyricRow)        

        list1.show_all()
    def on_click(self,widget):
        artist = self.usrInput.get_text()
        fetcher(artist)
        self.textbuffer.set_text(lyricsfetch.fetchedLyrics)






win = sampleList()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()