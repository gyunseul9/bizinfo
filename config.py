'''
use mysql
create database DB_NAME default character set utf8;
create user 'DB_NAME'@'localhost' identified by 'PASSWORD';
create user 'DB_NAME'@'127.0.0.1' identified by 'PASSWORD';
grant all privileges on DB_NAME.* to 'gyunseul9'@'localhost';
grant all privileges on DB_NAME.* to 'gyunseul9'@'127.0.0.1';
flush privileges;
quit;

CREATE TABLE rnd (
  num int(11) NOT NULL AUTO_INCREMENT,
  seq varchar(50) NOT NULL,
  kind varchar(100) NOT NULL,
  title varchar(100) NOT NULL,
  period varchar(100) NOT NULL,
  goverment varchar(100) NOT NULL,
  posted varchar(100) NOT NULL,
  summary varchar(255) NOT NULL,
  support varchar(255) NOT NULL,
  papers varchar(255) NOT NULL,
  point varchar(255) NOT NULL,
  question varchar(255) NOT NULL,
  rdate datetime DEFAULT NOW(),
  primary key (num)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
END'''

class Configuration:

  def get_configuration(choose):

    if(choose == 'local'):
      connect_value = dict(host='HOST_NAME',
        user='USER_ID',
        password='PASSWORD',
        database='DATABASE',
        port=3307,
        charset='utf8')
      
    elif(choose == 'ubuntu'):
      connect_value = dict(host='HOST_NAME',
        user='USER_ID',
        password='PASSWORD',
        database='DATABASE',
        port=3307,
        charset='utf8')

    else:
      print('Not Selected')
      connect_value = ''

    return connect_value
  