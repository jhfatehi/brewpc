# brewpc

This repository hosts the source code for a brew process control tool.

## Requirements

conda create -n brewpc python=2

conda activate brewpc

conda install -c conda-forge kivy

conda install -c conda-forge mysql-connector-python

conda install -c conda-forge sshtunnel

## Getting Started

### Create database

Navigate to input2 folder  
Run input2\_db.py (python input2\_db.py)  
This will create input2\_test.db

### Add path to database

Open db\_path file  
Input custom path  
Windows example: C:/Users/USERNAME/Documents/GitHub/brewpc/input2/input2\_test.db  
Linux example: /home/USERNAME/projects/brewpc/input2/input2\_test.db

### Launch GUI

Navigate to Source folder  
Run main.py (python main.py)
