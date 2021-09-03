CC=gcc 
CFLAGS=-Wall -pedantic

##Ago25 = Ago13/hello Ago25/operaciones_int Ago25/operaciones_float
##all: $(Ago25)
##$(Ago25): %: %.c
##	$(CC) $(CFLAGS) -o $@ $<

Ago27 = Ago27/area_circulo Ago27/temperaturas
all: $(Ago27)
$(Ago25): %: %.c
        $(CC) $(CFLAGS) -o $@ $<
