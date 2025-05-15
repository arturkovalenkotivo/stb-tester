import argparse
from pathlib import Path

from _stbt.core import new_device_under_test_from_config


parser = argparse.ArgumentParser()
cfg = parser.parse_args([])


cfg.source_pipeline = "videotestsrc ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert"
cfg.audio_pipeline = "audiotestsrc ! audio/x-raw, rate=44100, channels=2, format=S16LE"
cfg.sink_pipeline = ""
cfg.control = None
cfg.save_video = False
output_wav = Path.home() / "dut.wav"
dut = new_device_under_test_from_config(cfg)
with dut:
    save = []
    prev_end = 0
    prev_frame = 0
    for frame in dut.frames(5):
        if hasattr(frame, "audio") and frame.audio:
            audio = frame.audio
            save.append(audio)
            inter_chunk = audio.begin - prev_end
            prev_end = audio.end


            print(f"VF:{frame.time - prev_frame:.3f}, Audio: {frame.time - audio.begin:.3f} - {frame.time - audio.end:.3f}, IC: {inter_chunk:.3f}")
            prev_frame = frame.time
            # print(f"DUration: {audio.duration_seconds}, beg={audio.end - audio.begin}, end={audio.end}, frame={frame.time}, IC={inter_chunk:.3f}")
        else:
            print(f"VF:{frame.time - prev_frame:.3f}, Audio: None")
            prev_frame = frame.time
    sum(save).export(str(output_wav), format="wav")
