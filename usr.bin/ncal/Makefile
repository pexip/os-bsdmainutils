PROG   = ncal
SRC    = ncal.c calendar.c easter.c
FLAGS  = -D_GNU_SOURCE -include bsd/string.h

LIBS  += -ltinfo -lbsd

topdir=../..
include $(topdir)/config.mk

install-2:
	(cd $(bindir); ln -sf ncal cal)
	(cd $(mandir); ln -sf ncal.1 cal.1)
