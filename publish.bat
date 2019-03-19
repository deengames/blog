@echo off
rd /s /q ..\output
pelican
move output ..
echo DONE! Built to ..\output