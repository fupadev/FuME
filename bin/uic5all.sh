#!/usr/bin/env bash
# Converts .ui in .py
pyuic5 mainwindow.ui -o ../fume/ui/mainwindow.py;
pyuic5 settings.ui -o ../fume/ui/settings.py;
pyuic5 log.ui -o ../fume/ui/log.py;
pyuic5 filter.ui -o ../fume/ui/filter.py;
pyuic5 about.ui -o ../fume/ui/about.py;
pyuic5 updatewindow.ui -o ../fume/ui/updatewindow.py;
pyuic5 aboutqt.ui -o ../fume/ui/aboutqt.py;
pyuic5 edit.ui -o ../fume/ui/edit.py;
pyuic5 creategalery.ui -o ../fume/ui/creategalery.py;
