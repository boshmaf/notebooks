import wave, random, struct, re
from builtins import TypeError
import math

def pitchToFrequency(pitch_notation):
    MAP = { 'A': 1,
            'B': 3,
            'C': 4,
            'D': 6,
            'E': 8,
            'F': 9,
            'G': 11, }
    frequency = 16
    match = re.match('([ABCDEFG])([\+\-]?)([0123456789]?)', pitch_notation)
    if match:
        index = MAP[match.group(1)]
        if match.group(2) == '+':
            index += 1
        elif match.group(2) == '-':
            index -= 1
        if match.group(3):
            index += ( 12 * int(match.group(3)) )
        frequency = 441 * math.pow(2, ( index - 61 ) / 12 )
#     print(frequency)
    return frequency

def inst_raw(i, wavelength):
    value = (5000 * math.sin( i * (2 * math.pi / wavelength) ))
    return value

def inst_raw2(i, wavelength):
    value = (5000 * math.sin( i * (2 * math.pi / wavelength) ))   \
            + (2500 * math.sin( i * (2 * math.pi / (2 * wavelength))))
    return value

def inst_raw3(i, wavelength):
    value = (5000 * math.sin( i * (2 * math.pi / wavelength) ))   \
            + (2500 * math.sin( i * (2 * math.pi / (2 * wavelength))))   \
            + (1250 * math.sin( i * (2 * math.pi / (4 * wavelength))))
    return value

def inst_third(i, wavelength):
    value = (4000 * math.sin( i * (2 * math.pi / wavelength) ))   \
            + (2000 * math.sin( i * (2 * math.pow(2, (4/12) * math.pi / wavelength ))))
    return value

def inst_fourth(i, wavelength):
    value = (4000 * math.sin( i * (2 * math.pi / wavelength) ))   \
            + (2000 * math.sin( i * (2 * math.pow(2, (5/12)) * math.pi / wavelength)))
    return value

def inst_fifth(i, wavelength):
    value = (4000 * math.sin( i * (2 * math.pi / wavelength) ))   \
            + (2000 * math.sin( i * (2 * math.pow(2, (7/12)) * math.pi / wavelength)))
    return value

INSTRUMENT_WAVEFUNCTIONS = {
                            'raw': inst_raw,
                            'raw2': inst_raw2,
                            'raw3': inst_raw3,
                            'third': inst_third,
                            'fourth': inst_fourth,
                            'fifth': inst_fifth,
                            }

class Note():
    def __init__(self, framerate, pitch='A', length=1, intensity=0, noise=0, instrument='raw'):
        self.framerate = framerate
        self.pitch = pitch
        self.length = length
        self.intensity = intensity
        self.noise = noise
        self.instrument = instrument
        
        self.frequency = pitchToFrequency(self.pitch)
        self.wavelength = self.framerate / self.frequency
        self.wavefunction = INSTRUMENT_WAVEFUNCTIONS[self.instrument]
    
    def toBytes(self):
        values = []
        for i in range(0, round(self.length * self.framerate)):
            value = self.intensity + self.wavefunction(i, self.wavelength)
#                     + random.randint(-self.noise, self.noise)   \
            packed_value = struct.pack('h', round(value))
            values.append(packed_value)
            values.append(packed_value)
        value_bytes = (b''.join(values))
        return value_bytes

class Sequence():
    def __init__(self, framerate=44100, intensity=0, instrument=None):
        self.notes = []
        self.framerate = framerate
        self.intensity = intensity
        self.instrument = instrument
    
    def add(self, note):
        if type(note) == Note:
            self.notes.append(note)
        else:
            raise TypeError('Should be a Note object')
    
    def addNote(self, *args, **kwargs):
        if not 'instrument' in kwargs.keys() and self.instrument:
            kwargs['instrument'] = self.instrument
        if not 'instrument' in kwargs.keys() and self.intensity:
            kwargs['intensity'] = self.intensity
        self.notes.append(Note(self.framerate, *args, **kwargs))
    
    def writeWav(self, filename):
        noise_output = wave.open(filename+'.wav', 'w')
        noise_output.setparams((2, 2, self.framerate, 0, 'NONE', 'not compressed'))
        value_bytes = b''
        for note in self.notes:
            value_bytes += note.toBytes()
        noise_output.writeframes(value_bytes)
        noise_output.close()