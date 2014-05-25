sister_3
========

Keterangan file
---------------

- `data` : folder berisi file xml sampel
- `1_hash_client.py`	: client hash web service 
- `1_hash_service.bat`	: launcher server hash web service
- `1_hash_service.py`	: server hash web service 
- `2_a_stock.py`		: client web service saham
- `2_b_exchange.py`		: client web service kurs
- `2_c_weather.py`		: client web service cuaca
- `README.md`			: file yang sedang kamu baca sekarang


Instalasi package python
------------------------

Untuk menjalankan client service, package SUDS harus di-install terlebih dahulu

`pip install suds`

kemudian install package web service server

`pip install ladon`


Instruksi installasi pip
------------------------

https://pip.pypa.io/en/latest/installing.html


Intruksi menjalankan hash service server
----------------------------------------

`python D:\Python27\Scripts\ladon-ctl testserve 1_hash_service.py -p 8080`