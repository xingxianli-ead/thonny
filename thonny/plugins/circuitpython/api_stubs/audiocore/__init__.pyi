"""Support for audio samples"""

class RawSample:
    """A raw audio sample buffer in memory"""

    def __init__(self, buffer: array.array, *, channel_count: int = 1, sample_rate: int = 8000):
        """Create a RawSample based on the given buffer of signed values. If channel_count is more than
        1 then each channel's samples should alternate. In other words, for a two channel buffer, the
        first sample will be for channel 1, the second sample will be for channel two, the third for
        channel 1 and so on.

        :param array.array buffer: An `array.array` with samples
        :param int channel_count: The number of channels in the buffer
        :param int sample_rate: The desired playback sample rate

        Simple 8ksps 440 Hz sin wave::

          import audiocore
          import audioio
          import board
          import array
          import time
          import math

          # Generate one period of sine wav.
          length = 8000 // 440
          sine_wave = array.array("h", [0] * length)
          for i in range(length):
              sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15))

          dac = audioio.AudioOut(board.SPEAKER)
          sine_wave = audiocore.RawSample(sine_wave)
          dac.play(sine_wave, loop=True)
          time.sleep(1)
          dac.stop()"""
        ...

    def deinit(self, ) -> Any:
        """Deinitialises the AudioOut and releases any hardware resources for reuse."""
        ...

    def __enter__(self, ) -> Any:
        """No-op used by Context Managers."""
        ...

    def __exit__(self, ) -> Any:
        """Automatically deinitializes the hardware when exiting a context. See
        :ref:`lifetime-and-contextmanagers` for more info."""
        ...

    sample_rate: Any = ...
    """32 bit value that dictates how quickly samples are played in Hertz (cycles per second).
    When the sample is looped, this can change the pitch output without changing the underlying
    sample. This will not change the sample rate of any active playback. Call ``play`` again to
    change it."""

class WaveFile:
    """Load a wave file for audio playback

    A .wav file prepped for audio playback. Only mono and stereo files are supported. Samples must
    be 8 bit unsigned or 16 bit signed. If a buffer is provided, it will be used instead of allocating
    an internal buffer."""

    def __init__(self, file: typing.BinaryIO, buffer: bytearray):
        """Load a .wav file for playback with `audioio.AudioOut` or `audiobusio.I2SOut`.

        :param typing.BinaryIO file: Already opened wave file
        :param bytearray buffer: Optional pre-allocated buffer, that will be split in half and used for double-buffering of the data. If not provided, two 512 byte buffers are allocated internally.


        Playing a wave file from flash::

          import board
          import audiocore
          import audioio
          import digitalio

          # Required for CircuitPlayground Express
          speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
          speaker_enable.switch_to_output(value=True)

          data = open("cplay-5.1-16bit-16khz.wav", "rb")
          wav = audiocore.WaveFile(data)
          a = audioio.AudioOut(board.A0)

          print("playing")
          a.play(wav)
          while a.playing:
            pass
          print("stopped")"""
        ...

    def deinit(self, ) -> Any:
        """Deinitialises the WaveFile and releases all memory resources for reuse."""
        ...
    def __enter__(self, ) -> Any:
        """No-op used by Context Managers."""
        ...

    def __exit__(self, ) -> Any:
        """Automatically deinitializes the hardware when exiting a context. See
        :ref:`lifetime-and-contextmanagers` for more info."""
        ...

    sample_rate: Any = ...
    """32 bit value that dictates how quickly samples are loaded into the DAC
    in Hertz (cycles per second). When the sample is looped, this can change
    the pitch output without changing the underlying sample."""

    bits_per_sample: Any = ...
    """Bits per sample. (read only)"""

    channel_count: Any = ...
    """Number of audio channels. (read only)"""

