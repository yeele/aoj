if [ -z $1 ]; then
  echo "specify number saying from"; exit 1;
fi
if [ -z $2 ]; then
  echo "specify number saying to"; exit 1;
fi
__FROM=$1
__TO=$2

for i in `ls`; do
  #mv $i `echo $i | sed  -E "s/118/116/g"`; 
  mv $i `echo $i | sed  -E "s/${__FROM}/${__TO}/g"`; 
done

