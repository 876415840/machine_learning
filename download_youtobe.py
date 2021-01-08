#! _*_encoding=utf-8_*_


from pytube import YouTube
import ssl


def download():
    ssl._create_default_https_context = ssl._create_unverified_context
    # 需要翻墙保证网络通畅
    yt = YouTube("https://www.youtube.com/watch?v=U4kpHYIuV6c")
    print(yt.title)

    stream = yt.streams.first()
    path = stream.download(output_path='/Users/finup/Desktop')
    print(path)

if __name__ == '__main__':
    download()
