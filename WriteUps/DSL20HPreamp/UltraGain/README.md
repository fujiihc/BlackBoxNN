# DSL20HPreamp/UltraGain
Marshall DSL20H Preamp Modelling on the UltraGain Channel

## Overview
This is the first experiment with modelling a tube amplifier. 

This experiment aimed to model a Marshall DSL20H Preamp at varying gain levels, with the same model architecture and hyperparameters as [SD-1/DS340](../../../WriteUps/SD-1/DS340/README.md) to compare model performance in modelling a tube amp vs a solid-state pedal circuit.

This experiment specifically modelled the preamp section of the DSL20H, as I didn't have a load box or a way to attenuate the power amp. To record the output of the preamp, the signal was taken from FX Loop Send.

## Recording Settings
- Dry signals recorded at 20dB input at 44.1K Hz on Focusrite Scarlett 2i2 Gen 4
- Wet signals recorded at 15dB input at 44.1K Hz on Focusrite Scarlett 2i2 Gen 4
- Reverb, Resonance, and Presence knobs at 0
- EQ knobs at at 5
- Tone Shift off
- Ultra Gain Channel On
- Volume at 10
- Low Gain: Gain at 2
- Mid Gain: Gain at 5
- High Gain: Gain at 8

**Note: Resonance/Presence Knobs are part of the Power Amp circuit, and therefore have no effect on Preamp output.**

[Recordings](../../../Data/DSL20HPreamp/UltraGain)

[Recording Set Up](../../../DataGeneration)

## Training/Validation Data
Data was split into context chunks WITH NO overlap. The x data was a single chunk of dry audio with size n, and the y data was the corresponding wet audio output sample.

[Training/Validation Data](../../../TrainValPickles/DSL20HPreamp/UltraGain)

## Model Architecture
All models consisted of a single LSTM layer, fed into a single Dense layer.

## Hyperparameters
These hyperparameter combinations resulted in 36 models. 

Variable Hyperparameters:
  - Gain Levels on Marshall DSL20H Preamp: "Low", "Mid", "High"
  - Training/Validation Data Context Sizes: 44, 66, 88 samples (Corresponding to 1, 1.5, and 2 ms with a sample rate of 44.1K)
  - LSTM Hidden Unit Sizes: 64 and 96 units
  - Model Learning Rates: 0.01 and 0.0001

Fixed Hyperparameters:
  - Patience/Early Stopping: 15
  - Batch Size: 64
  - Epochs: 200
  - Training Data Shuffled: True
  - Random State: 25
  - Sample Rate: 44.1K
  - All models trained on approximately 75K data samples relative to Context Size
  - Adam Optimizer used
  - Loss Function: ESR Loss

**Note: Number of Epochs was increased to 200 to allow models more time to converge. This appeared to be a limiting factor with [SD-1/DS340](../../../WriteUps/SD-1/DS340/README.md).**

## Metrics
ESR loss (Error to Signal Ratio) was used as the loss function for all models. MSE and MAE were also observed as well.

## Testing Data
All models were tested on [battery.wav](../../../Data/Inputs/battery.wav), [electricEye.wav](../../../Data/Inputs/electricEye.wav), [holywar.wav](../../../Data/Inputs/holywar.wav), [ohwell.wav](../../../Data/Inputs/ohwell.wav), [sanitarium.wav](../../../Data/Inputs/sanitarium.wav), and [shadowlove.wav](../../../Data/Inputs/shadowlove.wav). These were chosen for their diversity in speed and complexity. It also would take too long to test all 36 models on all of the song samples. ESR loss for the model's predictions vs the true DSL20H Preamp's output was saved. The output audio files were also saved.

## Results

## Conclusions

## Takeaways
