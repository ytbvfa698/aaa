for x
do 
         sed -f sedscr $x > tmp.$x
         diff $x tmp.$x
done
