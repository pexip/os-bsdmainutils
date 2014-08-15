#!/bin/sh
set -e
ru_cal_path=${1}usr.bin/calendar/calendars/ru_RU.KOI8-R
uk_cal_path=${1}usr.bin/calendar/calendars/uk_UA.KOI8-U
#ru_cal_path=/usr/share/calendar/ru_RU
#uk_cal_path=/usr/share/calendar/uk_UA

cvt_cal() {
  local subst uk
  if [ Гру = "$1" ]; then
    uk=true  subst='s/Нд-1/Sun-1/;'
  else
    uk=false subst=
  fi
  while [ 0 -lt $# ];  do
    $uk && subst=$subst$(printf 's|^%s |%02d/|;' $1 $#)
    subst=$subst$(printf 's|^ *([0-9]{1,2}) %s([*]?)\t|%02d/\\1\\2\t|;' $1 $#)
    shift
  done
  #printf %s\\n "$subst"
  for f in "$cal_path"/calendar.*
  do sed -ri "$subst" "$f"
  done
}

cal_path=$ru_cal_path
cvt_cal дек ноя окт сен авг июл июн май апр мар фев янв
cal_path=$uk_cal_path
cvt_cal  Гру Лис Жов Вер Сер Лип Чер Тра Кві Бер Лют Січ

# vim:ai sw=2 sts=2 et:
