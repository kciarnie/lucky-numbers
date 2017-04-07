if ! test -d $1; then
   echo "The $1 directory doesn't exist'"
   virtualenv -p python3 $1
fi
source $1/bin/activate
pip3 install -e .