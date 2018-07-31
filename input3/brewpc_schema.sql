DROP SCHEMA IF EXISTS brewpc_test;
CREATE SCHEMA brewpc_test;
USE brewpc_test;

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
    
CREATE TABLE brews (
	brew_num int,
	batch int,
	size int,
	brand varchar(20),
    PRIMARY KEY(brew_num));
    
INSERT INTO process VALUES (0,0,0,0,0,0,0,0,0);