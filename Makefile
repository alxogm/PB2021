CC=gcc 
CFLAGS=-Wall

all: Ago13/hello
hello: Ago13/hello.o
hello.o: Ago13/hello.c 

clean:
    rm -f Ago13/hello Ago13/hello.o
