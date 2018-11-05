import os.path
import abc


class Gif(abc.ABC):

    def __init__(self, path):
        self.name = os.path.basename(path)
        self.dir = 'gifs/'
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
        """ saves the reversed gif and returns the path"""
        name,ext = os.path.splitext(self.name)
        new_path = os.path.join(self.dir, name + "_reversed" + ext) 
        self.write_gif(new_path, self.reversed_frames)
        return new_path
