-- parameters inserts
INSERT INTO parameters VALUES ('Lower Rate Limit');
INSERT INTO parameters VALUES ('Upper Rate Limit');
INSERT INTO parameters VALUES ('Maximum Sensor Rate');
INSERT INTO parameters VALUES ('Fixed AV Delay');
INSERT INTO parameters VALUES ('Sensed AV Delay Offset');
INSERT INTO parameters VALUES ('Atrial Amplitude');
INSERT INTO parameters VALUES ('Ventricular Amplitude');
INSERT INTO parameters VALUES ('Atrial Pulse Width');
INSERT INTO parameters VALUES ('Ventricular Pulse Width');
INSERT INTO parameters VALUES ('Atrial Sensitivity');
INSERT INTO parameters VALUES ('Ventricular Sensitivity');
INSERT INTO parameters VALUES ('VRP');
INSERT INTO parameters VALUES ('ARP');
INSERT INTO parameters VALUES ('PVARP');
INSERT INTO parameters VALUES ('PVARP Extension');
INSERT INTO parameters VALUES ('Hysteresis');
INSERT INTO parameters VALUES ('Rate Smoothing');
INSERT INTO parameters VALUES ('ATR Duration');
INSERT INTO parameters VALUES ('ATR Fallback Mode');
INSERT INTO parameters VALUES ('ATR Fallback Time');
INSERT INTO parameters VALUES ('Activity Threshold');
INSERT INTO parameters VALUES ('Reaction Time');
INSERT INTO parameters VALUES ('Response Factor');
INSERT INTO parameters VALUES ('Recovery Time');

-- Mode inserts
INSERT INTO mode VALUES ('AOO');
INSERT INTO mode VALUES ('VOO');
INSERT INTO mode VALUES ('AAI');
INSERT INTO mode VALUES ('VVI');
INSERT INTO mode VALUES ('AOOR');
INSERT INTO mode VALUES ('VOOR');
INSERT INTO mode VALUES ('AAIR');
INSERT INTO mode VALUES ('VVIR');


-- modeparameters Inserts
--- AOO
INSERT INTO modeparameters VALUES ('AOO', 'Lower Rate Limit', 1, 60, 30, 175,5);
INSERT INTO modeparameters VALUES ('AOO', 'Upper Rate Limit', 2,120, 50, 175,5);
INSERT INTO modeparameters VALUES ('AOO', 'Atrial Amplitude', 3,5,0, 5.0,0.1);
INSERT INTO modeparameters VALUES ('AOO', 'Atrial Pulse Width',4,1 ,1,30,1);
--- VOO
INSERT INTO modeparameters VALUES ('VOO', 'Lower Rate Limit',5, 60, 30, 175,5);
INSERT INTO modeparameters VALUES ('VOO', 'Upper Rate Limit',6, 120, 50, 175,5);
INSERT INTO modeparameters VALUES ('VOO', 'Ventricular Amplitude',7,5,0, 5.0,0.1);
INSERT INTO modeparameters VALUES ('VOO', 'Ventricular Pulse Width',8, 1 ,1,30,1);
--- AAI
INSERT INTO modeparameters VALUES ('AAI', 'Lower Rate Limit',9,60, 30, 175,5);
INSERT INTO modeparameters VALUES ('AAI', 'Upper Rate Limit',10, 120, 50, 175,5);
INSERT INTO modeparameters VALUES ('AAI', 'Atrial Amplitude',11, 5,0, 5.0,0.1);
INSERT INTO modeparameters VALUES ('AAI', 'Atrial Pulse Width',12, 1 ,1,30,1);
INSERT INTO modeparameters VALUES ('AAI', 'Atrial Sensitivity',13, 0, 0, 5, 0.1);
INSERT INTO modeparameters VALUES ('AAI', 'ARP',14, 250, 150, 500, 10);
INSERT INTO modeparameters VALUES ('AAI', 'PVARP',15, 250, 150, 500, 10);
INSERT INTO modeparameters VALUES ('AAI', 'Hysteresis',16, 0, 0, 1, 1);
INSERT INTO modeparameters VALUES ('AAI', 'Rate Smoothing', 17,0, 0, 25,3);
--- VVI
INSERT INTO modeparameters VALUES ('VVI', 'Lower Rate Limit',18,60, 30, 175,5);
INSERT INTO modeparameters VALUES ('VVI', 'Upper Rate Limit',19, 120, 50, 175,5);
INSERT INTO modeparameters VALUES ('VVI', 'Ventricular Amplitude', 20,5,0, 5.0,0.1);
INSERT INTO modeparameters VALUES ('VVI', 'Ventricular Pulse Width',21, 1 ,1,30,1);
INSERT INTO modeparameters VALUES ('VVI', 'Ventricular Sensitivity',22, 0, 0, 5, 0.1);
INSERT INTO modeparameters VALUES ('VVI', 'VRP',23, 320, 150, 500, 10);
INSERT INTO modeparameters VALUES ('VVI', 'Hysteresis',24, 0, 0, 1, 1);
INSERT INTO modeparameters VALUES ('VVI', 'Rate Smoothing',25,0, 0, 25,3);

--- ###R version INSERTS
--- AOOR
INSERT INTO modeparameters VALUES ('AOOR', 'Lower Rate Limit',26, 60, 30, 175,5);
INSERT INTO modeparameters VALUES ('AOOR', 'Upper Rate Limit',27, 120, 50, 175,5);
INSERT INTO modeparameters VALUES ('AOOR', 'Atrial Amplitude',28, 5,0, 5.0,0.1);
INSERT INTO modeparameters VALUES ('AOOR', 'Atrial Pulse Width',29, 1 ,1,30,1);
INSERT INTO modeparameters VALUES ('AOOR', 'Maximum Sensor Rate',30,120 ,50,175, 5);
INSERT INTO modeparameters VALUES ('AOOR', 'Activity Threshold',31, 0, 0, 5, 1);
INSERT INTO modeparameters VALUES ('AOOR', 'Reaction Time',32, 30, 10, 50, 10);
INSERT INTO modeparameters VALUES ('AOOR', 'Response Factor',33,  8, 1, 16, 8);
INSERT INTO modeparameters VALUES ('AOOR', 'Recovery Time',34, 5, 2, 16, 1);
--- VOOR
INSERT INTO modeparameters VALUES ('VOOR', 'Lower Rate Limit',35,60, 30, 175,5);
INSERT INTO modeparameters VALUES ('VOOR', 'Upper Rate Limit',36, 120, 50, 175,5);
INSERT INTO modeparameters VALUES ('VOOR', 'Ventricular Amplitude',37, 5,0, 5.0,0.1);
INSERT INTO modeparameters VALUES ('VOOR', 'Ventricular Pulse Width',38,  1 ,1,30,1);
INSERT INTO modeparameters VALUES ('VOOR', 'Maximum Sensor Rate',39, 120 ,50,175, 5);
INSERT INTO modeparameters VALUES ('VOOR', 'Activity Threshold',40, 0, 0, 5, 1);
INSERT INTO modeparameters VALUES ('VOOR', 'Reaction Time',41, 30, 10, 50, 10);
INSERT INTO modeparameters VALUES ('VOOR', 'Response Factor',42,  8, 1, 16, 8);
INSERT INTO modeparameters VALUES ('VOOR', 'Recovery Time',43, 5, 2, 16, 1);
--- AAIR
INSERT INTO modeparameters VALUES ('AAIR', 'Lower Rate Limit',44, 60, 30, 175,5);
INSERT INTO modeparameters VALUES ('AAIR', 'Upper Rate Limit',45, 120, 50, 175,5);
INSERT INTO modeparameters VALUES ('AAIR', 'Atrial Amplitude',46, 5,0, 5.0,0.1);
INSERT INTO modeparameters VALUES ('AAIR', 'Atrial Pulse Width',47, 1 ,1,30,1);
INSERT INTO modeparameters VALUES ('AAIR', 'Atrial Sensitivity',48, 0, 0, 5, 0.1);
INSERT INTO modeparameters VALUES ('AAIR', 'ARP',49, 250, 150, 500, 10);
INSERT INTO modeparameters VALUES ('AAIR', 'PVARP',50, 250, 150, 500, 10);
INSERT INTO modeparameters VALUES ('AAIR', 'Hysteresis',51, 0, 0, 1, 1);
INSERT INTO modeparameters VALUES ('AAIR', 'Rate Smoothing',52, 0, 0, 25,3);
INSERT INTO modeparameters VALUES ('AAIR', 'Maximum Sensor Rate',53,120 ,50,175, 5);
INSERT INTO modeparameters VALUES ('AAIR', 'Activity Threshold',3, 0, 0, 5, 1);
INSERT INTO modeparameters VALUES ('AAIR', 'Reaction Time',55, 30, 10, 50, 10);
INSERT INTO modeparameters VALUES ('AAIR', 'Response Factor',56, 8, 1, 16, 8);
INSERT INTO modeparameters VALUES ('AAIR', 'Recovery Time',57, 5, 2, 16, 1);
--- VVIR
INSERT INTO modeparameters VALUES ('VVIR', 'Lower Rate Limit',58, 60, 30, 175,5);
INSERT INTO modeparameters VALUES ('VVIR', 'Upper Rate Limit',59, 120, 50, 175,5);
INSERT INTO modeparameters VALUES ('VVIR', 'Ventricular Amplitude',60, 5,0, 5.0,0.1);
INSERT INTO modeparameters VALUES ('VVIR', 'Ventricular Pulse Width',61, 1 ,1,30,1);
INSERT INTO modeparameters VALUES ('VVIR', 'Ventricular Sensitivity',62, 0, 0, 5, 0.1);
INSERT INTO modeparameters VALUES ('VVIR', 'VRP',63, 320, 150, 500, 10);
INSERT INTO modeparameters VALUES ('VVIR', 'Hysteresis',64, 0, 0, 1, 1);
INSERT INTO modeparameters VALUES ('VVIR', 'Rate Smoothing',65, 0, 0, 25,3);
INSERT INTO modeparameters VALUES ('VVIR', 'Maximum Sensor Rate',66, 120 ,50,175, 5);
INSERT INTO modeparameters VALUES ('VVIR', 'Activity Threshold',67, 0, 0, 5, 1);
INSERT INTO modeparameters VALUES ('VVIR', 'Reaction Time',68, 30, 10, 50, 10);
INSERT INTO modeparameters VALUES ('VVIR', 'Response Factor',69,  8, 1, 16, 8);
INSERT INTO modeparameters VALUES ('VVIR', 'Recovery Time',70,  5, 2, 16, 1);



