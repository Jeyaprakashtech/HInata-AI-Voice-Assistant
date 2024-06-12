import sqlite3
import csv

con=sqlite3.connect("C://Users//user//Documents//projects//hina//database//hinata.db")
cursor = con.cursor()

#query="CREATE TABLE IF NOT EXISTS sys_command(id int primary key,name varchar(100),path varchar(1000))"
#cursor.execute(query)
#query="INSERT INTO contact VALUES (null,'me','9551552444','')"
#cursor.execute(query)
#con.commit()
#cursor.execute("CREATE TABLE IF NOT EXISTS contact(id integer primary key,name VARCHAR(200),moblie_no varchar(255),email varchar(255)NULL )")
#cursor.execute("CREATE TABLE IF NOT EXISTS contact(id integer primary key,name VARCHAR(200),moblie_no varchar(255),email varchar(255)NULL )")
#desired_column=[0,30]
#with open('contacts.csv','r',encoding='utf-8') as csvfile:
    #csvreader = csv.reader(csvfile)
    #for row in csvreader:
        #selected_data=  [row[i] for i in desired_column]
        #cursor.execute("INSERT INTO contacts(id,'name','moblie_no')VALUES(null,?,?):",tuple(selected_data))
#con.commit()
#con.close()
#query= 'frnd'
#query= query.strip().lower()
#cursor.execute("SELECT moblie_no FROM contact WHERE LOWER(name) like ?",('%'+query+'%',query+'%'))
#cursor.execute("SELECT moblie_no FROM contact WHERE LOWER(name) like ? OR LOWER(name) like ?", ('%' + query + '%', '%' + query + '%'))
#result = cursor.fetchall()
#sprint(result[0],[0])

name = "canva"
url = "https://www.canva.com/"
cursor.execute('''INSERT INTO web_command (name, url) VALUES (?, ?)''', (name, url))
con.commit()
id="2"
#cursor.execute('''DELETE FROM web_command WHERE id = ?''', (id,))
#con.commit()