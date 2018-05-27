DROP SCHEMA IF EXISTS brewpc;
CREATE SCHEMA brewpc;
USE brewpc;

CREATE TABLE test (
	brew_num int, 
	batch int, 
	size int, 
	brand varchar(20), 
	data1 float, 
	data2 float, 
	data3 float);

CREATE TABLE mash (
	brew_num int,
	batch int,
	size int,
	brand varchar(20),
	dGRStemp float,
	dSTKtemp float,
	dMSHvol float,
	dMSHtemp float,
	dMSHtime time,
	dBREWsig varchar(20),
	dRNCvol float,
	dVLFtime time,
	dMASHph float,
	d1RNvol float,
	dSPGvol float,
	dROFtime time,
	dRACKcnt int,
	dFILLtime time,
	dFILLvol float);

CREATE TABLE process (
	size int,
	brand varchar(20),
	tGRStemp float,
	tSTKtemp float,
	tMSHvol float,
	tMSHtemp float,
	tMASHphLOW float,
	tMASHphHI float,
	tSPGvol float);