python3 create-preso.py $1.md -t nalug -b $1/nalug.png

if [ $? -eq 0 ]; then
    tar -zcvf $1.tar.gz dist plugin common $1 $1.html
fi
