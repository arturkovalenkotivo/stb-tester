from pydub import AudioSegment as AS


class AudioSegment(AS):

    def __new__(cls, data=None, *args, **kwargs):
        _as = AS(data=None, *args, **kwargs)
        metadata_names = ("begin", "end")
        for mdata in metadata_names:
            val = kwargs.get(mdata)
            setattr(_as, mdata, val)
        return _as
