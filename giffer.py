import imageio
import os.path
import abc


class Gif(abc.ABC):

    def __init__(self, path):
        self.name = os.path.basename(path)
        self.dir = os.path.dirname(path)
        self.frames = self.extract_frames(path)
        self.path = path
    
    @property
    def reversed_frames(self):
        return reversed(self.frames)

    @staticmethod
    @abc.abstractmethod
    def extract_frames(path):
        ...
    
    @abc.abstractmethod
    def write_gif(self,file_name, frame_array):
        ...

    def write_reversed(self):
        name,ext = os.path.splitext(self.name)
        self.write_gif(os.path.join(self.dir, name + "_reversed" + ext), self.reversed_frames)