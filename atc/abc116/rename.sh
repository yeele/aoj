for i in `ls`; do
  mv $i `echo $i | sed  -E "s/118/116/g"`; 
done

