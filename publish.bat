@echo off
rd /s /q ..\output
REM make sure opengraph plugin is initialized. changing branches derps it.
git submodule update --recursive
pelican
move output ..
echo DONE! Built to ..\output
cd ..\output
python -m http.server