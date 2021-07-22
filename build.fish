#!/usr/bin/env fish

test -d build && rm -Rf build
mkdir -p build/
zip -r build/audio-switcher.alfredworkflow.zip *.py *.plist *.png images icons
mv build/audio-switcher.alfredworkflow.zip build/audio-switcher.alfredworkflow
#cp -R *.py *.plist *.png images icons build/audio-switcher.alfredworkflow/
