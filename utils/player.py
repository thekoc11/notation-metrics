import numpy as np
from scipy.io.wavfile import write


F_s = 44100
N_s = 44100
omega = 440

centre_freq = 256
default_length = 44100

def get_freq_after_x_semitones(x=1, init_freq=256):
    return init_freq * (2 ** (float(x) / 12))

def get_sine_wave(freq, t_start=0, t_end=default_length, f_s=F_s):
    t = np.arange(t_start, t_end)
    return np.cos((t - t_start)/t_end) * (t_end - t_start) * np.sin(2 * np.pi * freq * t / f_s)

def save_to_pcm(wave, name='test.wav'):
    scaled = np.int16(wave/np.max(np.abs(wave)) * 32767)
    write(name, F_s, scaled)

class Player():
    def __init__(self, song_coords3d, label='default'):
        self.rest = 99999
        self.scale = 12
        self.centre_freq = centre_freq
        self.note_length = default_length
        self.f_s = F_s
        self.song_coords = song_coords3d
        self.song_length = -1
        self.name = label
        self.compute_variables()


    def compute_variables(self):
        t = []
        a = []
        for note, dur in zip(self.song_coords["melody"], self.song_coords["durations"]):
            freq = get_freq_after_x_semitones(note) if note < 99999 else get_freq_after_x_semitones(0, init_freq=0)
            event_dur = int(dur * self.note_length)

            wav = get_sine_wave(freq, t_start=len(t), t_end=len(t) + event_dur) if note < 99999 else get_sine_wave(0, t_start=len(t), t_end=len(t) + event_dur)
            t += list(np.arange(len(t), len(t) + event_dur))
            a += list(wav)
            print(len(a), len(t), t[0], t[-1])
        a = np.array(a, dtype='float64')
        save_to_pcm(a, '{}.wav'.format(self.name))



if __name__ == '__main__':
    # print(get_freq_after_x_semitones(0))
    x = np.arange(default_length * 12)
    data = np.zeros(x.shape, dtype='float64')
    for i in range(len(x)):
        begin = x[i] // default_length * default_length
        data[i] = np.sin(2 * np.pi * get_freq_after_x_semitones(x[i] / default_length) * x[i] / F_s)
        print(x[i]/default_length)

    scaled = np.int16(data/np.max(np.abs(data)) * 32767)
    write('test.wav', 44100, scaled)