#!/usr/bin/bash

KEY="mYsO2m1KfJYFBEd3BYVvho4bmI9PKR2x"
ADDR="https://cobalt.qas.im/api/1.0/courses"

TEMP_COURSES="temp_courses.json"
EMPTY_COURSES="empty.json"

PROGRESS=0
AND="%20AND%20"


if [ ! 1 -eq $# ]
then
    echo "USAGE $0 <output_file>"
    exit
fi

FINAL_COURSES="$1.json"

if [ ! -f $EMPTY_COURSES ];
then
    echo "[]" > $EMPTY_COURSES
fi

for file in $FINAL_COURSES $TEMP_COURSES
do
    rm -f $file
    touch $file
done

while ! `cmp -s -n 2 $TEMP_COURSES $EMPTY_COURSES`
do
    cat $TEMP_COURSES >> $FINAL_COURSES
    curl "$ADDR/filter?key=$KEY&q=code:\"CSC\"%20AND%20campus:\"UTSG\"&limin=100&skip=$PROGRESS" > $TEMP_COURSES
    PROGRESS=$(($PROGRESS+100))
    echo
done
