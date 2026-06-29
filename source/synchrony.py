# calcul IBS, corrélation, PLV

def compute_correlation(eeg_a, eeg_b):
    pass

def compute_plv(eeg_a, eeg_b):
    pass

def compute_coherence(eeg_a, eeg_b):
    pass

def IBS(eeg_A, eeg_B, method='plv'):
    if method == 'plv':
        return compute_plv(eeg_A, eeg_B)
    elif method == 'coherence':
        return compute_coherence(eeg_A, eeg_B)
    else:
        return compute_correlation(eeg_A, eeg_B)
