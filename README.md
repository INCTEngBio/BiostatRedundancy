# Biome Redundancy Analysis & Statistical Validation
Authors: ELÍBIO LEOPOLDO RECH FILHO, DEBORAH BAMBIL, RAYANE NUNES LIMA, MARCO ANTÔNIO DE OLIVEIRA, PATRÍCIA VERDUGO PASCOAL, LUISA MAYUMI ARAKE DE TACCA

This Python script performs statistical analysis and visualization of genomic data (such as miRNAs) across Brazilian biomes, focusing on the impact of redundancy thresholds.

## 📊 Description

The code processes sequence abundance data across three categories:
* **Initial Copies**: Total raw copies per biome.
* **Exemplars**: Unique/representative sequences.
* **Retained (80% Threshold)**: Sequences remaining after the redundancy filter.

Beyond visualization, the script executes a **Chi-square ($\chi^2$) test of independence** to determine if the sequence retention rate is significantly dependent on the biome of origin.

## 🧬 Features

* **Statistical Analysis**: Automatic calculation of Chi-square and p-value using `scipy.stats`.
* **Scientific Visualization**: Grouped bar chart with automatic value annotations on each bar.
* **High-Quality Export**: Saves the plot in 300 DPI (`redundancy_threshold_with_stats.png`), suitable for scientific publications.

## 🛠️ Requirements

You will need the following Python libraries:

```bash
pip install matplotlib numpy scipy
