#!/bin/bash

### Remove all non-code files
rm libA.so
rm libB1.so
rm libB2.so
rm libC.so
rm dlopen

### Build all .o
gcc -fPIC -c a.c
gcc -fPIC -c b1.c
gcc -fPIC -c b2.c
gcc -fPIC -c c.c

### Build .so [ gcc -shared -o lib<name> <a.o> <b.o> ... ]
gcc -shared -o libB1.so b1.o #defines 'b'
gcc -shared -o libB2.so b2.o #defines 'b'
gcc -shared -o libC.so c.o   #defines 'c'
gcc -shared -o libA.so a.o -L . -lB1 #BUILD without dependency [ can crash, error shows up as "unresolved symbol" which is an abnormal exit ]
#gcc -shared -o libA.so a.o -Wl,-rpath,. -L . -lB1    #if libA.so depends on libB.so,
                                                        #we need to specify "-Wl,-rpath,. -L . -l<lib_name>" 
                                                        #that checks for 'libB.so' in the SAME dir

### Build main
gcc -Wall dlopen.c -o dlopen -ldl -L . -lA -lB1 -lB2
#gcc -Wall -g --static dlopen.c -ldl -o dlopen -s


### Run bin
if [ "$1" == "r" ]; then
    ./dlopen
fi

### Docker
#docker build -t dlopen_c .
#docker container run --rm dlopen_c

### Remove all non-code files
rm a.o
rm b1.o
rm b2.o
rm c.o
