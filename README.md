# Exploration on Generalization of Fairness Interventions

The following project explores how fairness intervention applied on classifiers, hold under on dataset/demographic split and how does it hold up when the data distribution shifts.

The motivation is that fairness interventions are often evalauted on fixed dataset split. In context of real world scenarios, it is important to consider how the model input shifts, such as demographic changes, distribution change, impact these interventions. This will provide implications for responsible AI deployment.

# Fairness Metrics
Demographic Parity, Equalized Odds, Equal Opportunity, Individual Fairness

# Interventions 
- Pre-processing: Reweighing (AIF360)
- In-processing: Fairness constraints (Fairlearn)
- Post-processing: Threshold optimization (Fairlearn)


