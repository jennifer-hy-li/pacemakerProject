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

-- ModelParameters Inserts
--- AOO
INSERT INTO modelparameters VALUES ('AOO', 'Lower Rate Limit', -1);
INSERT INTO modelparameters VALUES ('AOO', 'Upper Rate Limit', -1);
INSERT INTO modelparameters VALUES ('AOO', 'Atrial Amplitude', -1);
INSERT INTO modelparameters VALUES ('AOO', 'Atrial Pulse Width', -1);
--- VOO
INSERT INTO modelparameters VALUES ('VOO', 'Lower Rate Limit', -1);
INSERT INTO modelparameters VALUES ('VOO', 'Upper Rate Limit', -1);
INSERT INTO modelparameters VALUES ('VOO', 'Ventricular Amplitude', -1);
INSERT INTO modelparameters VALUES ('VOO', 'Ventricular Pulse Width', -1);
--- AAI
INSERT INTO modelparameters VALUES ('AAI', 'Lower Rate Limit', -1);
INSERT INTO modelparameters VALUES ('AAI', 'Upper Rate Limit', -1);
INSERT INTO modelparameters VALUES ('AAI', 'Atrial Amplitude', -1);
INSERT INTO modelparameters VALUES ('AAI', 'Atrial Pulse Width', -1);
INSERT INTO modelparameters VALUES ('AAI', 'Atrial Sensitivity', -1);
INSERT INTO modelparameters VALUES ('AAI', 'ARP', -1);
INSERT INTO modelparameters VALUES ('AAI', 'PVARP', -1);
INSERT INTO modelparameters VALUES ('AAI', 'Hysteresis', -1);
INSERT INTO modelparameters VALUES ('AAI', 'Rate Smoothing', -1);
--- VVI
INSERT INTO modelparameters VALUES ('VVI', 'Lower Rate Limit', -1);
INSERT INTO modelparameters VALUES ('VVI', 'Upper Rate Limit', -1);
INSERT INTO modelparameters VALUES ('VVI', 'Ventricular Amplitude', -1);
INSERT INTO modelparameters VALUES ('VVI', 'Ventricular Pulse Width', -1);
INSERT INTO modelparameters VALUES ('VVI', 'Ventricular Sensitivity', -1);
INSERT INTO modelparameters VALUES ('VVI', 'VRP', -1);
INSERT INTO modelparameters VALUES ('VVI', 'Hysteresis', -1);
INSERT INTO modelparameters VALUES ('VVI', 'Rate Smoothing', -1);
