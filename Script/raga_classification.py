# -*- coding: utf-8 -*-
"""Raga Classification

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GmqyvJl04TV9VW-Jy03Y3jXvNOJ1ivTG
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

# import os
# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

import os
import librosa
import yaml
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Paths to the audio and annotations
audio_path = '/kaggle/input/carnatic-music/carnatic_varnam_1.0/Audio'
annotations_path = '/kaggle/input/carnatic-music/carnatic_varnam_1.0/Notations_Annotations/annotations'


# List of ragas for classification
ragas = ['abhogi', 'begada', 'kalyani', 'mohanam', 'sahana', 'saveri', 'sri']

# Function to load audio and extract features (e.g., MFCCs)
def extract_features(file_path, n_mfcc=13):
    audio, sr = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    mfccs_mean = np.mean(mfccs.T, axis=0)
    return mfccs_mean

# Function to parse YAML notations or taala cycle annotations
def load_annotations(annotation_file):
    with open(annotation_file, 'r') as file:
        annotations = yaml.safe_load(file)
    return annotations

# Load all data and annotations
X = []
y = []

for raga in ragas:
    raga_folder = os.path.join(audio_path, raga)
    annotation_folder = os.path.join(annotations_path, 'taalas', raga)

    for audio_file in os.listdir(raga_folder):
        if audio_file.endswith('.wav'):  # Assuming audio files are in .wav format
            file_path = os.path.join(raga_folder, audio_file)
            features = extract_features(file_path)

            # Load corresponding annotation
            annotation_file = os.path.join(annotation_folder, audio_file.replace('.wav', '.yaml'))
            annotations = load_annotations(annotation_file)

            # Append features and corresponding raga label
            X.append(features)
            y.append(raga)

# Convert to numpy arrays
X = np.array(X)
y = np.array(y)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a baseline Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Predict and evaluate
y_pred = rf_classifier.predict(X_test)
print(classification_report(y_test, y_pred, target_names=ragas))

import os
import librosa
import yaml
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Paths to the audio and annotations
audio_path = '/path/to/Audio'
annotations_path = '/path/to/Notations_Annotations/annotations'

# List of ragas for classification
ragas = ['abhogi', 'begada', 'kalyani', 'mohanam', 'sahana', 'saveri', 'sri']

# Function to load audio and extract features (e.g., MFCCs)
def extract_features(file_path, n_mfcc=13):
    audio, sr = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    mfccs_mean = np.mean(mfccs.T, axis=0)
    return mfccs_mean

# Function to parse YAML notations or taala cycle annotations
def load_annotations(annotation_file):
    with open(annotation_file, 'r') as file:
        annotations = yaml.safe_load(file)
    return annotations

# Load all data and annotations
X = []
y = []

for raga in ragas:
    raga_folder = os.path.join(audio_path, raga)
    annotation_folder = os.path.join(annotations_path, 'taalas', raga)

    for audio_file in os.listdir(raga_folder):
        if audio_file.endswith('.wav'):  # Assuming audio files are in .wav format
            file_path = os.path.join(raga_folder, audio_file)
            features = extract_features(file_path)

            # Load corresponding annotation
            annotation_file = os.path.join(annotation_folder, audio_file.replace('.wav', '.yaml'))
            annotations = load_annotations(annotation_file)

            # Append features and corresponding raga label
            X.append(features)
            y.append(raga)

# Convert to numpy arrays
X = np.array(X)
y = np.array(y)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a baseline Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Predict and evaluate
y_pred = rf_classifier.predict(X_test)
print(classification_report(y_test, y_pred, target_names=ragas))



import os
import librosa
import yaml
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Path to dataset folders
AUDIO_PATH = "/path/to/carnatic_varnam_1.0/Audio"
ANNOTATIONS_PATH = "/path/to/carnatic_varnam_1.0/Notations_Annotations/annotations/taalas"

# Define ragas based on folder structure of annotations
ragas = ['abhogi', 'begada', 'kalyani', 'mohanam', 'sahana', 'saveri', 'sri']

# Helper function to extract MFCC features from audio
def extract_features(audio_file, sr=22050, n_mfcc=13):
    y, sr = librosa.load(audio_file, sr=sr)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return np.mean(mfcc.T, axis=0)

# Function to match audio files with their respective raga based on annotations
def match_audio_to_raga():
    data = []
    for raga in ragas:
        annotation_dir = os.path.join(ANNOTATIONS_PATH, raga)
        if os.path.isdir(annotation_dir):
            for annotation_file in os.listdir(annotation_dir):
                if annotation_file.endswith('.yaml'):
                    annotation_path = os.path.join(annotation_dir, annotation_file)
                    # Parse YAML file to get audio file reference
                    with open(annotation_path, 'r') as f:
                        annotation_data = yaml.safe_load(f)
                        # Loop through the cycles and match to audio files
                        for section in annotation_data.values():
                            for cycle in section:
                                # Assuming audio filenames follow a pattern that matches the annotation
                                audio_filename = f"{cycle}.wav"
                                audio_filepath = os.path.join(AUDIO_PATH, audio_filename)
                                if os.path.exists(audio_filepath):
                                    # Extract features
                                    features = extract_features(audio_filepath)
                                    data.append([features, raga])
    return data

# Preprocess data
data = match_audio_to_raga()
df = pd.DataFrame(data, columns=['features', 'label'])

# Split into features (X) and labels (y)
X = np.array(df['features'].tolist())
y = df['label']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict and evaluate model
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

import os
import librosa
import yaml
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Path to dataset folders
AUDIO_PATH = "/kaggle/input/carnatic-music/carnatic_varnam_1.0/Audio"
ANNOTATIONS_PATH = "/kaggle/input/carnatic-music/carnatic_varnam_1.0/Notations_Annotations/notations"

# Define ragas based on folder structure of annotations
ragas = ['abhogi', 'begada', 'kalyani', 'mohanam', 'sahana', 'saveri', 'sri']

# Helper function to extract MFCC features from audio
def extract_features(audio_file, sr=22050, n_mfcc=13):
    y, sr = librosa.load(audio_file, sr=sr)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return np.mean(mfcc.T, axis=0)

# Function to match audio files with their respective raga based on annotations
def match_audio_to_raga():
    data = []
    for raga in ragas:
        annotation_dir = os.path.join(ANNOTATIONS_PATH, raga)
        if os.path.isdir(annotation_dir):
            for annotation_file in os.listdir(annotation_dir):
                if annotation_file.endswith('.yaml'):
                    annotation_path = os.path.join(annotation_dir, annotation_file)
                    # Parse YAML file to get audio file reference
                    with open(annotation_path, 'r') as f:
                        annotation_data = yaml.safe_load(f)
                        # Loop through the cycles and match to audio files
                        for section in annotation_data.values():
                            for cycle in section:
                                # Assuming audio filenames follow a pattern that matches the annotation
                                audio_filename = f"{cycle}.wav"
                                audio_filepath = os.path.join(AUDIO_PATH, audio_filename)
                                if os.path.exists(audio_filepath):
                                    # Extract features
                                    features = extract_features(audio_filepath)
                                    print("Hello")
                                    data.append([features, raga])
    return data

# Preprocess data
data = match_audio_to_raga()
df = pd.DataFrame(data, columns=['features', 'label'])

# Split into features (X) and labels (y)
X = np.array(df['features'].tolist())
y = df['label']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict and evaluate model
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))



import os
import librosa
import yaml
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Path to dataset folders
AUDIO_PATH = "/path/to/carnatic_varnam_1.0/Audio"
ANNOTATIONS_PATH = "/path/to/carnatic_varnam_1.0/Notations_Annotations/annotations/taalas"

# Define ragas based on folder structure of annotations
ragas = ['abhogi', 'begada', 'kalyani', 'mohanam', 'sahana', 'saveri', 'sri']

# Helper function to extract MFCC features from audio
def extract_features(audio_file, sr=22050, n_mfcc=13):
    try:
        y, sr = librosa.load(audio_file, sr=sr)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
        return np.mean(mfcc.T, axis=0)
    except Exception as e:
        print(f"Error extracting features from {audio_file}: {e}")
        return None

# Function to match audio files with their respective raga based on annotations
def match_audio_to_raga():
    data = []
    for raga in ragas:
        annotation_dir = os.path.join(ANNOTATIONS_PATH, raga)
        if os.path.isdir(annotation_dir):
            print(f"Processing raga: {raga}")
            for annotation_file in os.listdir(annotation_dir):
                if annotation_file.endswith('.yaml'):
                    annotation_path = os.path.join(annotation_dir, annotation_file)
                    # Parse YAML file to get audio file reference
                    with open(annotation_path, 'r') as f:
                        annotation_data = yaml.safe_load(f)
                        # Loop through the cycles and match to audio files
                        for section in annotation_data.values():
                            for cycle in section:
                                # Assuming audio filenames follow a pattern that matches the annotation
                                audio_filename = f"{cycle}.wav"  # Verify this naming assumption
                                audio_filepath = os.path.join(AUDIO_PATH, audio_filename)
                                if os.path.exists(audio_filepath):
                                    print(f"Matching audio file: {audio_filename} to raga: {raga}")
                                    # Extract features
                                    features = extract_features(audio_filepath)
                                    if features is not None:
                                        data.append([features, raga])
                                else:
                                    print(f"Audio file {audio_filename} not found.")
    return data

# Preprocess data
data = match_audio_to_raga()

if len(data) == 0:
    print("No data found. Please check the audio filenames and annotations.")
else:
    df = pd.DataFrame(data, columns=['features', 'label'])

    # Split into features (X) and labels (y)
    X = np.array(df['features'].tolist())
    y = df['label']

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest Classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Predict and evaluate model
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

import os
import librosa
import yaml
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Path to dataset folders
AUDIO_PATH = "/kaggle/input/carnatic-music/carnatic_varnam_1.0/Audio"
ANNOTATIONS_PATH = "/kaggle/input/carnatic-music/carnatic_varnam_1.0/Audio"

# Define ragas based on folder structure of annotations
ragas = ['abhogi', 'begada', 'kalyani', 'mohanam', 'sahana', 'saveri', 'sri']

# Helper function to extract MFCC features from audio
def extract_features(audio_file, sr=22050, n_mfcc=13):
    try:
        y, sr = librosa.load(audio_file, sr=sr)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
        return np.mean(mfcc.T, axis=0)
    except Exception as e:
        print(f"Error extracting features from {audio_file}: {e}")
        return None

# Function to match audio files with their respective raga based on annotations
def match_audio_to_raga():
    data = []
    for raga in ragas:
        annotation_dir = os.path.join(ANNOTATIONS_PATH)
        if os.path.isdir(annotation_dir):
            print(f"Processing raga: {raga}")
            for annotation_file in os.listdir(annotation_dir):
                if annotation_file.endswith('.yaml'):
                    annotation_path = os.path.join(annotation_dir, annotation_file)
                    # Parse YAML file to get audio file reference
                    with open(annotation_path, 'r') as f:
                        annotation_data = yaml.safe_load(f)
                        # Loop through the cycles and match to audio files
                        for section in annotation_data.values():
                            for cycle in section:
                                # Assuming audio filenames follow a pattern that matches the annotation
                                audio_filename = f"{cycle}.wav"  # Verify this naming assumption
                                audio_filepath = os.path.join(AUDIO_PATH, audio_filename)
                                if os.path.exists(audio_filepath):
                                    print(f"Matching audio file: {audio_filename} to raga: {raga}")
                                    # Extract features
                                    features = extract_features(audio_filepath)
                                    if features is not None:
                                        data.append([features, raga])
                                else:
                                    print(f"Audio file {audio_filename} not found.")
    return data

# Preprocess data
data = match_audio_to_raga()

if len(data) == 0:
    print("No data found. Please check the audio filenames and annotations.")
else:
    df = pd.DataFrame(data, columns=['features', 'label'])

    # Split into features (X) and labels (y)
    X = np.array(df['features'].tolist())
    y = df['label']

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest Classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Predict and evaluate model
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

import os
import librosa
import yaml
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Path to dataset folders
AUDIO_PATH = "/kaggle/input/carnatic-music/carnatic_varnam_1.0/Audio"
ANNOTATIONS_PATH = "/kaggle/input/carnatic-music/carnatic_varnam_1.0/Notations_Annotations/notations"

# Define ragas based on folder structure of annotations
ragas = ['abhogi', 'begada', 'kalyani', 'mohanam', 'sahana', 'saveri', 'sri']

# Helper function to extract MFCC features from audio
def extract_features(audio_file, sr=22050, n_mfcc=13):
    try:
        y, sr = librosa.load(audio_file, sr=sr)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
        return np.mean(mfcc.T, axis=0)
    except Exception as e:
        print(f"Error extracting features from {audio_file}: {e}")
        return None

# Function to match audio files with their respective raga based on annotations
def match_audio_to_raga():
    data = []
    for raga in ragas:
#         annotation_dir = os.path.join(ANNOTATIONS_PATH, raga)
        annotation_dir = ANNOTATIONS_PATH
        if os.path.isdir(annotation_dir):
            print(f"Processing raga: {raga}")
            for annotation_file in os.listdir(annotation_dir):
                if annotation_file.endswith('.yaml'):
                    annotation_path = os.path.join(annotation_dir, annotation_file)
                    # Parse YAML file to get audio file reference
                    with open(annotation_path, 'r') as f:
                        annotation_data = yaml.safe_load(f)
                        # Loop through the cycles and match to audio files
                        for section in annotation_data.values():
                            for cycle in section:
                                # Assuming audio filenames follow a pattern that matches the annotation
                                audio_filename = f"{cycle}.wav"  # Verify this naming assumption
                                audio_filepath = os.path.join(AUDIO_PATH, audio_filename)
                                if os.path.exists(audio_filepath):
                                    print(f"Matching audio file: {audio_filename} to raga: {raga}")
                                    # Extract features
                                    features = extract_features(audio_filepath)
                                    if features is not None:
                                        data.append([features, raga])
                                else:
                                    print(f"Audio file {audio_filename} not found.")
    return data

# Preprocess data
data = match_audio_to_raga()

if len(data) == 0:
    print("No data found. Please check the audio filenames and annotations.")
else:
    df = pd.DataFrame(data, columns=['features', 'label'])

    # Split into features (X) and labels (y)
    X = np.array(df['features'].tolist())
    y = df['label']

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest Classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Predict and evaluate model
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_csv('/kaggle/input/dataset-ragas-excel/Dataset.csv')

# Separate features and target label
X = df.drop(columns=['filename', 'raga'])  # 'filename' is irrelevant for classification, 'raga' is the label
y = df['raga']

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')

# Detailed classification report
print(classification_report(y_test, y_pred))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_csv('/kaggle/input/dataset-ragas-excel/Dataset.csv')

# Separate features and target label
X = df.drop(columns=['filename', 'raga'])  # 'filename' is irrelevant for classification, 'raga' is the label
y = df['raga']

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Naive Bayes Classifier
nb = GaussianNB()

# Train the model
nb.fit(X_train, y_train)

# Make predictions on the test set
y_pred = nb.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')

# Detailed classification report
print(classification_report(y_test, y_pred))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_csv('/kaggle/input/dataset-ragas-excel/Dataset.csv')

# Separate features and target label
X = df.drop(columns=['filename', 'raga'])  # 'filename' is irrelevant for classification, 'raga' is the label
y = df['raga']

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define different SVM kernels to test
kernels = ['linear', 'rbf', 'poly']

# Loop through each kernel, train the model, and evaluate performance
for kernel in kernels:
    print(f"\nSVM with {kernel} kernel:")

    # Initialize SVM with the current kernel
    svm = SVC(kernel=kernel, random_state=42)

    # Train the SVM model
    svm.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = svm.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.4f}')

    # Detailed classification report
    print(classification_report(y_test, y_pred))