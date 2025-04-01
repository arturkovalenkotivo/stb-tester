from _stbt.core import Display, NoSinkPipeline, SinkPipeline
from pathlib import Path
import cv2
display = [None]

def raise_in_user_thread(exception):
    display[0].tell_user_thread(exception)


source_pipeline = "videotestsrc ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert"
audio_pipeline = "audiotestsrc ! audio/x-raw, rate=44100, channels=1, format=S16LE"
sink_pipeline = SinkPipeline("", raise_in_user_thread, save_video="/tmp/test")
sink_pipeline = NoSinkPipeline()
display = Display(source_pipeline, sink_pipeline, audio_pipeline)

audio_chunks = []
for _i in range(100):
    frame = display.get_frame()
    audio_chunks.append(frame.audio)
output_wav = Path.home() / "output2.wav"
combined = sum(audio_chunks)
combined.export(str(output_wav), format="wav")

cv2.imshow(frame, "Name")
