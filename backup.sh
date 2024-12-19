file=/tmp/db-$(/usr/bin/date +\%Y-%m-%d-%H:%M:%S).sql
container=seezntv-db-1
/usr/bin/docker container exec $container pg_dump -U postgres django > $file
mc cp $file b2/jst-seezntv
rm $file
