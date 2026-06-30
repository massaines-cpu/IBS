import sqlite3
from pathlib import Path

#table dyades

conn = sqlite3.connect("ibs.db")
cursor = conn.cursor()

dyads = ["J1", "J2", "J4", "J5", "J7", "J8", "J10", "J15"]

for dyad in dyads:
    cursor.execute(
        "INSERT INTO dyads (dyad_id) VALUES (?)",
        (dyad,)
    )

conn.commit()

#les participants

folder = Path("../data/preprocessed")

for file in folder.glob("*.fif"):
    print(file.name)

# cursor.execute("""
# INSERT INTO participants
# (participant_id, dyad_id, role, preprocessed_path)
# VALUES (?, ?, ?, ?)
# """, (
#     participant_id,
#     dyad_id,
#     role,
#     str(file)
# ))