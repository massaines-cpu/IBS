import mne

raw = mne.io.read_raw_edf(
    '../data/raw/J1-1MB2012-LMG-edfplus.edf',
    preload=True,
)

epochs = mne.read_epochs(
    "../data/preprocessed/J1-1MB2012-LMG-edfplus_reconstruct-epo.fif"
)
print(len(epochs))
# print(epochs.metadata.head())
# print(epochs.metadata.columns)
# print(epochs.metadata)

metadata = epochs.metadata.copy()

metadata["event_code"] = metadata["label"]
metadata["window"] = metadata["segment_type"]

print(metadata[["label", "event_code", "window"]].head())
print(metadata["event_code"].value_counts())
print(metadata["segment_type"].value_counts())