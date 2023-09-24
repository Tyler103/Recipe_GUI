from isoduration import parse_duration
import urllib.request
from PIL import Image


class Recipe:

    def __init__(self, n, cook_t, prep_t, rec_yield):
        self._name = n
        self._cook_time = cook_t
        self._prep_time = prep_t
        self._yield = rec_yield
        self._image = None

        self._com = 0
        self._com2 = 10

    def get_name(self):
        return self._name[0:25]

    def get_cook_time(self):
        if self._cook_time == '':
            time = "00"
            return f"{time}:{time}"
        else:
            duration = parse_duration(self._cook_time)
            time_1 = duration.time
            hh = time_1.hours
            mm = time_1.minutes

            if hh != self._com:
                return f"0{hh}:0{mm}"
            else:
                if mm >= self._com2:
                    return f"{hh}0:{mm}"
                else:
                    return f"{hh}0:0{mm}"

    def get_prep_time(self):
        if self._prep_time == '':
            set_time = "00"
            return f"{set_time}:{set_time}"
        else:
            duration = parse_duration(self._prep_time)
            time_1 = duration.time
            hh = time_1.hours
            mm = time_1.minutes

            if hh != self._com:
                return f"0{hh}:0{mm}"
            else:
                if mm >= self._com2:
                    return f"{hh}0:{mm}"
                else:
                    return f"{hh}0:0{mm}"

    def get_recipe_yield(self):
        return self._yield[0:25]

    def set_image(self, url):

        high_index = url.rfind("/")
        nam = url[high_index + 1:]
        first_index = nam.index(".")
        filename = nam.replace(nam[first_index + 1:], "gif")

        req = urllib.request.Request(url)
        your_img = urllib.request.urlopen(req)

        img = Image.open(your_img)
        scaled_width = 200
        percent_width = (scaled_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(percent_width)))
        img = img.resize((scaled_width, h_size), Image.ANTIALIAS)
        img.save("GIF_files/" + filename)

        self._image = "GIF_files/" + filename

    def get_image(self):
        return self._image
