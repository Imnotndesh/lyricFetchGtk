import gi
gi.require_version('Gtk','4.0')
gi.require_version('Gdk','4.0')
from gi.repository import Gtk,Gdk

builder = Gtk.Builder()
def app_resources():
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path('lyricFetchGtk/main.css')
    Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    builder.add_from_file("lyricFetchGtk/lyricsFetchGtk")

