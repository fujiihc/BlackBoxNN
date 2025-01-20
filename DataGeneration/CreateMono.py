
import os
import librosa as lb
import soundfile as sf


#use this code to convert stereo clips into mono
#guitar signals are mono, so this is necessary for the model

sampleRate = 44100
channels = 1


audioFilePath = ""
storageDir = ""
outputDir = ""

counter = 0
#might be stored in a subdirectory
for root, dirs, files in os.walk(f"{audioFilePath}/{storageDir}"):
    for file in files:
        if file.endswith(".wav"):
            path = os.path.join(root,file)
            audio, sr = lb.load(path,sr=sampleRate, mono = True)
            #can also use "PCM_16"
            #include directory where files will be saved
            os.makedirs(f"{audioFilePath}/{outputDir}", exist_ok=True)
            sf.write(f"{audioFilePath}/{outputDir}/{file}", audio, sampleRate, subtype="PCM_24")
            #print(counter)
            counter += 1
            
print("All files processed")
