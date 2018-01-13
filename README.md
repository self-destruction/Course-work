# Course-work
Исследование возможности синхронного распознавания речи и артикуляции говорящего. Разработка прототипа.

Installation  
// Make sure we have up-to-date versions of pip, setuptools and wheel:  
$ pip install --upgrade pip setuptools wheel  
$ pip install --upgrade pocketsphinx  

Install pocketsphinx  
$ git clone --recursive https://github.com/bambocher/pocketsphinx-python  
$ cd pocketsphinx-python  
$ python setup.py install

В директории pocketsphinx/model находится акустическая модель русского языка.  
Для работы требуется лингвистическая модель (ru.lm.bin) и словарь (zero_ru.cd_cont_4000), которые можно скачать по ссылке:  
https://cloud.mail.ru/public/CBFr/hCJ1wBTsz  
Лингвистическая модель, акустическая модель и словарь должны находится в pocketsphinx/model
