import cx_Oracle


con = cx_Oracle.connect('system/a123456@localhost:1521/XE')
cur = con.cursor()
cur.execute('select * from HR.EMPLOYEES where EMPLOYEE_ID = \'100\'')
for result in cur:
    test = str(result);
    print ('test = ' + str(result[0])) #  prints first column from result set 
    print ('test = ' + str(result[1])) #  prints second column from result set 
cur.close()
con.close()