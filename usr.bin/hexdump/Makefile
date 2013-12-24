FLAGS = -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

PROG = hexdump
SRC  = conv.c display.c hexdump.c hexsyntax.c odsyntax.c parse.c

topdir=../..
include $(topdir)/config.mk

install-2:
	(cd $(bindir); ln -sf hexdump hd)
	(cd $(mandir); ln -sf hexdump.1 hd.1)
