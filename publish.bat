@echo off
rd /s /q ..\output
pelican
move output ..
echo DONE! Built to ..\output
cd ..\output
python -m http.server