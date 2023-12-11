import numpy as np

def voiced_excitation(duration, F0, Fs):
    '''
    Create voiced speeech excitation.
    
    @param:
    duration (scalar) - length of the excitation, in samples
    F0 (scalar) - pitch frequency, in Hertz
    Fs (scalar) - sampling frequency, in samples/second
    
    @returns:
    excitation (np.ndarray) - the excitation signal, such that
      excitation[n] = -1 if n is an integer multiple of int(np.round(Fs/F0))
      excitation[n] = 0 otherwise
    '''
    excitation = np.zeros(duration)
    period_samples = int(np.round(Fs / F0))
    excitation[::period_samples] = -1
    return excitation

def resonator(x, F, BW, Fs):
    '''
    Generate the output of a resonator.
    
    @param:
    x (np.ndarray(N)) - the excitation signal
    F (scalar) - resonant frequency, in Hertz
    BW (scalar) - resonant bandwidth, in Hertz
    Fs (scalar) - sampling frequency, in samples/second
    
    @returns:
    y (np.ndarray(N)) - resonant output
    '''
    omega = 2 * np.pi * F / Fs
    alpha = np.sin(omega) * np.sinh((np.log(2) / 2) * BW * omega / np.sin(omega))

    y = np.zeros(len(x))
    for n in range(2, len(x)):
        y[n] = 2 * np.cos(omega) * y[n-1] - y[n-2] + x[n] - 2 * np.cos(omega) * alpha * x[n-1] + alpha**2 * x[n-2]

    return y

def synthesize_vowel(duration,F0,F1,F2,F3,F4,BW1,BW2,BW3,BW4,Fs):
    '''
    Synthesize a vowel.
    
    @param:
    duration (scalar) - duration in samples
    F0 (scalar) - pitch frequency in Hertz
    F1 (scalar) - first formant frequency in Hertz
    F2 (scalar) - second formant frequency in Hertz
    F3 (scalar) - third formant frequency in Hertz
    F4 (scalar) - fourth formant frequency in Hertz
    BW1 (scalar) - first formant bandwidth in Hertz
    BW2 (scalar) - second formant bandwidth in Hertz
    BW3 (scalar) - third formant bandwidth in Hertz
    BW4 (scalar) - fourth formant bandwidth in Hertz
    Fs (scalar) - sampling frequency in samples/second
    
    @returns:
    speech (np.ndarray(samples)) - synthesized vowel
    '''
    excitation = voiced_excitation(duration, F0, Fs)

    resonator_1 = resonator(excitation, F1, BW1, Fs)
    resonator_2 = resonator(excitation, F2, BW2, Fs)
    resonator_3 = resonator(excitation, F3, BW3, Fs)
    resonator_4 = resonator(excitation, F4, BW4, Fs)

    speech = resonator_1 + resonator_2 + resonator_3 + resonator_4

    return speech
