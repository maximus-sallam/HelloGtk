from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Button Clicker 2.0")

        # Button
        self.button = Gtk.Button(label="Click me!")
        self.button.connect("clicked", self.button_clicked)
        self.add(self.button)

        # Box
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        # Bacon button
        self.bacon_button = Gtk.Button(label="Bacon")
        self.bacon_button.connect("clicked", self.bacon_clicked)
        self.box.pack_start(self.bacon_button, True, True, 0)

        # Tuna button
        self.tuna_button = Gtk.Button(label="Tuna")
        self.tuna_button.connect("clicked", self.tuna_clicked)
        self.box.pack_start(self.tuna_button, True, True, 0)

    # User clicks button
    def button_clicked(self, widget):
        print("Yay!")

    def button_clicked(self, widget):
        print("You clicked bacon.")

    def tuna_clicked(self, widget):
        print("You clicked tuna.")


# Label
#label = Gtk.Label()
#label.set_label("OMG!")
#label.set_angle(30)
#label.set_halign(Gtk.Align.END)

#print(label.get_properties("angle"))

window = MainWindow()
#window.add(label)
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()