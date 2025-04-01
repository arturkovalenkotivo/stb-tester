from pydub import AudioSegment as AS


class AudioSegment:

    def __new__(cls, data=None, **kwargs) -> AS:
        sample_width=kwargs["sample_width"]
        frame_rate = kwargs["frame_rate"]
        channels = kwargs["channels"]
        _as = AS(data, sample_width=sample_width, frame_rate=frame_rate, channels=channels)
        metadata_names = ("begin", "end")
        for mdata in metadata_names:
            val = kwargs.get(mdata)
            setattr(_as, mdata, val)
        return _as
