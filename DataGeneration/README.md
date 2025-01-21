# DataGeneration
How to Create Train/Val/Test Data

## Overview
CreateMono.py converts Stereo to Mono.

PlayRecMono.py takes Mono files, and plays them through a Buffer Splitter (Boss RC-1 in this case), sending one signal to the Effect and the other signal directly to be recorded.

Both Dry and Wet signals are recorded at the same time so there is no latency between them.

## Set Up
![Set Up](../Images/DataGenerationImg/RecordingSetUp.jpg)

## Recording Settings

SD-1/DS340
  - Dry and Wet signals recorded at 20dB input at 44.1K Hz on Focusrite Scarlett 2i2 Gen 4
  - Tone and Level knobs at Noon
  - Low Gain: Drive at 9:00
  - Mid Gain: Drive at 12:00
  - High Gain: Drive at 3:00

DSL20HPreamp/UltraGain
  - Dry signals recorded at 20dB input at 44.1K Hz on Focusrite Scarlett 2i2 Gen 4
  - Wet signals recorded at 15dB input at 44.1K Hz on Focusrite Scarlett 2i2 Gen 4
  - Reverb, Resonance, and Presence knobs at 0
  - EQ knobs at at 5
  - Tone Shift off
  - Ultra Gain channel on
  - Volume at 10
  - Low Gain: Gain at 2
  - Mid Gain: Gain at 5
  - High Gain: Gain at 8
