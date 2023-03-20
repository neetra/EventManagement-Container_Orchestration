
create database devopsroles;
use devopsroles;

CREATE TABLE test_table (
  name VARCHAR(20),
  color VARCHAR(10)
);

INSERT INTO test_table
  (name, color)
VALUES
  ('dev', 'blue'),
  ('pro', 'yellow');



CREATE TABLE events (
  id VarCHAR(50),
  Name VARCHAR(100) Not NULL  ,
  HostBy varchar(50),
  TimeStamp datetime null,
  description varchar(255) null
 ); 


insert into events (id, name, HostBy, Description) values (UUID_SHORT(), 'gudipadwa', 'netra amrale', 'descr');



