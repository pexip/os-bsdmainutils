PROG = printerbanner
MAN = banner.6

topdir=../..
include $(topdir)/config.mk

printerbanner.o: banner.c
	$(CC) -include $(topdir)/freebsd.h $(FLAGS) $(CFLAGS) -c -o $@ $<

install-2:
	mv $(mandir)/banner.6 $(mandir)/printerbanner.1
