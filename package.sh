python3 create-preso.py $1.md -t nalug -b $1/nalug.png
tar -zcvf $1.tar.gz dist plugin common $1 $1.html
