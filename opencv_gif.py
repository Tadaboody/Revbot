from giffer import Gif
import cv2

class Cv2Gif(Gif):
    def __init__(self, path):
        super().__init__(path)
        cap = cv2.VideoCapture(self.path)
        self.fourcc = cap.get(cv2.CAP_PROP_FOURCC)
        self.fps  = cap.get(cv2.CAP_PROP_FPS)
        self.frame_size = (cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cap.release()

    @staticmethod
    def gif_iterator(gif_path):
        cap =  cv2.VideoCapture(gif_path) 
        not_empty = True
        while not_empty:
            not_empty, frame = cap.read()
            if not_empty:
                yield frame
        cap.release()

    @staticmethod
    def extract_frames(path):
        return list(Cv2Gif.gif_iterator(path))
    
    def write_gif(self,path,frame_array):
        writer = cv2.VideoWriter(path,self.fourcc,int(self.fps),self.frame_size)
        for image in frame_array:
            writer.write(image)
        writer.release()

if __name__ == '__main__':
    Cv2Gif("george.gif").write_reversed()
