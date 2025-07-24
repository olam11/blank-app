import streamlit as st
import yt_dlp
import os

def download_mp3(video_id, output_dir="/tmp"):
    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        mp3_file = os.path.splitext(filename)[0] + '.mp3'
        return mp3_file

# Streamlit UI
st.title("Téléchargeur MP3 YouTube avec yt-dlp")
video_id = st.text_input("Entrez l'identifiant de la vidéo YouTube")

if st.button("Télécharger"):
    if video_id:
        try:
            mp3_path = download_mp3(video_id)
            st.success("Téléchargement réussi !")
            st.audio(mp3_path)
        except Exception as e:
            st.error(f"Erreur lors du téléchargement : {e}")
    else:
        st.warning("Veuillez entrer un identifiant YouTube.")
