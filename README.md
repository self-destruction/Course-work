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

В директории pocketsphinx/model представлен словарь и акустическая модель русского языка  
Для работы требуется лингвистическая модель, которую можно скачать по ссылке:  
https://cloud.mail.ru/public/AkNg/v41bm4mTG
