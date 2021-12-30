#!/usr/bin/env zsh

cd /Users/zacheliason/Documents/website/zach_website/

python add_md.py

bash git.sh
echo "git committed"
npm run build
sleep 20
echo "dist built"

cp -R dist/* /Users/zacheliason/Documents/website/zacheliason.github.io

cd /Users/zacheliason/Documents/website/zacheliason.github.io
sleep .2
bash git.sh
sleep 2
echo "git committed"
echo "put down that cocktail!"
