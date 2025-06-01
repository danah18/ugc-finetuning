import yt_dlp

def download_vimeo_video(url, output_path):
    """
    Download a Vimeo video using yt-dlp.

    Args:
        url (str): The URL of the Vimeo video.
        output_path (str): The output template for the downloaded file.
    """
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'bestvideo+bestaudio/best',  # Downloads best video + audio and merges
        'merge_output_format': 'mp4',
        'quiet': False,  # Set to True to suppress output
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading video from: {url}")
        ydl.download([url])

# Example usage
# if __name__ == "__main__":
#     vimeo_url = "https://r2.foreplay.co/1027672322193282/e100664c2c7fa506ecaacec99049c7ab.mp4" #"https://player.vimeo.com/video/1072475389"
#     download_vimeo_video(vimeo_url)
