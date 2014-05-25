@echo off
set py_path=D:\Python27
"%py_path%\python.exe" "%py_path%\Scripts\ladon-ctl" testserve 1_hash_service.py -p 8080
pause