if [ -z $1 ]; then
  echo "specify number saying this ABC, like 119"; exit 1;
fi

ROUND=$1
curdir=$(cd `dirname $0`; pwd)

for LEVEL in "a" "b" "c" "d";
do
  DIR_NAME=test-${LEVEL}
  if [ -d ${curdir}/${DIR_NAME} ]; then
    rm -rf ${curdir}/${DIR_NAME}
  fi
  oj dl https://atcoder.jp/contests/abc${ROUND}/tasks/abc${ROUND}_${LEVEL} -d ${DIR_NAME}
done


