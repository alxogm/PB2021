CC=gcc 
CFLAGS=-Wall

objects = Ago13/hello
all: $(objects)

$(objects): %: %.c
	$(CC) $(CFLAGS) -o $@ $<
