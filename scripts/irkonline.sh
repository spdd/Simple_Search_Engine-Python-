/usr/local/bin/mysqldump -uroot -pmysql irkdb > /usr/local/db/dump.sql &&
/usr/bin/gzip /usr/local/db/dump.sql &&
/usr/bin/scp /usr/local/db/dump.sql.gz root@irkonline.info:/usr/local/db/ &&
/usr/bin/ssh root@irkonline.info '~/mysqlrestore.sh' &&
/bin/rm /usr/local/db/*
