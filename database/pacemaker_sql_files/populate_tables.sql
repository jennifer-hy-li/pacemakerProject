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
INSERT INTO modeparameters VALUES ('AOO', 'Lower Rate Limit', -1);
INSERT INTO modeparameters VALUES ('AOO', 'Upper Rate Limit', -1);
INSERT INTO modeparameters VALUES ('AOO', 'Atrial Amplitude', -1);
INSERT INTO modeparameters VALUES ('AOO', 'Atrial Pulse Width', -1);
--- VOO
INSERT INTO modeparameters VALUES ('VOO', 'Lower Rate Limit', -1);
INSERT INTO modeparameters VALUES ('VOO', 'Upper Rate Limit', -1);
INSERT INTO modeparameters VALUES ('VOO', 'Ventricular Amplitude', -1);
INSERT INTO modeparameters VALUES ('VOO', 'Ventricular Pulse Width', -1);
--- AAI
INSERT INTO modeparameters VALUES ('AAI', 'Lower Rate Limit', -1);
INSERT INTO modeparameters VALUES ('AAI', 'Upper Rate Limit', -1);
INSERT INTO modeparameters VALUES ('AAI', 'Atrial Amplitude', -1);
INSERT INTO modeparameters VALUES ('AAI', 'Atrial Pulse Width', -1);
INSERT INTO modeparameters VALUES ('AAI', 'Atrial Sensitivity', -1);
INSERT INTO modeparameters VALUES ('AAI', 'ARP', -1);
INSERT INTO modeparameters VALUES ('AAI', 'PVARP', -1);
INSERT INTO modeparameters VALUES ('AAI', 'Hysteresis', -1);
INSERT INTO modeparameters VALUES ('AAI', 'Rate Smoothing', -1);
--- VVI
INSERT INTO modeparameters VALUES ('VVI', 'Lower Rate Limit', -1);
INSERT INTO modeparameters VALUES ('VVI', 'Upper Rate Limit', -1);
INSERT INTO modeparameters VALUES ('VVI', 'Ventricular Amplitude', -1);
INSERT INTO modeparameters VALUES ('VVI', 'Ventricular Pulse Width', -1);
INSERT INTO modeparameters VALUES ('VVI', 'Ventricular Sensitivity', -1);
INSERT INTO modeparameters VALUES ('VVI', 'VRP', -1);
INSERT INTO modeparameters VALUES ('VVI', 'Hysteresis', -1);
INSERT INTO modeparameters VALUES ('VVI', 'Rate Smoothing', -1);

--- ###R version INSERTS
--- AOOR
INSERT INTO modeparameters VALUES ('AOOR', 'Lower Rate Limit', -1);
INSERT INTO modeparameters VALUES ('AOOR', 'Upper Rate Limit', -1);
INSERT INTO modeparameters VALUES ('AOOR', 'Atrial Amplitude', -1);
INSERT INTO modeparameters VALUES ('AOOR', 'Atrial Pulse Width', -1);
INSERT INTO modeparameters VALUES ('AOOR', 'Maximum Sensor Rate', -1);
INSERT INTO modeparameters VALUES ('AOOR', 'Activity Threshold', -1);
INSERT INTO modeparameters VALUES ('AOOR', 'Reaction Time', -1);
INSERT INTO modeparameters VALUES ('AOOR', 'Response Factor', -1);
INSERT INTO modeparameters VALUES ('AOOR', 'Recovery Time', -1);
--- VOOR
INSERT INTO modeparameters VALUES ('VOOR', 'Lower Rate Limit', -1);
INSERT INTO modeparameters VALUES ('VOOR', 'Upper Rate Limit', -1);
INSERT INTO modeparameters VALUES ('VOOR', 'Ventricular Amplitude', -1);
INSERT INTO modeparameters VALUES ('VOOR', 'Ventricular Pulse Width', -1);
INSERT INTO modeparameters VALUES ('VOOR', 'Maximum Sensor Rate', -1);
INSERT INTO modeparameters VALUES ('VOOR', 'Activity Threshold', -1);
INSERT INTO modeparameters VALUES ('VOOR', 'Reaction Time', -1);
INSERT INTO modeparameters VALUES ('VOOR', 'Response Factor', -1);
INSERT INTO modeparameters VALUES ('VOOR', 'Recovery Time', -1);
--- AAIR
INSERT INTO modeparameters VALUES ('AAIR', 'Lower Rate Limit', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'Upper Rate Limit', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'Atrial Amplitude', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'Atrial Pulse Width', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'Atrial Sensitivity', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'ARP', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'PVARP', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'Hysteresis', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'Rate Smoothing', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'Maximum Sensor Rate', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'Activity Threshold', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'Reaction Time', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'Response Factor', -1);
INSERT INTO modeparameters VALUES ('AAIR', 'Recovery Time', -1);
--- VVIR
INSERT INTO modeparameters VALUES ('VVIR', 'Lower Rate Limit', -1);
INSERT INTO modeparameters VALUES ('VVIR', 'Upper Rate Limit', -1);
INSERT INTO modeparameters VALUES ('VVIR', 'Ventricular Amplitude', -1);
INSERT INTO modeparameters VALUES ('VVIR', 'Ventricular Pulse Width', -1);
INSERT INTO modeparameters VALUES ('VVIR', 'Ventricular Sensitivity', -1);
INSERT INTO modeparameters VALUES ('VVIR', 'VRP', -1);
INSERT INTO modeparameters VALUES ('VVIR', 'Hysteresis', -1);
INSERT INTO modeparameters VALUES ('VVIR', 'Rate Smoothing', -1);
INSERT INTO modeparameters VALUES ('VVIR', 'Maximum Sensor Rate', -1);
INSERT INTO modeparameters VALUES ('VVIR', 'Activity Threshold', -1);
INSERT INTO modeparameters VALUES ('VVIR', 'Reaction Time', -1);
INSERT INTO modeparameters VALUES ('VVIR', 'Response Factor', -1);
INSERT INTO modeparameters VALUES ('VVIR', 'Recovery Time', -1);



