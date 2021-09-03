CC=gcc 
CFLAGS=-Wall

objects = Ago13/hello Ago25/operaciones_int.c Ago25/operaciones_float.c Ago27/temperaturas.c Ago27/area_circulo.c
all: $(objects)

$(objects): %: %.c
	$(CC) $(CFLAGS) -o $@ $<
