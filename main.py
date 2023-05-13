import pytube
import json
import os

class FastYoutubeConverter():
    def __init__(self, url=None):
        pass

    def download_playlist_mp3(self, url):
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        playlist = pytube.Playlist(url)

        for video in playlist.videos:
            video.streams.get_audio_only().download('downloads')

        for file in os.listdir('downloads'):
            if file.endswith('.mp4'):
                mp4_file = os.path.join('downloads', file)
                mp3_file = os.path.join('downloads', os.path.splitext(file)[0]+'.mp3')
                os.system(f'ffmpeg -i "{mp4_file}" "{mp3_file}"')
                os.remove(mp4_file)
    
    def download_playlist_wav(self, url):
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        playlist = pytube.Playlist(url)

        for video in playlist.videos:
            video.streams.get_audio_only().download('downloads')

        for file in os.listdir('downloads'):
            if file.endswith('.mp4'):
                mp4_file = os.path.join('downloads', file)
                wav_file = os.path.join('downloads', os.path.splitext(file)[0]+'.wav')
                os.system(f'ffmpeg -i "{mp4_file}" "{wav_file}"')
                os.remove(mp4_file)
    
    def download_playlist_mp4(self, url):
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        playlist = pytube.Playlist(url)

        for video in playlist.videos:
            video.streams.get_highest_resolution().download('downloads')
    
    def download_single_video_mp3(self, url):
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        video = pytube.YouTube(url)
        video.streams.get_audio_only().download('downloads')

        for file in os.listdir('downloads'):
            if file.endswith('.mp4'):
                mp4_file = os.path.join('downloads', file)
                mp3_file = os.path.join('downloads', os.path.splitext(file)[0]+'.mp3')
                os.system(f'ffmpeg -i "{mp4_file}" "{mp3_file}"')
                os.remove(mp4_file)
    
    def download_single_video_mp4(self, url):
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        video = pytube.YouTube(url)
        video.streams.get_highest_resolution().download('downloads')
    
    def download_single_video_wav(self, url):
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        video = pytube.YouTube(url)
        video.streams.get_audio_only().download('downloads')

        for file in os.listdir('downloads'):
            if file.endswith('.mp4'):
                mp4_file = os.path.join('downloads', file)
                wav_file = os.path.join('downloads', os.path.splitext(file)[0]+'.wav')
                os.system(f'ffmpeg -i "{mp4_file}" "{wav_file}"')
                os.remove(mp4_file)

if __name__ == '__main__':
    converter = FastYoutubeConverter()
    config = json.load(open('config.json'))

    download_functions = {
        'mp3': {
            True: converter.download_single_video_mp3,
            False: converter.download_playlist_mp3
        },
        'mp4': {
            True: converter.download_single_video_mp4,
            False: converter.download_playlist_mp4
        },
        'wav': {
            True: converter.download_single_video_wav,
            False: converter.download_playlist_wav
        }
    }

    download_type = config['download_type']
    single_video = config['single_video']

    if download_type in download_functions:
        download_functions[download_type][single_video](config['url'])
    else:
        print(f"Invalid download_type: {download_type}. Please check your config.json file.")