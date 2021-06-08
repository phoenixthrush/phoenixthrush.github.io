cd .\
cd dist
del main.bat
cd ..
pyinstaller -i nezuko.ico --onefile --uac-admin --name main main.py