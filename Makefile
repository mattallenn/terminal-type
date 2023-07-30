CC = gcc
CFLAGS = -Wall
LDFLAGS = -lncurses	

TARGET = terminaltype 
SOURCE = terminaltype.c
	
all: $(TARGET)
	
$(TARGET): $(SOURCE)
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCE) $(LDFLAGS)
	
clean:
	rm -f $(TARGET)

