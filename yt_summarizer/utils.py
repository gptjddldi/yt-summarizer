import yt_summarizer.constants as constants

from pytube import YouTube
from pywhispercpp.model import Model

import os
import subprocess

def extract_audio(url):
    video = YouTube(url)

    audio_stream = video.streams.filter(only_audio=True).first()
    f = audio_stream.download(filename="test.mp4")
    nf = wav_converter(f)

    os.remove(f)

    return nf

def wav_converter(file_path):
    file_name, _ = os.path.splitext(file_path)
    new_file_path = f"{file_name}.wav"

    command = "ffmpeg -i {} -ab 160k -ac 2 -ar 16000 -vn {}".format(file_path, new_file_path)
        
    subprocess.call(command, shell=True)

    return new_file_path

def transcribe_audio(file_name, model = 'small.en'):
    model = Model(model, n_threads=6)
    segments = []

    def segment_callback(segment):
        segments.append(segment[0].text)

    try:
        model.transcribe(file_name, speed_up=True, new_segment_callback=segment_callback)
    except UnicodeDecodeError as ue:
        print("error")
    finally:
        os.remove(file_name)
    return segments

def write_txt(file_path, segments):
    with open(file_path, "w") as file:
        for segment in segments:
            file.write(segment + "\n")
    return file_path

def read_file_content(file_path: str = constants.TRANSCRIBE_OUTPUT_FILE_NAME):
    with open(file_path, 'r', encoding='utf-8') as file:
        ret = file.read()

    os.remove(file_path)

    return ret