import cv2
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class grayProcess:
    def grayWindow_destroy_cb(self, object, data=None):
        Gtk.main_quit()

    # Choose file process
    def btnBrowser_clicked_cb(self, object, data=None):
        self.dialog = Gtk.FileChooserDialog(
            "Please Choose a File",
            None,
            Gtk.FileChooserDialog.OPEN,
            (Gtk.STOCK_CANCLE, Gtk.ResponType.CANCLE,
             Gtk.STOCK_OPEN, Gtk.ResponType.OK)
        )

        self.response = self.dialog.run()

        global url
        if self.response == Gtk.ResponseType.OK:
            self.search = self.builder.get_object("txtSearch")
            imgOri = self.builder.get_object("imgOri")
            url = self.dialog.get_filename()
            self.search.set_text(str(url))
            imgOri.set_from_file(url)

        elif self.response == Gtk.ResponseType.Cancle:
            print("Cancle Clicked")

        self.dialog.destroy()

    # Show image process
    def btnProcess_clicked_cb(self, object, data=None):
        self.img = cv2.imread(url)
        imgGray = self.builder.get_object("imgGray")
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('img/gray.jpg', self.gray)
        imgGray.set_from_file('img/gray.jpg')

    # Inisialisasi
    def __init__(self):
        self.gladefile = ("grayFrontEnd.glade")
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("grayWindow")

        self.window.show()


if __name__ == "__main__":
    main = grayProcess()
    Gtk.main()
