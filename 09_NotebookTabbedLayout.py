import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Notebook Demo")
        self.set_border_width(10)
        self.set_default_size(500, 400)
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # First page
        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label("Page 1."))
        self.notebook.append_page(self.page1, Gtk.Label("First Tab"))

        # Second page
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label("Page 2."))
        image = Gtk.Image.new_from_icon_name("dialog-information-symbolic.symbolic", Gtk.IconSize.MENU)
        self.notebook.append_page(self.page2, image)

        # Second page
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label("Page 3."))
        image = Gtk.Image.new_from_icon_name("open-menu-symbolic", Gtk.IconSize.MENU)
        self.notebook.append_page(self.page2, image)



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()