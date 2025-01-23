# SD-1/ContextExperiments
Boss SD-1 Modelling with Experiments Adjusting the Context Size Hyperparameter

## Overview
This was the first continuation of the project from [SD-1/DS340](../../../WriteUps/SD-1/DS340/README.md). The results from SD-1/DS340 indicated that increasing context size for the models to learn from might improve performance. This experiment centered around training models with the same hyperparameters on increasing levels of context to see how well they would perform.

## Recording Settings

- Dry and Wet signals recorded at 20dB input at 44.1K Hz on Focusrite Scarlett 2i2 Gen 4
- Tone and Level knobs at Noon
- Mid Gain: Drive at 12:00

The recordings used for this dataset were the same recordings used for SD-1/DS340: [Recordings](../../../Data/SD-1/DS340)
    
## Training/Validation Data 
Data was split into context chunks of size n WITH overlap. The x data was a single chunk of dry audio with size n, and the y data was the corresponding wet audio output sample.

Context chunk overlap was included when creating the x data because at higher contexts, there weren't enough samples in the audio to create a large enough dataset with no overlap. 100000 x y pairs were randomly sampled from all of the chunks generated. 75% of those pairs were used for training, and 25% for validation.

[Training/Validation Data](../../../TrainValPickles/SD-1/ContextExperiments)

## Model Architecture
All models consisted of a single LSTM layer, fed into a single Dense layer.

## Hyperparameters
These hyperparameter combinations resulted in 10 models. 

Variable Hyperparameters:
  - Training/Validation Data Context Sizes: 44, 88, 132, 176, 220, 264, 308, 352, 396, and 440 samples (Corresponding to 1-10 ms with a sample rate of 44.1K)

Fixed Hyperparameters:
  - Gain Level on Boss SD-1: "Mid"
  - LSTM Hidden Unit Size: 64
  - Model Learning Rate: 0.001
  - Train Data Size: 75000
  - Validation Data Size: 25000
  - Patience/Early Stopping: 15
  - Batch Size: 64
  - Epochs: 100
  - Training Data Shuffled: True
  - Random State: 25
  - Sample Rate: 44.1K
  - Adam Optimizer used
  - Loss Function: ESR Loss

## Metrics
ESR loss (Error to Signal Ratio) was used as the loss function for all models. MSE and MAE were also observed as well.

## Testing Data
All models were tested on [battery.wav](../../../Data/Inputs/battery.wav), [electricEye.wav](../../../Data/Inputs/electricEye.wav), [holywar.wav](../../../Data/Inputs/holywar.wav), [ohwell.wav](../../../Data/Inputs/ohwell.wav), [sanitarium.wav](../../../Data/Inputs/sanitarium.wav), and [shadowlove.wav](../../../Data/Inputs/shadowlove.wav). ESR loss for the model's predictions vs the true SD-1 output was saved. The output audio files were also saved.

## Results


## Conclusions


## Takeaways

