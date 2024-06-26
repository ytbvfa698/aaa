#!/bin/bash

for x
do
	echo "editing $x: \c"
	if test "$x" = sedscr; then
	   echo  "not editing sedscript!"
	elif test -s $x; then
	   sed -f sedscr $x > /tmp/$x$$
	   if test -s /tmp/$x$$
	   then
	      if cmp -s $x /tmp/$x$$
	      then
	         echo "file not changed: /c"
	      else
	         mv $x $x.bak 
	         cp /tmp/$x$$ $x
	      fi
	      echo "done"
	   else
              echo "Sed produced an empty file\c"
	      echo " - check your sedscript."
	   fi
	   rm -f /tmp/$x$$
        else
           echo "original file is empty."
	fi
done
echo "all done"
