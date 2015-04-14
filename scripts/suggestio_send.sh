/usr/local/bin/python /usr/local/scripts/export_csv.py
/usr/local/bin/curl --digest -u irk:nHk7E04Uc9t http://suggest.io/api/v1/suggests/clear/1111 &&
/usr/local/bin/curl --digest -u irk:nHk7E04Uc9t --upload-file /tmp/suggest.csv http://suggest.io/api/v1/suggests/import/1111/suggest