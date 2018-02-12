# Course-work
Исследование возможности синхронного распознавания речи и артикуляции говорящего. Разработка прототипа.
  
В pocketsphinx есть возможность [преобразования речи в поток фонем](https://cmusphinx.github.io/wiki/phonemerecognition/). Их можно сравнивать с результатом, полученным от распознавания артикуляции, чтобы делать вывод о вероятности произносении той или иной фонемы. Не уверен насколько будет лучшим способ распознать по видео набор фонем и в модели распознавания речи отсекать фонемы, которые не были распознаны по видео.  
  
Installation  
// Make sure we have up-to-date versions of pip, setuptools and wheel:  
$ pip install --upgrade pip setuptools wheel  
$ pip install --upgrade pocketsphinx  

Install pocketsphinx  
$ git clone --recursive https://github.com/bambocher/pocketsphinx-python  
$ cd pocketsphinx-python  
$ python setup.py install

В директории pocketsphinx/model находится словарь.  
Для работы требуется лингвистическая модель (ru.lm.bin) и акустическая модель (zero_ru.cd_cont_4000), которые можно скачать по ссылке:  
https://cloud.mail.ru/public/CBFr/hCJ1wBTsz  
Лингвистическая модель, акустическая модель и словарь должны находится в pocketsphinx/model