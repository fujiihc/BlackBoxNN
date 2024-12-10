import sounddevice as sd
import os
import librosa as lb
import soundfile as sf

sampleRate = 44100
channels = 2


sd.default.device = (20,17)
sd.default.samplerate = sampleRate
sd.default.channels = channels
#20 Analogue 1 + 2 (Focusrite USB Audio), Windows WASAPI (4 in, 0 out)
#17 Speakers (Focusrite USB Audio), Windows WASAPI (0 in, 2 out)
#find a way to work with ASIO?


audioFilePath = ""
storageDir = ""
outputDir = ""
#make sure clean and distorted are recorded on the correct channels
#otherwise switch them

#might be stored in a subdirectory
counter = 0
for root, dirs, files in os.walk(f"{audioFilePath}{storageDir}"):
    for file in files:
        if file.endswith(".wav"):
            path = os.path.join(root,file)
            audio, sr = lb.load(path,sr=sampleRate, mono = True)
            recordedAudio = sd.playrec(audio, samplerate = sampleRate, channels = channels)
            sd.wait()
            wetL = recordedAudio[:,0]
            dryR = recordedAudio[:,1]
            #can also use "PCM_16"
            #include directory where files will be saved
            sf.write(f"{audioFilePath}{outputDir}/Wet/w_{file}", wetL, sampleRate, subtype='PCM_24')
            sf.write(f"{audioFilePath}{outputDir}/Dry/d_{file}", dryR, sampleRate, subtype='PCM_24') 
            #print(counter)
            counter +=1


print("All files processed")

