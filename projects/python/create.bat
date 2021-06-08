cd .\
cd dist
del main.exe
cd ..
pyinstaller -i nezuko.ico --noconsole --onefile --name main main.py