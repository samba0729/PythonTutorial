import cx_Oracle


con = cx_Oracle.connect('system/a123456@localhost:1521/XE')
print (con.version)
cur = con.cursor()
cur.execute('SELECT 2 FROM DUAL')
for result in cur:
    test = str(result);
    print ('test = ' + str(result[0]))
cur.close()
con.close()