#! /usr/bin/python3
# Filename: calendarJudaic.py
#
# License: no warranty close + no license (public domain)
#
# Author: Ron Varburg <linux-il@hotmail.com>
#
# Creates a calendar.judaic file, which is suitable for inclusion
# in Debian's bsdmainutils package.  Up to the introductory of
# this script the calendar.judaic file was not updated regularly.
# Probably because updating it is time consuming.  This python
# script let anyone create that file, for any year.  Its output is
# written to stdout.  It requires the libhdate-python package.
# A small part of the holidays might require manual editing
# because the state of Israel modifies the actual date by a few
# days due to various considerations.

# References:
# http://www.mail-archive.com/linux-il@cs.huji.ac.il/msg58169.html
# http://www.mail-archive.com/linux-il@cs.huji.ac.il/msg58321.html
# http://www.mail-archive.com/linux-il@cs.huji.ac.il/msg58451.html


from    string    import  Template
import  hdate,  optparse,  sys,  time


def main():

  description = '''Description:
Creates a calendar.judaic file, which is suitable for inclusion
in Debian's bsdmainutils package.  Up to the introductory of
this script the calendar.judaic file was not updated regulary.
Probably because updating it is time consuming.  This python
script let anyone create that file, for any year.  Its output is
written to stdout.  It requires the libhdate-python package.
A small part of the holydays might require manual editing
because the state of Israel modifies the actual date by a few
days due to various considerations.
'''
  usage = "Usage:    %prog [year]\n"\
          "          %prog [--help|--version]\n"\
          "\n"\
          "Example:  %prog"
  version = "29-May-2010"
  parser = optparse.OptionParser(description=description,
                                 usage=usage, version=version)
  (options, args) = parser.parse_args()
  if len(args)> 1:
    parser.error("\n  " + str(len(args)) + " arguments were "
        "given.  At most 1, an integer represnting a year, "
        "is expected."
                )
  elif len(args) == 1:
      # An integer represnting a year is expected.
      try:
          year = int(args[0])
      except ValueError:
          parser.error("\n  Could not convert the argument " + args[0]
            + ", which should represent a year, to an integer."
                      )
  else:  # len(args) == 0, no args were given.  Use the current year.
    year = time.localtime().tm_year

  h = hdate.Hdate()

  template_for_header = '''/*
 * Judaic Calendar. Created by calendar.judaic.py.
 * Collaboratively authored by linux-il@cs.huji.ac.il.
 *
 * $$Debian GNU\Linux$$
 *
 */

#ifndef _calendar_judaic_
#define _calendar_judaic_

LANG=UTF-8

/*
 * Jewish calendar for the CE year ${PLACE_HOLDER_FOR_THR_CE_YEAR}
 * ${PLACE_HOLDER_FOR_THE_JEWISH_START_OF_THE_CE_YEAR} - ${PLACE_HOLDER_FOR_THE_JEWISH_END_OF_THE_CE_YEAR}
 */

'''

  footer = '''

#endif /* !_calendar_judaic_ */'''

  substitutions_for_header = {
      'PLACE_HOLDER_FOR_VERSION' : version,
      'PLACE_HOLDER_FOR_THR_CE_YEAR' : str(year)
                               }
  h.set_gdate(1, 1, year)
  substitutions_for_header[
      'PLACE_HOLDER_FOR_THE_JEWISH_START_OF_THE_CE_YEAR'] = \
          h.get_format_date(h.get_julian()) + ' ' + \
                              h.get_hebrew_year_string()
  h.set_gdate(31, 12, year)
  substitutions_for_header[
      'PLACE_HOLDER_FOR_THE_JEWISH_END_OF_THE_CE_YEAR'] = \
          h.get_format_date(h.get_julian()) + ' ' + \
                              h.get_hebrew_year_string()
  header = Template(template_for_header).substitute(
                                  substitutions_for_header)
  print(header)

  h.set_gdate(1, 1, year)
  julian = h.get_julian()
  for i in range(0, 365):
    h.set_jd(julian)
    julian += 1
    day = h.get_gday()
    month = h.get_gmonth()
    holyday = { 'Israel' : None, 'diaspora' : None }
    parasha = { 'Israel' : None, 'diaspora' : None }
    h.set_israel
    holyday['Israel'] = h.get_holyday_string(0)
    parasha['Israel'] = h.get_parasha_string(0)
    h.set_diaspora
    holyday['diaspora'] = h.get_holyday_string(0)
    parasha['diaspora'] = h.get_parasha_string(0)
    if holyday['Israel']:
      if holyday['Israel'] == holyday['diaspora']:
        print("%02d/%02d*	%s" % (month, day, holyday['Israel']))
      else:
        print("%02d/%02d*	%s (Israel only)" % \
                                (month, day, holyday['Israel']))
    elif holyday['diaspora']:
      print("%02d/%02d*	%s (diaspora only)" % \
                                (month, day, holyday['diaspora']))
    if parasha['Israel']  and  parasha['Israel'] != 'none':
      if parasha['Israel'] == parasha['diaspora']:
        print("%02d/%02d*	Parshat %s" % \
                                (month, day, parasha['Israel']))
      else:
        print("%02d/%02d*	%s (Israel only)" % \
                                (month, day, parasha['Israel']))
    elif parasha['diaspora']  and  parasha['diaspora'] != 'none':
    # See http://bugs.debian.org/583092 why 'none' is required here.
      print("%02d/%02d*	Parshat %s (diaspora only)" % \
                                (month, day, parasha['diaspora']))

  print(footer)

  sys.exit()


if __name__ == "__main__":
  main()
else:
  # The following is useful from within an interactive Python
  # interpreter, where calendarJudaic.py is in the same `pwd`:
  #  >>> import calendarJudaic
  pass
