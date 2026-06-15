import pandas as pd
import numpy as np
import random

from .config import (
    N_MCI, N_CONTROLS,
    BASELINE_N_CANTAB_FEATURES,
    BASELINE_AGE_MCI, BASELINE_AGE_CONTROLS,
    BASELINE_SEX_MCI_FEMALE_RATIO, BASELINE_SEX_CONTROLS_FEMALE_RATIO,
    BASELINE_EDU_MCI_LOW_RATIO, BASELINE_EDU_CONTROLS_LOW_RATIO,
    BASELINE_CFI_MCI, BASELINE_CFI_CONTROLS,
    BASELINE_ECOG_MCI, BASELINE_ECOG_CONTROLS,
    BASELINE_CFI_ITEM_NOISE, BASELINE_ECOG_ITEM_NOISE,
    BASELINE_PAL_ERRORS_MCI, BASELINE_PAL_ERRORS_CONTROLS,
    BASELINE_SWM_ERRORS_MCI, BASELINE_SWM_ERRORS_CONTROLS,
    BASELINE_PRM_CORRECT_MCI, BASELINE_PRM_CORRECT_CONTROLS,
    BASELINE_MTS_TIME_MCI, BASELINE_MTS_TIME_CONTROLS,
    BASELINE_PADDING_NOISE_MEAN, BASELINE_PADDING_NOISE_STD,
    CAMCOG_N_DAYS, CAMCOG_SESSIONS_PER_DAY, CAMCOG_MISSINGNESS_RATE,
    CAMCOG_DSST_MCI, CAMCOG_DSST_CONTROLS, CAMCOG_DSST_NOISE, CAMCOG_DSST_DAY_IMPROVEMENT,
    CAMCOG_NBACK_MCI, CAMCOG_NBACK_CONTROLS, CAMCOG_NBACK_NOISE, CAMCOG_NBACK_DAY_IMPROVEMENT,
    CAMCOG_DISTRACTION_RATE_MCI, CAMCOG_DISTRACTION_RATE_CONTROLS,
    TELEMOCA_N_VALIDATION, TELEMOCA_MCI_OVERSAMPLING_RATIO,
    TELEMOCA_TOTAL_MCI, TELEMOCA_TOTAL_CONTROLS,
    TELEMOCA_DELAYED_RECALL_MCI, TELEMOCA_DELAYED_RECALL_CONTROLS,
    TELEMOCA_ATTENTION_MCI, TELEMOCA_ATTENTION_CONTROLS,
    TELEMOCA_EXECUTIVE_MCI, TELEMOCA_EXECUTIVE_CONTROLS,
    TELEMOCA_ORIENTATION_FRACTION, TELEMOCA_MIS_MULTIPLIER,
    TELEMOCA_MIS_NOISE_MCI, TELEMOCA_MIS_NOISE_CONTROLS,
    TELEMOCA_TECHNICAL_VALIDITY_RATE,
    SENSORKIT_N_WEEKS,
    SENSORKIT_TAPS_MCI, SENSORKIT_TAPS_CONTROLS, SENSORKIT_TAPS_NOISE,
    SENSORKIT_HOLD_TIME_MCI, SENSORKIT_HOLD_TIME_CONTROLS, SENSORKIT_HOLD_TIME_NOISE,
    SENSORKIT_FLIGHT_TIME_MCI, SENSORKIT_FLIGHT_TIME_CONTROLS, SENSORKIT_FLIGHT_TIME_NOISE,
    SENSORKIT_UNLOCKS_MCI, SENSORKIT_UNLOCKS_CONTROLS, SENSORKIT_UNLOCKS_NOISE,
    SENSORKIT_MSG_MULTIPLIER, SENSORKIT_MSG_BASE_NOISE_MCI, SENSORKIT_MSG_BASE_NOISE_CONTROLS, SENSORKIT_MSG_BASE,
    SENSORKIT_LOCATIONS_LAMBDA_MCI, SENSORKIT_LOCATIONS_LAMBDA_CONTROLS,
    HEALTHKIT_N_DAYS, HEALTHKIT_WEAR_TIME_THRESHOLD,
    HEALTHKIT_STEPS_MCI, HEALTHKIT_STEPS_CONTROLS, HEALTHKIT_STEPS_NOISE, HEALTHKIT_STEPS_MIN, HEALTHKIT_STEPS_MAX,
    HEALTHKIT_HRV_MCI, HEALTHKIT_HRV_CONTROLS, HEALTHKIT_HRV_NOISE, HEALTHKIT_HRV_MIN, HEALTHKIT_HRV_MAX,
    HEALTHKIT_DEEP_SLEEP_MCI, HEALTHKIT_DEEP_SLEEP_CONTROLS, HEALTHKIT_DEEP_SLEEP_NOISE,
    HEALTHKIT_WEAR_TIME_MCI, HEALTHKIT_WEAR_TIME_CONTROLS, HEALTHKIT_WEAR_TIME_NOISE,
    HEALTHKIT_SLEEP_COLLECTION_RATE, HEALTHKIT_REM_MULTIPLIER, HEALTHKIT_REM_NOISE,
    HEALTHKIT_CORE_BASE, HEALTHKIT_CORE_NOISE,
    HEALTHKIT_HR_MCI, HEALTHKIT_HR_CONTROLS, HEALTHKIT_HR_MIN, HEALTHKIT_HR_MAX,
)

class SyntheticDataGenerator:
    """
    A class to reproduce the multidimensional data footprint of the Nature Medicine (2025) study:
    'Smartwatch- and smartphone-based remote assessment of brain health and detection of MCI'.
    
    Generates 5 distinct synthetic datasets embedding true demographic shifts, clinical baseline 
    abilities, and performance variances between healthy controls and Mild Cognitive Impairment (MCI).
    """
    def __init__(self, seed=42):
        self.seed = seed
        np.random.seed(self.seed)
        
        # Core Study Sizing Elements
        self.n_mci = N_MCI
        self.n_controls = N_CONTROLS
        self.n_total = self.n_mci + self.n_controls
        
        # Map participant list and ground truths internally to maintain tracking alignment across tables
        self.participant_ids = [f'SUB_{i:05d}' for i in range(self.n_total)]
        self.mci_status_map = {f'SUB_{i:05d}': (1 if i < self.n_mci else 0) for i in range(self.n_total)}

    def generate_baseline_dataset(self):
        """1. Builds the core matrix containing 176 CANTAB cognitive variables and survey scores."""
        mci_status = np.array([1] * self.n_mci + [0] * self.n_controls)
        
        # Demographics
        age_mci = np.clip(np.random.normal(loc=BASELINE_AGE_MCI['loc'], scale=BASELINE_AGE_MCI['scale'], size=self.n_mci), BASELINE_AGE_MCI['min'], BASELINE_AGE_MCI['max'])
        age_controls = np.clip(np.random.normal(loc=BASELINE_AGE_CONTROLS['loc'], scale=BASELINE_AGE_CONTROLS['scale'], size=self.n_controls), BASELINE_AGE_CONTROLS['min'], BASELINE_AGE_CONTROLS['max'])
        ages = np.concatenate([age_mci, age_controls])

        sex_mci = np.random.choice([1, 0], size=self.n_mci, p=[BASELINE_SEX_MCI_FEMALE_RATIO, 1 - BASELINE_SEX_MCI_FEMALE_RATIO])
        sex_controls = np.random.choice([1, 0], size=self.n_controls, p=[BASELINE_SEX_CONTROLS_FEMALE_RATIO, 1 - BASELINE_SEX_CONTROLS_FEMALE_RATIO])
        sexes = np.concatenate([sex_mci, sex_controls])

        edu_mci = np.random.choice([1, 0], size=self.n_mci, p=[BASELINE_EDU_MCI_LOW_RATIO, 1 - BASELINE_EDU_MCI_LOW_RATIO])
        edu_controls = np.random.choice([1, 0], size=self.n_controls, p=[BASELINE_EDU_CONTROLS_LOW_RATIO, 1 - BASELINE_EDU_CONTROLS_LOW_RATIO])
        educations = np.concatenate([edu_mci, edu_controls])

        # Subjective Surveys
        cfi_mci = np.clip(np.random.normal(loc=BASELINE_CFI_MCI['loc'], scale=BASELINE_CFI_MCI['scale'], size=self.n_mci), BASELINE_CFI_MCI['min'], BASELINE_CFI_MCI['max'])
        cfi_controls = np.clip(np.random.normal(loc=BASELINE_CFI_CONTROLS['loc'], scale=BASELINE_CFI_CONTROLS['scale'], size=self.n_controls), BASELINE_CFI_CONTROLS['min'], BASELINE_CFI_CONTROLS['max'])
        cfi_totals = np.concatenate([cfi_mci, cfi_controls])

        ecog_mci = np.clip(np.random.normal(loc=BASELINE_ECOG_MCI['loc'], scale=BASELINE_ECOG_MCI['scale'], size=self.n_mci), BASELINE_ECOG_MCI['min'], BASELINE_ECOG_MCI['max'])
        ecog_controls = np.clip(np.random.normal(loc=BASELINE_ECOG_CONTROLS['loc'], scale=BASELINE_ECOG_CONTROLS['scale'], size=self.n_controls), BASELINE_ECOG_CONTROLS['min'], BASELINE_ECOG_CONTROLS['max'])
        ecog_totals = np.concatenate([ecog_mci, ecog_controls])

        df = pd.DataFrame({
            'Participant_ID': self.participant_ids,
            'Age': ages,
            'Sex_Female': sexes,
            'Education_Low': educations,
            'CFI_Total': cfi_totals,
            'ECog_12_Total': ecog_totals,
            'MCI_Status': mci_status
        })

        # Derive individual item-level mock metrics for surveys
        for i in range(1, 15):
            df[f'CFI_Q{i}'] = np.clip(df['CFI_Total'] / 14 + np.random.normal(0, BASELINE_CFI_ITEM_NOISE, self.n_total), 0, 1)
        for i in range(1, 13):
            df[f'ECog_Q{i}'] = np.clip(df['ECog_12_Total'] + np.random.normal(0, BASELINE_ECOG_ITEM_NOISE, self.n_total), 1.0, 4.0)

        # Generate primary landmark CANTAB tasks
        cantab_features = {}
        pal_err_mci = np.random.normal(loc=BASELINE_PAL_ERRORS_MCI['loc'], scale=BASELINE_PAL_ERRORS_MCI['scale'], size=self.n_mci)
        pal_err_ctrl = np.random.normal(loc=BASELINE_PAL_ERRORS_CONTROLS['loc'], scale=BASELINE_PAL_ERRORS_CONTROLS['scale'], size=self.n_controls)
        cantab_features['PAL_Total_Errors_Adjusted'] = np.clip(np.concatenate([pal_err_mci, pal_err_ctrl]), BASELINE_PAL_ERRORS_MCI['min'], BASELINE_PAL_ERRORS_MCI['max'])

        swm_err_mci = np.random.normal(loc=BASELINE_SWM_ERRORS_MCI['loc'], scale=BASELINE_SWM_ERRORS_MCI['scale'], size=self.n_mci)
        swm_err_ctrl = np.random.normal(loc=BASELINE_SWM_ERRORS_CONTROLS['loc'], scale=BASELINE_SWM_ERRORS_CONTROLS['scale'], size=self.n_controls)
        cantab_features['SWM_Strategy_Errors'] = np.clip(np.concatenate([swm_err_mci, swm_err_ctrl]), BASELINE_SWM_ERRORS_MCI['min'], BASELINE_SWM_ERRORS_MCI['max'])

        prm_mci = np.random.normal(loc=BASELINE_PRM_CORRECT_MCI['loc'], scale=BASELINE_PRM_CORRECT_MCI['scale'], size=self.n_mci)
        prm_ctrl = np.random.normal(loc=BASELINE_PRM_CORRECT_CONTROLS['loc'], scale=BASELINE_PRM_CORRECT_CONTROLS['scale'], size=self.n_controls)
        cantab_features['PRM_Delayed_Percent_Correct'] = np.clip(np.concatenate([prm_mci, prm_ctrl]), BASELINE_PRM_CORRECT_MCI['min'], BASELINE_PRM_CORRECT_MCI['max'])

        mts_mci = np.random.normal(loc=BASELINE_MTS_TIME_MCI['loc'], scale=BASELINE_MTS_TIME_MCI['scale'], size=self.n_mci)
        mts_ctrl = np.random.normal(loc=BASELINE_MTS_TIME_CONTROLS['loc'], scale=BASELINE_MTS_TIME_CONTROLS['scale'], size=self.n_controls)
        cantab_features['MTS_8_Box_Search_Time'] = np.clip(np.concatenate([mts_mci, mts_ctrl]), BASELINE_MTS_TIME_MCI['min'], BASELINE_MTS_TIME_MCI['max'])

        # Pad out parallel noise spaces to secure exact N=176 cognitive outcomes array
        for i in range(len(cantab_features), BASELINE_N_CANTAB_FEATURES):
            base_signal = df['MCI_Status'].values * np.random.normal(0.2, 0.1)
            cantab_features[f'CANTAB_Metric_{i+1}'] = base_signal + np.random.normal(BASELINE_PADDING_NOISE_MEAN, BASELINE_PADDING_NOISE_STD, self.n_total)

        df_cantab = pd.DataFrame(cantab_features)
        return pd.concat([df, df_cantab], axis=1).sample(frac=1).reset_index(drop=True)

    def generate_cam_cog_burst(self, days=CAMCOG_N_DAYS, sessions_per_day=CAMCOG_SESSIONS_PER_DAY):
        """2. Builds the long-format High-Frequency Burst Testing Dataset (N-Back and DSST)."""
        rows = []
        for p_id in self.participant_ids:
            is_mci = self.mci_status_map[p_id]
            base_dsst = np.random.normal(loc=CAMCOG_DSST_MCI['loc'], scale=CAMCOG_DSST_MCI['scale']) if is_mci else np.random.normal(loc=CAMCOG_DSST_CONTROLS['loc'], scale=CAMCOG_DSST_CONTROLS['scale'])
            base_nback = np.random.normal(loc=CAMCOG_NBACK_MCI['loc'], scale=CAMCOG_NBACK_MCI['scale']) if is_mci else np.random.normal(loc=CAMCOG_NBACK_CONTROLS['loc'], scale=CAMCOG_NBACK_CONTROLS['scale'])

            for day in range(1, days + 1):
                for session in range(1, sessions_per_day + 1):
                    if np.random.rand() > CAMCOG_MISSINGNESS_RATE:
                        dsst_score = int(np.clip(base_dsst + np.random.normal(0, CAMCOG_DSST_NOISE) + (day * CAMCOG_DSST_DAY_IMPROVEMENT), 0, 90))
                        nback_d = np.clip(base_nback + np.random.normal(0, CAMCOG_NBACK_NOISE) + (day * CAMCOG_NBACK_DAY_IMPROVEMENT), -1.0, 4.0)
                        distracted = 1 if np.random.rand() < (CAMCOG_DISTRACTION_RATE_MCI if is_mci else CAMCOG_DISTRACTION_RATE_CONTROLS) else 0
                        
                        rows.append({
                            'Participant_ID': p_id, 'MCI_Status': is_mci, 'Burst_Quarter': 1, 'Study_Day': day,
                            'Session_Numeric': session, 'DSST_Total_Correct': dsst_score, 'N_Back_D_Prime': round(nback_d, 4),
                            'Session_Marked_Distracted': distracted
                        })
        return pd.DataFrame(rows)

    def generate_tele_research(self, n_validation=TELEMOCA_N_VALIDATION):
        """3. Generates a clinical Validation/Sub-Study matrix containing Tele-MoCA parameters."""
        # Biased distribution towards impaired/complaining individuals as done in tele-calls triggers
        n_mci_val = int(n_validation * TELEMOCA_MCI_OVERSAMPLING_RATIO)
        mci_status = np.array([1] * n_mci_val + [0] * (n_validation - n_mci_val))
        
        # Random sample subset of IDs
        val_ids = list(np.random.choice(self.participant_ids, size=n_validation, replace=False))
        
        rows = []
        for i, p_id in enumerate(val_ids):
            status = mci_status[i]
            total = int(np.clip(np.random.normal(loc=TELEMOCA_TOTAL_MCI['loc'], scale=TELEMOCA_TOTAL_MCI['scale']) if status == 1 else np.random.normal(loc=TELEMOCA_TOTAL_CONTROLS['loc'], scale=TELEMOCA_TOTAL_CONTROLS['scale']), TELEMOCA_TOTAL_MCI['min'], TELEMOCA_TOTAL_MCI['max']))
            
            if status == 1:
                dr = int(np.clip(np.random.normal(loc=TELEMOCA_DELAYED_RECALL_MCI['loc'], scale=TELEMOCA_DELAYED_RECALL_MCI['scale']), TELEMOCA_DELAYED_RECALL_MCI['min'], TELEMOCA_DELAYED_RECALL_MCI['max']))
                att = int(np.clip(np.random.normal(loc=TELEMOCA_ATTENTION_MCI['loc'], scale=TELEMOCA_ATTENTION_MCI['scale']), TELEMOCA_ATTENTION_MCI['min'], TELEMOCA_ATTENTION_MCI['max']))
                exec_fn = int(np.clip(np.random.normal(loc=TELEMOCA_EXECUTIVE_MCI['loc'], scale=TELEMOCA_EXECUTIVE_MCI['scale']), TELEMOCA_EXECUTIVE_MCI['min'], TELEMOCA_EXECUTIVE_MCI['max']))
            else:
                dr = int(np.clip(np.random.normal(loc=TELEMOCA_DELAYED_RECALL_CONTROLS['loc'], scale=TELEMOCA_DELAYED_RECALL_CONTROLS['scale']), TELEMOCA_DELAYED_RECALL_CONTROLS['min'], TELEMOCA_DELAYED_RECALL_CONTROLS['max']))
                att = int(np.clip(np.random.normal(loc=TELEMOCA_ATTENTION_CONTROLS['loc'], scale=TELEMOCA_ATTENTION_CONTROLS['scale']), TELEMOCA_ATTENTION_CONTROLS['min'], TELEMOCA_ATTENTION_CONTROLS['max']))
                exec_fn = int(np.clip(np.random.normal(loc=TELEMOCA_EXECUTIVE_CONTROLS['loc'], scale=TELEMOCA_EXECUTIVE_CONTROLS['scale']), TELEMOCA_EXECUTIVE_CONTROLS['min'], TELEMOCA_EXECUTIVE_CONTROLS['max']))
                
            ori = int(np.clip(max(0, total - (dr + att + exec_fn)) * TELEMOCA_ORIENTATION_FRACTION, 0, 6))
            mis = int(np.clip((dr * TELEMOCA_MIS_MULTIPLIER) + np.random.choice(TELEMOCA_MIS_NOISE_MCI if status == 1 else TELEMOCA_MIS_NOISE_CONTROLS), 0, 15))
            
            rows.append({
                'Participant_ID': p_id, 'Clinical_Ground_Truth_MCI': status, 'Tele_MoCA_Total_Score': total,
                'MoCA_Subscore_Delayed_Recall': dr, 'MoCA_Subscore_Attention': att, 'MoCA_Subscore_Executive': exec_fn,
                'MoCA_Subscore_Orientation': ori, 'Memory_Impairment_Score_MIS': mis,
                'Session_Technical_Validity_Flag': np.random.choice([1, 0], p=[TELEMOCA_TECHNICAL_VALIDITY_RATE, 1 - TELEMOCA_TECHNICAL_VALIDITY_RATE])
            })
        return pd.DataFrame(rows)

    def generate_sensor_kit(self, weeks=SENSORKIT_N_WEEKS):
        """4. Tracks smartphone telemetry (keyboard hold/flight times and messaging volumes)."""
        rows = []
        for p_id in self.participant_ids:
            is_mci = self.mci_status_map[p_id]
            if is_mci:
                base_taps = np.random.normal(loc=SENSORKIT_TAPS_MCI['loc'], scale=SENSORKIT_TAPS_MCI['scale'])
                base_hold = np.random.normal(loc=SENSORKIT_HOLD_TIME_MCI['loc'], scale=SENSORKIT_HOLD_TIME_MCI['scale'])
                base_flight = np.random.normal(loc=SENSORKIT_FLIGHT_TIME_MCI['loc'], scale=SENSORKIT_FLIGHT_TIME_MCI['scale'])
                base_unlocks = np.random.normal(loc=SENSORKIT_UNLOCKS_MCI['loc'], scale=SENSORKIT_UNLOCKS_MCI['scale'])
            else:
                base_taps = np.random.normal(loc=SENSORKIT_TAPS_CONTROLS['loc'], scale=SENSORKIT_TAPS_CONTROLS['scale'])
                base_hold = np.random.normal(loc=SENSORKIT_HOLD_TIME_CONTROLS['loc'], scale=SENSORKIT_HOLD_TIME_CONTROLS['scale'])
                base_flight = np.random.normal(loc=SENSORKIT_FLIGHT_TIME_CONTROLS['loc'], scale=SENSORKIT_FLIGHT_TIME_CONTROLS['scale'])
                base_unlocks = np.random.normal(loc=SENSORKIT_UNLOCKS_CONTROLS['loc'], scale=SENSORKIT_UNLOCKS_CONTROLS['scale'])

            for wk in range(1, weeks + 1):
                taps_pm = np.clip(base_taps + np.random.normal(0, SENSORKIT_TAPS_NOISE), 50, 300)
                hold_t = np.clip(base_hold + np.random.normal(0, SENSORKIT_HOLD_TIME_NOISE), 40, 180)
                flight_t = np.clip(base_flight + np.random.normal(0, SENSORKIT_FLIGHT_TIME_NOISE), 100, 500)
                unlocks = int(np.clip(base_unlocks + np.random.normal(0, SENSORKIT_UNLOCKS_NOISE), 5, 120))
                msg_sent = int(np.clip((unlocks * SENSORKIT_MSG_MULTIPLIER) + np.random.normal(SENSORKIT_MSG_BASE, SENSORKIT_MSG_BASE_NOISE_MCI if is_mci else SENSORKIT_MSG_BASE_NOISE_CONTROLS), 0, 200))
                locs = int(np.clip(np.random.poisson(lam=SENSORKIT_LOCATIONS_LAMBDA_MCI if is_mci else SENSORKIT_LOCATIONS_LAMBDA_CONTROLS), 1, 50))

                rows.append({
                    'Participant_ID': p_id, 'MCI_Status': is_mci, 'Study_Week': wk, 'Keyboard_Taps_Per_Minute': round(taps_pm, 2),
                    'Keyboard_Key_Hold_Time_ms': round(hold_t, 2), 'Keyboard_Key_Flight_Time_ms': round(flight_t, 2),
                    'Daily_Screen_Unlocks_Avg': unlocks, 'Weekly_Text_Messages_Sent': msg_sent, 'Unique_Locations_Visited_Count': locs})
        return pd.DataFrame(rows)

    def generate_health_kit(self, days=HEALTHKIT_N_DAYS):
        """5. Tracks smartwatch biometric streaming (HRV, step trends, sleep layers, wear hours)."""
        rows = []
        for p_id in self.participant_ids:
            is_mci = self.mci_status_map[p_id]
            if is_mci:
                base_steps = np.random.normal(loc=HEALTHKIT_STEPS_MCI['loc'], scale=HEALTHKIT_STEPS_MCI['scale'])
                base_hrv = np.random.normal(loc=HEALTHKIT_HRV_MCI['loc'], scale=HEALTHKIT_HRV_MCI['scale'])
                base_deep = np.random.normal(loc=HEALTHKIT_DEEP_SLEEP_MCI['loc'], scale=HEALTHKIT_DEEP_SLEEP_MCI['scale'])
                base_wear = np.random.normal(loc=HEALTHKIT_WEAR_TIME_MCI['loc'], scale=HEALTHKIT_WEAR_TIME_MCI['scale'])
            else:
                base_steps = np.random.normal(loc=HEALTHKIT_STEPS_CONTROLS['loc'], scale=HEALTHKIT_STEPS_CONTROLS['scale'])
                base_hrv = np.random.normal(loc=HEALTHKIT_HRV_CONTROLS['loc'], scale=HEALTHKIT_HRV_CONTROLS['scale'])
                base_deep = np.random.normal(loc=HEALTHKIT_DEEP_SLEEP_CONTROLS['loc'], scale=HEALTHKIT_DEEP_SLEEP_CONTROLS['scale'])
                base_wear = np.random.normal(loc=HEALTHKIT_WEAR_TIME_CONTROLS['loc'], scale=HEALTHKIT_WEAR_TIME_CONTROLS['scale'])

            for dy in range(1, days + 1):
                steps = int(np.clip(base_steps + np.random.normal(0, HEALTHKIT_STEPS_NOISE), HEALTHKIT_STEPS_MIN, HEALTHKIT_STEPS_MAX))
                hrv = np.clip(base_hrv + np.random.normal(0, HEALTHKIT_HRV_NOISE), HEALTHKIT_HRV_MIN, HEALTHKIT_HRV_MAX)
                wear_t = np.clip(base_wear + np.random.normal(0, HEALTHKIT_WEAR_TIME_NOISE), 0.0, 24.0)

                if wear_t > HEALTHKIT_WEAR_TIME_THRESHOLD and np.random.rand() > (1 - HEALTHKIT_SLEEP_COLLECTION_RATE):
                    deep_s = int(np.clip(base_deep + np.random.normal(0, HEALTHKIT_DEEP_SLEEP_NOISE), 0, 180))
                    rem_s = int(np.clip((deep_s * HEALTHKIT_REM_MULTIPLIER) + np.random.normal(0, HEALTHKIT_REM_NOISE), 0, 200))
                    core_s = int(np.clip(HEALTHKIT_CORE_BASE + np.random.normal(0, HEALTHKIT_CORE_NOISE), 60, 500))
                else:
                    deep_s, rem_s, core_s = 0, 0, 0
                avg_hr = np.clip(np.random.normal(loc=HEALTHKIT_HR_MCI['loc'], scale=HEALTHKIT_HR_MCI['scale']) if is_mci else np.random.normal(loc=HEALTHKIT_HR_CONTROLS['loc'], scale=HEALTHKIT_HR_CONTROLS['scale']), HEALTHKIT_HR_MIN, HEALTHKIT_HR_MAX)
                rows.append({'Participant_ID': p_id, 'MCI_Status': is_mci, 'Study_Day': dy, 'Daily_Watch_Wear_Hours': round(wear_t, 1), 'Daily_Step_Count': steps, 'Mean_Heart_Rate_BPM': round(avg_hr, 1), 'Heart_Rate_Variability_HRV_ms': round(hrv, 2), 'Sleep_Stage_Core_Minutes': core_s, 'Sleep_Stage_REM_Minutes': rem_s, 'Sleep_Stage_Deep_Minutes': deep_s})
        return pd.DataFrame(rows)

    @staticmethod
    def generate_synthetic_data(seed=42):
        """Modular execution function wrapper.
        Returns a dictionary holding all 5 freshly initialized pandas dataframes."""
        generator = SyntheticDataGenerator(seed=seed)
        print("Initializing Data Pipeline Synthesis...")
        return {'baseline_classifier_data': generator.generate_baseline_dataset(),
                'cam_cog_burst_data': generator.generate_cam_cog_burst(),
                'tele_research_validation_data': generator.generate_tele_research(),
                'sensor_kit_data': generator.generate_sensor_kit(),
                'health_kit_data': generator.generate_health_kit()
                }