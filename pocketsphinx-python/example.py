from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from pocketsphinx import get_model_path, get_data_path
import pyaudio

MODELDIR = get_model_path()
DATADIR = get_data_path()

config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'zero_ru.cd_cont_4000'))
config.set_string('-lm', path.join(MODELDIR, 'ru.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'ru.dic'))
# config.set_float('-samprate', 8000.0)

# config = {
#     'samprate': 8000.0,
# 	'hmm': os.path.join(model_path, 'zero_ru.cd_cont_4000'),
#     'lm': os.path.join(model_path, 'ru.lm.bin'),
#     'dict': os.path.join(model_path, 'ru.dic')
# }

decoder = Decoder(config)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=8000, input=True, frames_per_buffer=1024)
stream.start_stream()

in_speech_bf = False
decoder.start_utt()
while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()
                print 'Result:', decoder.hyp().hypstr
                decoder.start_utt()
    else:
        break
decoder.end_utt()