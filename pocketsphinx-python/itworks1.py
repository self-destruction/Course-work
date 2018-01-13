import os
from pocketsphinx import AudioFile, Pocketsphinx, get_model_path, get_data_path

model_path = get_model_path()
data_path = get_data_path()

config = {
    'samprate': 8000.0,
	'hmm': os.path.join(model_path, 'zero_ru.cd_cont_4000'),
    'lm': os.path.join(model_path, 'ru.lm.bin'),
    'dict': os.path.join(model_path, 'ru.dic')
}

ps = Pocketsphinx(**config)
ps.decode(
    audio_file=os.path.join(data_path, 'decoder-test.wav'),
    buffer_size=2048,
    no_search=False,
    full_utt=False
)

print(ps.hypothesis())
