from apiclient.discovery import build


class YoutubeSubscriberCount(object):
    def __init__(self, api_key = 'YOUR KEY '):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    @property
    def get(self):
        res = self.youtube.channels().list(id="UC_eOodxvwS_H7x2uLQa-svw", part="statistics").execute()
        return res['items'][0]['statistics']['subscriberCount']

obj = YoutubeSubscriberCount()
print("Youtube Subscribers are {}".format(obj.get))

