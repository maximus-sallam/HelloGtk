import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Notebook Demo")
        self.set_border_width(10)



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()