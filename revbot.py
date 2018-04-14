import imgur_client
import praw
import json
import imageiogif
from collections import namedtuple
import re

VERSION = 'v0.1'
class RevBot:
    OAUTH_INFO_FILE = 'oauth_info.json'
    WATCHED_SUBREDDITS_FILE = 'watched.json'
    USER_AGENT = 'python:revbot{version} (by /u/Tadaboody)'.format(version=VERSION)
    ACTIVATING_PHRASES = ['!rev','!reverse','reverse','!revbot','reversed']
    def __init__(self):
        with open(self.OAUTH_INFO_FILE) as fp:
            oauth_info = json.load(fp)
        self.reddit = praw.Reddit(**oauth_info['reddit'])
        self.imgur = imgur_client.Imgur(**oauth_info['imgur'])
        with open(self.WATCHED_SUBREDDITS_FILE) as fp:
            self.watched_subreddits = json.load(fp)
        
    @staticmethod
    def download_gif(url : str) -> imageiogif.ImageIOGif:
        return imageiogif.ImageIOGif.from_url(url)
    
    @staticmethod
    def reply_string(image_url):
        return """here's a reversed version of this gif:  
        ({image_url})[Link]  
        visit me at /r/revbot"""

    GIF_SITES = ['giphy']
    @staticmethod
    def contains_gif(url):
        return any(site in url for site in RevBot.GIF_SITES) or url.endswith('.gif')

    def reply_comment(self,comment):
        gif_bearer = comment.parent()
        try:
            gif_bearer.refresh() # Comments are lazily evaluated
        finally:
            if not RevBot.contains_gif(gif_bearer):
                gif_bearer = comment.submission
                if not RevBot.contains_gif(gif_bearer):
                    raise ValueError("post did not contain gifs")
        gif = RevBot.download_gif(RevBot.extract_gif(gif_bearer))
        reversed_image = self.imgur.upload_image(gif.write_reversed())
        gif_bearer.reply(RevBot.reply_string(reversed_image['url']))
        
    @staticmethod
    def extract_gif(url:str) -> str:
        if url.endswith('.gif'):
            return url
        giphy_match = re.match(r'giphy.com/gifs/(\w+)$',url)
        if giphy_match:
            return """media.giphy.com/media/{id}/giphy.gif""".format(id=giphy_match[1])

    @staticmethod
    def is_RevBot_called(comment):
        return any(phrase in comment for phrase in RevBot.ACTIVATING_PHRASES)
    
    def comment_stream(self):
        all_subreddits = self.reddit.subreddit('+'.join(self.watched_subreddits))
        return all_subreddits.stream.comments()
    
    def run(self):
        for comment in self.comment_stream(): 
            if RevBot.is_RevBot_called(comment):
                self.reply_comment(comment)