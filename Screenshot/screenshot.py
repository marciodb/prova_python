from Xlib import display, X
import PIL


class screenshot:

    def Print(self):

        W,H = 200,200
        dsp = display.Display()
        root = dsp.screen().root
        raw = root.get_image(0, 0, W,H, X.ZPixmap, 0xffffffff)
        image = Image.fromstring("RGB", (W, H), raw.data, "raw", "BGRX")
        image.show()