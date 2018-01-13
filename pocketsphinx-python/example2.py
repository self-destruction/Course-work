from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from pocketsphinx import get_model_path, get_data_path

MODELDIR = get_model_path()
DATADIR = get_data_path()

# Create a decoder with certain model
config = Decoder.default_config()
# config.set_string('-hmm', path.join(MODELDIR, 'en-us'))
# config.set_string('-lm', path.join(MODELDIR, 'en-us.lm.bin'))
# config.set_string('-dict', path.join(MODELDIR, 'cmudict-en-us.dict'))
config.set_string('-hmm', path.join(MODELDIR, 'zero_ru.cd_cont_4000'))
config.set_string('-lm', path.join(MODELDIR, 'ru.lm'))
config.set_string('-dict', path.join(MODELDIR, 'ru.dic'))
decoder = Decoder(config)

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()
stream = open(path.join(DATADIR, 'decoder-test.wav'), 'rb')
while True:
  buf = stream.read(1024)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()
print ('Best hypothesis segments: ', [seg.word.decode('utf-8') for seg in decoder.seg()])