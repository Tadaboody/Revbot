import giffer
import imageio
import os
class ImageIOGif(giffer.Gif):
        
    @staticmethod
    def extract_frames(path):
        return imageio.mimread(path,memtest=False)

    @staticmethod
    def write_gif(file_name, frame_array):
        imageio.mimwrite(file_name, frame_array,format="gif")

if __name__ == '__main__':
    ImageIOGif("george.gif").write_reversed()