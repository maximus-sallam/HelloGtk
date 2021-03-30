import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Label Example")
        self.set_border_width(20)
        self.set_default_size(500, 300)

        # Boxes
        hbox = Gtk.Box(spacing=20)
        hbox.set_homogeneous(False)



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()