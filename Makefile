# Makefile for the new bsdmainutils
# $Id$

# what programs to build
BIN=$(wildcard usr.bin/*)

# used for building in the subdirectories
rmake=@set -e; for i in $(BIN); do $(MAKE) --no-print-directory -C $$i $(1); done

all: $(BIN)
	$(call rmake)

clean:
	$(call rmake,clean)

install: all
	mkdir -p $(DESTDIR)/usr/bin
	mkdir -p $(DESTDIR)/usr/share/man/man1

	$(call rmake,install)

dist: clean
	tar -czf ../`basename $(PWD)`.tar.gz -C .. --exclude .svn `basename $(PWD)`

.PHONY: all install clean
