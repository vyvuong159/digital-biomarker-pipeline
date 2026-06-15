# Digital Biomarker Pipeline: Mild Cognitive Impairment (MCI) Detection

## Project Overview
This project aims to reproduce the paper *["Smartwatch- and smartphone-based remote assessment of brain health and detection of mild cognitive impairment"](https://pmc.ncbi.nlm.nih.gov/articles/PMC11922773/)* by Butler et al., Nat Med., 2025. The paper assesses whether everyday data from smartphones and smartwatches can help detect Mild Cognitive Impairment (MCI). MCI is an early stage of memory loss that can lead to Alzheimer's disease. We want to see if the subtle ways people use their devices can act as early warning signs for brain health.

This repository contains a modular, end-to-end data pipeline designed to preprocess the data, combine multiple health tracking streams, and train a machine learning model to accurately identify early signs of MCI.

### Rationale
Right now, to check someone’s memory, a doctor usually has to sit down with them in a clinic and ask them to complete pen-and-paper tests.

* The Problem: These tests only happen once in a while, can make patients nervous, and people sometimes get better at them just by practicing.
* The Solution: People use smartphones and smartwatches every single day. By safely tracking small patterns, like how fast someone types or how much they walk, we might be able to spot memory changes early, right from the comfort of their own home.

### Research Questions & Hypotheses
* **Research quetion 1:** Can short, brain-game apps accurately tell the difference between someone with early memory loss and someone with healthy aging?
    * *Hypothesis 1:* Yes. People with early memory loss will make noticeably more mistakes and take longer to solve visual puzzles on the apps because the areas of the brain responsible for short-term memory are the first to experience subtle decline.

* **Research quetion 2:** Is the computer better at spotting memory loss when it looks at everything combined (phone habits + watch data + health surveys) rather than just looking at one piece of data alone?
    * *Hypothesis 2:* Yes. Combining all the data will be much more accurate because early memory loss changes many parts of a person's life at once, affecting physical activity, sleep cycles, and daily typing rhythm all at the same time.

### Key Objectives
* **Data integrity:** Implementing robust cleaning pipelines for noisy, multi-source longitudinal health data
* **Signal reliability:** Distinguishing true behavioral patterns from device-related data gaps (synchronization delays, non-wear time)
* **Clinical insight:** Translating passive behavioral telemetry into meaningful constructs that assist in longitudinal health monitoring

## Datasets (synthetic)
*Note: The datasets contained in this repository are synthetic and created for demonstration purposes only. They do not contain any Protected Health Information (PHI) or real-world user data.*

**1. Baseline health profile**
- What it is: This includes a person's age, gender, education level, responses to memory surveys, scores from specialized touchscreen brain games, and a label indicating their clinical status (Healthy vs. MCI). Level: Participant level (one row per person).
- Purpose: Provides the basic info about the participant and "ground truth" to train models that distinguish between healthy individuals and those with early signs of cognitive impairment.

**2. The brain-game apps (cam-cog burst data)**
- What it is: Records of 2-minute cognitive games (like memory tests) on an app performed 3 times a day for 2 weeks. Level: Session level (one row per game session).
- Purpose: Captures how cognitive performance fluctuates throughout the day, providing a more accurate "real-world" view than a single, one-time test.

**3. Remote doctor check-ups**
- What it is: Results from professional cognitive assessments conducted remotely via video call. Level: Participant level (one row per assessment).
- Purpose: Acts as our "gold standard" or reliable answer key. We compare these expert-verified results against our automated digital signals to prove the system's accuracy.

**4. Passive smartphone habit telemetry**
- What it is: Automated logs of daily phone interaction habits, including how fast a person types, how long they hold down keys when messaging, how often they unlock their phone, and how many text messages they send. Level: Daily/Event level (one row per day or interaction).
- Purpose: Tracks "micro-behaviors" which serve as subtle, non-intrusive indicators of how a user’s coordination and engagement levels change over time.

**5. Passive health kit**
- What it is: Continuous data streaming from wearable devices, including heart rate, sleep quality, and daily step counts. Level: Daily level (one row per day per person).
- Purpose: Provides lifestyle context. Includes a daily *wear-time* flag. Our cleaning pipeline strictly utilizes this to filter out days where the device was not worn for at least 4 hours, ensuring our analysis is based on genuine behavioral trajectories rather than device inactivity.

## Data Processing (in-progress)
- Wear time filtering: in the Passive health kit data, only keep wearables wear-time >=4 hrs
- Longitudinal metric aggregation: Convert long-format timeseries tables into static, participant-level features using individual descriptive statistical definitions:
    - Health/Sensor Kit: Compute the participant-level Mean and Standard Deviation for heart rate variability, daily step count, and keyboard key hold time
    - Cam-Cog Burst: Compute the Slope over the 14 days to capture individual learning/practice curves across the sessions.
- Feature merging: Merge all aggregated metrics into the baseline dataset
- Outlier and missingness treatment: 
    - Cap extreme physiological noise at the 1st and 99th percentiles
    - Impute remaining missing values utilizing K-Nearest Neighbors (KNN) Imputation (\(K=5\)) based on demographic indices
- Feature standardization: Scale all 176 quantitative cognitive columns using StandardScaler to yield a mean of 0 and standard deviation of 1

## Exploratory Data Analysis (in-progress)
- Demographic profile table: Compute the distribution of Age, Sex, and Education stratified cleanly by MCI_Status
- Construct validity vorrelations: Run a Pearson Correlation ($r$) matrix between `PAL_Total_Errors_Adjusted` and the gold-standard `Tele_MoCA_Total_Score` from the validation cohort. Verify that an inverse relationship exists ($r \approx -0.31$ to $-0.35$)
- Feature distribution mapping: Generate box plots tracking the divergence of typing flight-times, learning slopes, and step counts across both classification boundaries

## Modeling (in-progress)
- Class imbalance mitigation: To protect the model from the severe baseline class imbalance (556 MCI vs. 16,234 Controls), apply a 3:1 majority-to-minority bootstrap downsampling strategy strictly within the training folds to avoid data leakage.
- Nested cross-validation: Implement a 5-fold outer/ 3-fold inner cross-validation loop
    - Inner Loop: Used to grid search optimal hyperparameter values for the regularization penalty coefficient ($\alpha$)
    - Outer Loop: Used to estimate generalized clinical error
- Main model: Train a Logistic Regression model with Ridge Penalization (L2 Regularization)
- Evaluation metrics: Compute and track the Mean AUROC (Area Under the Receiver Operating Characteristic), Sensitivity, Specificity, and F1-score across the cross-validation folds


## Project Structure
- `data/`: Sample synthetic datasets used for pipeline testing
- `src/`: Reusable Python modules for data cleaning, feature engineering, and signal diagnostic logic
- `notebooks/`: Exploratory Data Analysis (EDA) and clinical validation experiments
- `tests/`: Basic unit tests for critical signal-processing functions
- `docs/`: Methodological documentation and rationale behind health-metric design

## Technical Highlights
* **Longitudinal modeling:** The pipeline is built to handle repeated-measures data, accounting for temporal variability in user engagement
* **Engineering logic:** Cleaning strategies are informed by the engineering constraints of the sensors (e.g., handling backfilled cache data vs. true non-use)
* **Modularity:** Designed for maintainability, with clear separation between raw data processing and feature engineering

## Getting Started
1. Clone the repo: `git clone https://github.com/yourusername/digital-biomarker-pipeline.git`
2. Install requirements: `pip install -r requirements.txt`
3. Run the pipeline diagnostics: `pytest tests/`
