import sounddevice as sd
import os
import librosa as lb
import soundfile as sf

sampleRate = 44100
channels = 2
#Use this to find out what Input and Output devices to use
#print(sd.query_devices())
sd.default.device = (20,17)
sd.default.samplerate = sampleRate
sd.default.channels = channels
#20 Analogue 1 + 2 (Focusrite USB Audio), Windows WASAPI (4 in, 0 out)
#17 Speakers (Focusrite USB Audio), Windows WASAPI (0 in, 2 out)
#find a way to work with ASIO?


effect = "SD-1"
projVer = "DS340"
gain = ""
testOrTrain = "Test"

#make sure clean and distorted are recorded on the correct channels
#otherwise switch them

counter = 0
for root, dirs, files in os.walk(f"../Data/Inputs"):
    for file in files:
        if file.endswith(".wav"):
            path = os.path.join(root,file)
            audio, sr = lb.load(path,sr=sampleRate, mono = True)
            recordedAudio = sd.playrec(audio, samplerate = sampleRate, channels = channels)
            sd.wait()
            #switch based on setup
            L = recordedAudio[:,0]
            R = recordedAudio[:,1]
            #can also use "PCM_16"
            directory = f"../Data/{effect}/{projVer}/{testOrTrain}/{gain}"
            os.makedirs(f"{directory}/Wet", exist_ok=True)
            os.makedirs(f"{directory }/Dry", exist_ok=True)
            #swap left and right according to how your interface is set up
            sf.write(f"{directory}/Wet/w_{file}", R, sampleRate, subtype='PCM_24')
            sf.write(f"{directory}/Dry/d_{file}", L, sampleRate, subtype='PCM_24')  
            #print(counter)
            counter +=1


print("All files processed")

