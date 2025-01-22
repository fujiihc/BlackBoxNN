# BlackBoxNN
Black Box Neural Network Modelling of Guitar Amplifiers and Effect Pedals

## Overview
This project was inspired by an interest in Neural Models for guitar effects after my friend introduced me to Neural DSP Plugins. 
As a data scientist and guitar player with an interest in messing around with pedal and amp electronics, this project was a natural choice.
It was originally for my Fall Semester DS340 AI/ML Final Project, but I've decided to take it further on my own time.

The paper [Real-Time Guitar Amplifier Emulation with Deep Learning](https://www.mdpi.com/2076-3417/10/3/766) helped inspire initial architectures and experiments, but my version has been modified.

All the work done is for Educational and Personal use.

## Datasets Explored
  - [IDMT-SMT-Guitar Dataset](https://zenodo.org/records/7544110)

  - [GuitarSet](https://zenodo.org/records/3371780)

  - [EGDB](https://drive.google.com/drive/folders/1h9DrB4dk4QstgjNaHh7lL7IMeKdYw82_)

  - All Other Data was Created By Me

## Table of Contents
  - [Data](/Data): Stores dry and wet audio files used for training, validation, and testing.

    <details><summary>Data Folder Structure</summary>
  
      ```
      /Data
        ├── Inputs/
        │   └── ...
        ├── <effect_name>/
        │   ├── <experiment_or_project_version>/
        │   │   ├── Train/
        │   │   │   ├── <effect_level>/
        │   │   │   │   ├── Dry/
        │   │   │   │   │   └── ...
        │   │   │   │   ├── Wet/
        │   │   │   │   │   └── ...
        │   │   │   └── ...
        │   │   ├── Val/
        │   │   │   ├── <effect_level>/
        │   │   │   │   ├── Dry/
        │   │   │   │   │   └── ...
        │   │   │   │   ├── Wet/
        │   │   │   │   │   └── ...
        │   │   │   └── ...
        │   │   ├── Test/
        │   │   │   ├── <effect_level>/
        │   │   │   │   ├── Dry/
        │   │   │   │   │   └── ...
        │   │   │   │   ├── Wet/
        │   │   │   │   │   └── ...
        │   │   │   └── ...
        │   └── ...   
        └── ...
      
      
      ```
    </details>
    
    **Note: Currently, Validation Data is just taken from Training Data. Training Data is not yet finalized.**

  - [Data Generation](/DataGeneration): Generates dry and wet audio files.

  - [Example Output](/ExampleOutput): Gives an output example of a model and its performance.

  - [Images](/Images): Stores images used in various README's in the repository.

  - [ModelResults](/ModelResults): Stores pickled Pandas dataframes of model performance on input dry audio.
    <details><summary>ModelResults Folder Structure</summary>
      
    ```
    /ModelResults
      ├── <effect_name>/
      │   ├── <experiment_or_project_version>/
      │   │   └── ...
      │   └── ...
      └── ...
    ```
    </details>

  - [Models](/Models): Stores trained models as well as their metadata and testing outputs.
    <details> <summary>Models Folder Structure</summary>
    
    ```
    /Models
      ├── <effect_name>/
      │   ├── <experiment_or_project_version>/
      │   │   ├── Model_<model_number>/
      │   │   │   ├── ...
      │   │   │   ├── Output/
      │   │   │   │   └── ...
      │   │   └── ...   
      │   └── ...
      └── ...
    ```
    </details>

  - [Notebooks](/Notebooks): Stores template notebooks for dataset prep, training, testing, and analyzing experiments as well as experiment specific notebooks.
    <details><summary>Notebooks Folder Structure</summary>
    
    ```
    /Notebooks
      ├── Templates/
      │   └── ...
      ├── <effect_name>/
      │   ├── <experiment_or_project_version>/
      │   │   └── ...
      │   └── ...   
      └── ...
    ```
    </details>

  - [TrainValPickles](/TrainValPickles): Stores pickles of x and y inputs and outputs used for training and validation of models.
    <details><summary>TrainValPickles Folder Structure</summary>

    ```
    /TrainValPickles
      ├── <effect_name>/
      │   ├── <experiment_or_project_version>/
      │   │  └── ... 
      │   └── ...     
      └── ...
    ```
    </details>

  - [WriteUps](/WriteUps): Contains README write ups for each experiment/project version.
    <details><summary>WriteUps Folder Structure</summary>

    ```
    /WriteUps
      ├── <effect_name>/
      │   ├── <experiment_or_project_version>/
      │   │  └── ... 
      │   └── ...     
      └── ...
    ```
    </details>

    
## To-Do/Future Plans
Model Other Effects, Model an Amplifier
  
  - Boss DS-1, Ibanez TS9, Marshall DSL20HR
  
  - Experiment with Cabinets and Impulse Responses

Improve LSTM Model Performance
  
  - Experiment with Context Size, Model Architectures, Train/Val Dataset Selection, Creating my own train set
    
Include Adjustable Parameters in Models
  
  - Tone, Level, Gain Controls for Starters
    
Create Real-Time Hardware Integration for Models
  
  - Allow Users to Load Models onto Physical Devices

Experiment With Hybrid Analog/Neural Net Based Devices
  
  - Model Subsections of Circuits and Integrate with Analog Circuits

