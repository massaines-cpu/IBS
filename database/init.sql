CREATE TABLE IF NOT EXISTS dyads (
    dyad_id TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS participants (
    participant_id TEXT PRIMARY KEY,
    dyad_id TEXT NOT NULL,
    role TEXT,
    raw_path TEXT,
    preprocessed_path TEXT,
    FOREIGN KEY (dyad_id) REFERENCES dyads(dyad_id)
);

CREATE TABLE IF NOT EXISTS epochs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dyad_id TEXT NOT NULL,
    participant_id TEXT NOT NULL,
    epoch_index INTEGER NOT NULL,
    event_code TEXT,
    segment_type TEXT,
    tmin REAL,
    tmax REAL,
    FOREIGN KEY (dyad_id) REFERENCES dyads(dyad_id),
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id)
);

CREATE TABLE IF NOT EXISTS labels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dyad_id TEXT NOT NULL,
    epoch_index INTEGER NOT NULL,
    synchrony_label INTEGER,
    FOREIGN KEY (dyad_id) REFERENCES dyads(dyad_id)
);

CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dyad_id TEXT NOT NULL,
    epoch_index INTEGER NOT NULL,
    predicted_label INTEGER,
    probability REAL,
    model_version TEXT,
    created_at TEXT
);