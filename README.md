# Raga Classification in Indian Classical Music

## Overview
This project aims to automate the classification of ragas from Indian classical music using machine learning techniques. The goal is to explore the feasibility of applying machine learning algorithms for raga classification based on audio recordings, along with ensuring interpretability through methods like LIME and SHAP.

## Table of Contents
- [Project Summary](#project-summary)
- [Objectives](#objectives)
- [Dataset](#dataset)
- [Methodology](#methodology)
  - [Data Preprocessing](#data-preprocessing)
  - [Feature Extraction](#feature-extraction)
  - [Models Used](#models-used)
- [Results](#results)
- [Interpretability and Explainability](#interpretability-and-explainability)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Summary
Indian classical music, particularly its ragas, has a deep emotional and cultural significance. However, classifying ragas from audio recordings presents unique challenges due to variability in performance, lack of standardized notation, and cultural nuances. This project focuses on using machine learning to classify ragas automatically and interpret the decisions made by the models to better understand the classification process.

## Objectives
- To evaluate various feature extraction techniques suitable for analyzing audio recordings of Indian classical music.
- To implement and compare different machine learning models for raga classification.
- To ensure that the developed models are interpretable, providing insights into the classification process.

## Dataset
The Carnatic Varnam dataset is used, consisting of 28 vocal recordings across 7 ragas. Each recording is sung by professional vocalists and is accompanied by taala annotations and notations. The dataset is structured for both melodic and rhythmic analysis.

A smaller dataset is also used for simpler model training with annotated audio segments corresponding to specific ragas.

## Methodology

### Data Preprocessing
- Normalization of audio volumes.
- Segmentation of audio into consistent segments for training.
- Conversion of audio signals into meaningful features like MFCCs, chroma features, and spectral properties.

### Feature Extraction
- **MFCCs (Mel-Frequency Cepstral Coefficients)**: Used to capture the timbral characteristics of the audio recordings.
- **Chroma Features**: These represent the energy distribution across the twelve pitch classes.
- **Spectral Properties**: Such as spectral contrast and zero-crossing rate (ZCR).

### Models Used
1. **CNN-LSTM**: A deep learning model that combines Convolutional Neural Networks (CNNs) and Long Short-Term Memory (LSTM) networks to capture both temporal and spatial information. It achieved a training accuracy of 98.63% and test accuracy of 86.73%.
2. **Decision Tree**: A simple model used for its interpretability, achieving 32.51% accuracy.
3. **Random Forest**: An ensemble method of decision trees with an accuracy of 59.11%.
4. **SVM (Support Vector Machine)**: A linear classifier with an accuracy of 66.75%.

## Results
The CNN-LSTM model performed the best in terms of accuracy, but it required significant computational resources. Simpler models like Decision Tree, Random Forest, and SVM, while offering lower accuracy, provided greater interpretability and insights into feature importance.

| Model            | Accuracy   |
|------------------|------------|
| CNN-LSTM         | 86.73%     |
| Random Forest    | 59.11%     |
| SVM (Linear)     | 66.75%     |
| Decision Tree    | 32.51%     |

## Interpretability and Explainability
- **LIME (Local Interpretable Model-agnostic Explanations)**: Applied to create local explanations of predictions, highlighting which features influence the model’s output for individual instances.
- **SHAP (SHapley Additive exPlanations)**: Used to assess global feature importance across the entire dataset.

Both LIME and SHAP were used to provide transparency in the decision-making process of the models, particularly with Random Forest and SVM, showing how MFCCs and chroma features were critical for accurate raga classification.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/raga-classification.git
