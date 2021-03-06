import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
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
        image2 = Gtk.Image.new_from_icon_name("dialog-information-symbolic.symbolic", Gtk.IconSize.MENU)
        self.notebook.append_page(self.page2, image2)

        # Third page
        self.page3 = Gtk.Box()
        self.page3.set_border_width(10)
        self.page3.add(Gtk.Label("Page 3."))
        image3 = Gtk.Image.new_from_icon_name("open-menu-symbolic", Gtk.IconSize.MENU)
        self.notebook.append_page(self.page3, image3)

        # Forth page
        self.page4 = Gtk.Box()
        self.page4.set_border_width(10)
        self.page4.add(Gtk.Label("Page 4."))
        image4 = Gtk.Image.new_from_icon_name("list-add-symbolic", Gtk.IconSize.MENU)
        self.notebook.append_page(self.page4, image4)

        # Fifth page
        self.page5 = Gtk.TextView()
        self.page5.set_border_width(20)
        self.page5.add(Gtk.Label("Page 5."))
        image5 = Gtk.Image.new_from_icon_name("list-remove-symbolic", Gtk.IconSize.MENU)
        self.notebook.append_page(self.page5, image5)

        # Header bar
        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "Max's Python Application"
        self.set_titlebar(header_bar)

        # Dialog button on right
        dialog_button = Gtk.Button()
        dialog_icon = Gio.ThemedIcon(name="dialog-information-symbolic.symbolic")
        dialog_image = Gtk.Image.new_from_gicon(dialog_icon, Gtk.IconSize.BUTTON)
        dialog_button.add(dialog_image)
        header_bar.pack_end(dialog_button)

        # Menu button on right
        menu_button = Gtk.Button()
        menu_icon = Gio.ThemedIcon(name="open-menu-symbolic")
        menu_image = Gtk.Image.new_from_gicon(menu_icon, Gtk.IconSize.BUTTON)
        menu_button.add(menu_image)
        header_bar.pack_end(menu_button)

        # Create
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        # Left arrow on left
        left_arrow = Gtk.Button()
        left_arrow.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(left_arrow)

        # Right arrow on left
        right_arrow = Gtk.Button()
        right_arrow.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        box.add(right_arrow)

        header_bar.pack_start(box)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
