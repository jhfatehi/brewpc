DROP SCHEMA IF EXISTS brewpc_test;
CREATE SCHEMA brewpc_test;
USE brewpc_test;

CREATE TABLE brews (
	brew_num int,
	batchs int,
	brand varchar(20),
	FV int,
	strtDATE date,
	finDATE date
    PRIMARY KEY(brew_num));
    
CREATE TABLE mash (
    brew_num int, 
	batch_num int,
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
	dFILLvol float,
    foreign key (brew_num) references brews(brew_num)
    ); 

CREATE TABLE boil (
	)

CREATE TABLE ko (
	)

CREATE TABLE process (
	brand varchar(20) NOT NULL,
	
	-- Mash
	tGRStemp float,
	tSTKtemp float,
	tMSHvol float,
	tMSHtemp float,
	tMASHphLOW float,
	tMASHphHI float,
	tSPGvol float,
	
	iWT1 varchar(30),
	iWT1lb float,
	iWT2 varchar(30),
	iWT2lb float,
	iWT3 varchar(30),
	iWT4lb float,
	iWT4 varchar(30),
	iWT5lb float,
	iWT5 varchar(30),
	iWT5lb float,

	iGST1 varchar(30),
	iGST1sk float,
	iGST1lb float,
	iGST2 varchar(30),
	iGST2sk float,
	iGST2lb float,
	iGST3 varchar(30),
	iGST3sk float,
	iGST3lb float,
	iGST4 varchar(30),
	iGST4sk float,
	iGST4lb float,
	iGST5 varchar(30),
	iGST5sk float,
	iGST5lb float,
	iGST6 varchar(30),
	iGST6sk float,
	iGST6lb float,
	iGST7 varchar(30),
	iGST7sk float,
	iGST7lb float,
	iGSTtotlb float,

	-- Boil


	-- Knock Out


    PRIMARY KEY (brand));
    
    
INSERT INTO process VALUES (0,0,0,0,0,0,0,0);