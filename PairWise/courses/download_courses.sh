#!/usr/bin/bash

KEY="mYsO2m1KfJYFBEd3BYVvho4bmI9PKR2x"
ADDR="https://cobalt.qas.im/api/1.0/courses"

FINAL_COURSES="csc_courses.json"
TEMP_COURSES="temp_courses.json"
EMPTY_COURSES="empty.json"

PROGRESS=0
AND="%20AND%20"

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
    echo "Different"
    cat $TEMP_COURSES
    echo
    cat $TEMP_COURSES >> $FINAL_COURSES
    curl "$ADDR/filter?key=$KEY&q=code:\"CSC\"%20AND%20campus:\"UTSG\"&limin=100&skip=$PROGRESS" > $TEMP_COURSES
    PROGRESS=$(($PROGRESS+100))
    echo $PROGRESS
done
# curl "$ADDR/filter?key=$KEY&"

