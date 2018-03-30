import giffer
import imageio
import os
class ImageIOGif(giffer.Gif):
    def __init__(self, path):
        self.frame_array = imageio.mimread(path,memtest=False)
        
    @property
    def reversed_frames(self):
        return reversed(self.frame_array)

    @staticmethod
    def write_gif(file_name, frame_array):
        imageio.mimwrite(file_name, frame_array)

    def write_reversed(self):
        self.write_gif(os.path.join(self.dir, self.name + "_reversed"), self.reversed_frames)