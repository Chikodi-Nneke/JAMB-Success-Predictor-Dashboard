# JAMB Success Predictor Dashboard

## Project Overview

This repository contains a comprehensive Power BI dashboard and accompanying Python data preparation scripts, designed to analyse the profound impact of key student background factors (such as socioeconomic status, parental education, attendance, and study time) on overall student performance in the JAMB examination. This projects aims to identify key student background factors (such as socioeconomic status, parental education, attendance, and study time) that most strongly influence JAMB exam success.


## Goal

Students often face significant challenges in achieving optimal performance in the JAMB examination, impacting their educational progression and future opportunities. This project was proposed to provide a clear, data-driven understanding of the underlying student background factors influencing JAMB performance. Consequently, it empowers education policymakers and school administrators to make data-driven decisions and craft targeted interventions that significantly improve student outcomes and enhance overall school performance. Ultimately, this robust tool champions the use of data-driven strategies to optimize resource allocation and foster superior educational achievements for all students.


## Features

- Interactive Power BI Dashboard: Features dynamic filters by gender, school location, and school type allowing for granular analysis.
- Python Data Preparation Scripts: Python scripts for data transformation and predictive modeliing of performance data.
- Custom DAX Measures: Utilizes custom DAX measures within Power BI to calculate key performance indicators, such as the percentage of students meeting specific score thresholds and top performing student groups.


## Data

The analysis utilises a comprehensive dataset sourced from Kaggle for tudent perfromance in JAM 2024, comprising 17 columns of student performance and background information.

Key fields include: Gender, Age, JAMB Scores, Socioeconomic Status, Parental Education Level, Attendance Rate, and Weekly Study Hours. All sensitive data has been anonymized to ensure privacy.


## Usage 

- Use Power Query to clean and prepare raw CSV data files in the /data folder.
- Open JAMB_Success_Predictor_Dashboard.pbix in Power BI Desktop.
- Use the dashboard slicers to filter by gender, school location, and school type.


## Results and Insights

- Parental Education Correlates with Student Performance: The analysis shows that students with parents who have tertiary education or some form of education consistently score higher than those whose parents do not have any form of education. This supports the idea of intergenerational influence on academic outcomes.
- Attendance Rate and Study Hours Positively Correlate with Scores: The scatter plot and line chart illustrate strong upward trends and a positive correlation between study hours and attendance. Based on these results, it appears that even a small increase in attendance and study hours can significantly improve scores, which is consistent with the "What If?" scenario tool.
- Student performance by socioeconomic group shows a big gap, with students from higher socioeconomic backgrounds outperforming those from lower backgrounds, reinforcing the need for targeted support.


## Recommendations

- Promote and facilitate effective weekly study hours by implementing structured study sessions, offer workshops on effective study techniques and time management, and ensure access to conducive learning environments.
- Prioritize and incentivize consistent student attendance by launching targeted campaigns or incentive programs to raise attendance rates, particularly among low-SES and underperforming groups.
- Strengthen parental education support initiatives by developing accessible workshops for parents focusing on academic support strategies, resource provision, and fostering educational aspirations at home.
- Develop data-driven, holistic intervention strategies that continuously monitor trends, identify at-risk students, and tailor interventions that address not only academic gaps but also attendance habits, home-based support, and effective study practices.


## Contact & Support

For questions or collaboration, please contact Chikodinaka Nneke at chikodinneke@gmail.com or open an issue on this repo.


## References & Resources

- [Power BI Report](https://app.powerbi.com/view?r=eyJrIjoiMDliMDk2NjQtY2UyZS00N2U1LWExZjItNWY1Y2NjMzU2NDNiIiwidCI6IjU5NGFiMDZmLTFiZTQtNGIwMi1iZjU4LTIyY2ZmZTljMmExMSJ9)
- [Data Source](https://www.kaggle.com/datasets/idowuadamo/students-performance-in-2024-jamb)
