CC=gcc 
CFLAGS=-Wall

objects = Ago13/hello Ago25/operaciones_int Ago25/operaciones_float Ago27/temperaturas Ago27/area_circulo
all: $(objects)

$(objects): %: %.c
	$(CC) $(CFLAGS) -o $@ $<
