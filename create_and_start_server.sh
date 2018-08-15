#rm -rf blog
pelican -s pelicanconf.py
cd output
python -m http.server
