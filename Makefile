CC=gcc 
CFLAGS=-Wall -pedantic

Ago25 = Ago13/hello Ago25/operaciones_int Ago25/operaciones_float
all: $(Ago25)
$(Ago25): %: %.c
	$(CC) $(CFLAGS) -o $@ $<

Ago27 = Ago27/area_circulo Ago27/temperaturas
all: $(Ago27)
$(Ago27): %: %.c
	$(CC) $(CFLAGS) -o $@ $<

Sep1 = Sep1/cambio_coordenadas
all: $(Sep1)
$(Sep1): %: %.c
	$(CC) $(CFLAGS) -o $@ $<
