PROG = banner
SRC = banner.c
MAN = banner.6
LIBS += -lbsd
FLAGS = -include bsd/string.h

topdir=../..
include $(topdir)/config.mk

install-2:
	mv $(mandir)/banner.6 $(mandir)/printerbanner.1
	mv $(bindir)/banner $(bindir)/printerbanner
