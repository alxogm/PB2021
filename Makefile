CC=gcc 
CFLAGS=-Wall -pedantic

Ago25 = Ago13/hello Ago25/operaciones_int Ago25/operaciones_float
all: $(Ago25)
$(Ago25): %: %.c
	$(CC) $(CFLAGS) -o $@ $<
