PROG = bsd-from
MAN = from.1

topdir=../..
include $(topdir)/config.mk

bsd-from.o: from.c
	$(CC) -include $(topdir)/freebsd.h $(FLAGS) $(CFLAGS) -c -o $@ $<

install-2:
	mv $(mandir)/from.1 $(mandir)/bsd-from.1

topdir=../..
include $(topdir)/config.mk
