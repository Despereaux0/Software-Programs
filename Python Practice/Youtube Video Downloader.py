import yt_dlp

# Get user input
url = input("Enter the YouTube video link: ")
choice = input("Do you want to download (A)udio or (V)ideo? ").strip().lower()

if choice == 'a':
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',  # Download best audio (M4A)
        'outtmpl': 'downloads/%(title)s.%(ext)s'  # Save file in 'downloads' folder
    }
elif choice == 'v':
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Download best MP4 quality
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }
else:
    print("Invalid choice. Please enter 'A' for audio or 'V' for video.")
    exit()

# Download based on user selection
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed!")
