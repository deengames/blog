cd ..
rd /s /q output
cd blog
move output ..
git checkout gh-pages
cd ..
robocopy output blog /s /e
cd blog
