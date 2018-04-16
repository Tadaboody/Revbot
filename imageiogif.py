import giffer
import imageio
import os
import requests
class ImageIOGif(giffer.Gif):
        
    @staticmethod
    def extract_frames(path):
        if path.startswith('http'):
            request = requests.get(path)
            return imageio.mimread(request.content,memtest=False) 
        return imageio.mimread(path,memtest=False)

    @staticmethod
    def write_gif(file_name, frame_array):
        imageio.mimwrite(file_name, frame_array,format="gif")

if __name__ == '__main__':
    ImageIOGif("https://upload.wikimedia.org/wikipedia/commons/2/2c/Rotating_earth_%28large%29.gif").write_reversed()