# Acoustic Shadow Effect

## Overview
This project is an exploratory experimental study of the **acoustic shadow effect**, investigating how different everyday materials attenuate sound when placed between a sound source and a receiver. The goal is not to produce a finalized acoustic model, but to demonstrate experimental reasoning, signal analysis, and honest treatment of limited data.

---

## Research Question
**Do different common materials produce measurably different acoustic attenuation under identical geometric and recording conditions?**

The study focuses on **relative attenuation** rather than absolute SPL values, using an unobstructed (direct) sound path as the reference.

---

## Experimental Setup & Data Collection
- A controlled sound source and fixed microphone position were used.
- Sound was recorded in two configurations:
  - **Direct path** (no obstruction)
  - **Obstructed path** with one material placed between source and microphone
- Materials tested:
  - Cardboard
  - Plastic
  - Cotton
- Recordings were made using **Audacity** and exported for analysis.
- Broadband Sound Pressure Level (SPL) values were extracted from the recordings.

The raw audio project file (`.aup3`) and processed SPL data (`.csv`) are included for transparency and reproducibility.

---

## Data Analysis
The analysis focuses on attenuation relative to the direct (unobstructed) case, defined as:

Attenuation is defined as:

ΔSPL = SPL_material − SPL_direct


This approach isolates the acoustic shadowing contribution of each material.

### Scripts
- `analysis/analyze_data.py`  
  Loads SPL data and performs basic inspection and preprocessing.
- `analysis/relative_attenuation.py`  
  Computes attenuation relative to the direct case and generates comparative visualizations.

---

## Results
The materials exhibit different levels of attenuation, consistent with qualitative expectations based on their acoustic properties:
- Cotton shows higher attenuation, consistent with porous absorption.
- Cardboard and plastic show comparatively lower attenuation, consistent with partial reflection and transmission.

Final plots and figures are compiled in:
- `results/Acoustic_Shadow_Effect.pdf`

---

## Limitations
This study is intentionally limited in scope and should be interpreted as a **pilot experiment**.

Key limitations include:
- Single thickness per material
- No frequency-resolved analysis (broadband SPL only)
- Single trial per material (no statistical uncertainty estimates)
- Fixed geometry and angle of incidence

These constraints were imposed by time and equipment availability and are explicitly acknowledged to avoid overinterpretation.

---

## Future Work
Possible extensions include:
- Studying attenuation as a function of material thickness
- Frequency-dependent analysis using FFT-based methods
- Multiple trials with uncertainty estimation
- Comparing experimental results with simple acoustic models

---

## Tools & Dependencies
- Python  
- pandas  
- matplotlib  
- Audacity (for audio recording and preprocessing)

---

## Project Status
Completed as a **demonstration and portfolio project** showcasing experimental acoustics, data analysis, and scientific reasoning.
