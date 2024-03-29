DROP SCHEMA IF EXISTS brewpc_test;
CREATE SCHEMA brewpc_test;
USE brewpc_test;

CREATE TABLE brews (
	brew_num int,
	batches int,
	brand varchar(20),
	FV int,
	strtDATE date,
	finDATE date,
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
	d1RNp float,
	dSPGvol float,
	dROFtime time,
	dRACKcnt int,
	dFILLtime time,
	dFILLvol float,
	dMASHnote varchar(280),
    foreign key (brew_num) references brews(brew_num)
    ); 

CREATE TABLE boil (
	brew_num int, 
	batch_num int,
	dBOILtime time,
	dHOP1time time,
	dIGp float,
	dIPH float,
	dLIQ1gal float,
	dHOP2time time,
	dZINCtime time,
	dKICKtime time,
	dHOP3time time,
	dMESLVLbbl float,
	dMESGp float,
	dLIQ2gal float,
	dFNLLVLbbl float,
	dFNLGp float,
	dFNLPH float,
	dBOILnote varchar(280),
	foreign key (brew_num) references brews(brew_num)
	);

CREATE TABLE ko (
	brew_num int, 
	batch_num int,
	dKOSRTtime time,
	dKOsig varchar(20),
	dKOtemp float,
	dO2lpm float,
	dO2ppm float,
	dKOENDtime time,
	dFMVOLbbl float,
	dCLDFVbbl float,
	dBD600sig varchar(20),
	dBD900sig varchar(20),
	dBD1200sig varchar(20),
	dBD1500sig varchar(20),
	dOGp float,
	dYSTGEN int,
	dSRCFV int,
	dSRCNUM int,
	dAMTPTCHs float,
	dFRMTEMPsig varchar(20),
	dAFOoz float,
	dAFOsig varchar(20),
	dKOnote varchar(280),
	foreign key (brew_num) references brews(brew_num)
	);

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
	iWT3lb float,
	iWT4 varchar(30),
	iWT4lb float,
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
	tFG float,
	tBOILphLO float,
	tBOILphHI float,

	iZNg float,
	iKICKoz float,

	iHOP1 varchar(30),
	iHOP1kg float,
	iHOP1min float,
	iHOP2 varchar(30),
	iHOP2kg float,
	iHOP2min float,
	iHOP3 varchar(30),
	iHOP3kg float,
	iHOP3min float,
	iHOP4 varchar(30),
	iHOP4kg float,
	iHOP4min float,
	iHOP5 varchar(30),
	iHOP5kg float,
	iHOP5min float,
	iHOP6 varchar(30),
	iHOP6kg float,
	iHOP6min float,
	iHOP7 varchar(30),
	iHOP7kg float,
	iHOP7min float,

	-- Knock Out
	tWASTEbbl float,
	tFERMf float,
	tYEASTtype varchar(5),

    PRIMARY KEY (brand));
    
    
INSERT INTO process VALUES (
	0,0,0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,0);