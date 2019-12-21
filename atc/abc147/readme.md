## Quick Start
# first rename abcXXX.py to abcYYY.py
./reanme.sh 116 119

# then, download the testcases for YYY
./download_test.sh 119

# That's it.


## Manual Test
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_d -d test-d
oj test -d test-d -c "python abc116d.py"
oj test -d test-d -c "python abc116d.py" test-d/sample-3.in

