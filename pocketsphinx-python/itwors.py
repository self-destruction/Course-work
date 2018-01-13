# -*- coding: utf-8 -*-

from __future__ import print_function
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

array_segments = ps.segments(detailed=True)

description = ['слово', 'правдободобие', 'нач_фрейма', 'кон_фрейма']
print('слово', end='\t\t')
print('правдободобие', end='\t')
print('нач_фрейма', end='\t')
print('кон_фрейма')

for segment in array_segments:
	for i in range(4):
		print(segment[i], end='\t\t')
	print()

best_ten = ps.best(count=10)

for node in best_ten:
	for i in range(2):
		print(node[i], end='\t\t')
	print()

# print(ps.hypothesis())  # => go forward ten meters
# # print(ps.probability()) # => -32079
# # print(ps.score())       # => -7066
# # print(ps.confidence())  # => 0.04042641466841839

# print(*ps.best(count=10), sep='\n')