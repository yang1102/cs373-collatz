FILES :=                              \
    Collatz.html                      \
    Collatz.log                       \
    Collatz.py                        \
    RunCollatz.in                     \
    RunCollatz.out                    \
    RunCollatz.py                     \
    TestCollatz.out                   \
    TestCollatz.py

#    collatz-tests/EID-RunCollatz.in   \
#    collatz-tests/EID-RunCollatz.out  \
#    collatz-tests/EID-TestCollatz.out \
#    collatz-tests/EID-TestCollatz.py  \

.pylintrc:
	pylint --disable=bad-whitespace,missing-docstring,pointless-string-statement --reports=n --generate-rcfile > $@

collatz-tests:
	git clone https://github.com/cs373-summer-2016/collatz-tests.git

Collatz.html: Collatz.py
	pydoc3 -w Collatz

Collatz.log:
	git log > Collatz.log

RunCollatz.tmp: RunCollatz.in RunCollatz.out RunCollatz.py
	-pylint Collatz.py
	-pylint RunCollatz.py
	./RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.tmp RunCollatz.out
	python3 -m cProfile RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	cat RunCollatz.tmp

TestCollatz.tmp: TestCollatz.py
	-pylint Collatz.py
	-pylint TestCollatz.py
	coverage-3.5 run    --branch TestCollatz.py >  TestCollatz.tmp 2>&1
	coverage-3.5 report -m                      >> TestCollatz.tmp
	cat TestCollatz.tmp

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  RunCollatz.tmp
	rm -f  TestCollatz.tmp
	rm -rf __pycache__

config:
	git config -l

format:
	autopep8 -i Collatz.py
	autopep8 -i RunCollatz.py
	autopep8 -i TestCollatz.py

scrub:
	make clean
	rm -f  Collatz.html
	rm -f  Collatz.log
	rm -rf collatz-tests

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: .pylintrc Collatz.html Collatz.log RunCollatz.tmp TestCollatz.tmp collatz-tests check
