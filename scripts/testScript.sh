#!/bin/bash
sshpass -p 'hello' ssh pi@raspberrypiednaregina.local 'sudo python3 Sp24Test.py; exit'
python3 ~/School/Sp24/fileTransfer.py
