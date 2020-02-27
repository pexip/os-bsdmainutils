PROG = bsd-write
MAN = write.1
LIBS += -lbsd
FLAGS = -include fcntl.h -include time.h -include bsd/string.h 

topdir=../..
include $(topdir)/config.mk

bsd-write.o: write.c
	$(CC) -include $(topdir)/freebsd.h $(FLAGS) $(CFLAGS) -c -o $@ $<

install-2:
	chown root:tty $(bindir)/$(PROG)
	chmod 2755 $(bindir)/$(PROG)
	mv $(mandir)/write.1 $(mandir)/bsd-write.1
