CC      := gcc
CFLAGS  := -W -Wall -Werror
LDFLAGS := -lcunit
BIN     := strrev

SRC := strrev.c
OBJ := $(patsubst %.c,%.o,$(SRC))

%.o: %.c
		$(CC) $(CFLAGS) -o $@ -c $<

all: $(OBJ)
		$(CC) $(CFLAGS) -o $(BIN) $(OBJ) $(LDFLAGS)

clean:
		$(RM) $(BIN) $(OBJ)
