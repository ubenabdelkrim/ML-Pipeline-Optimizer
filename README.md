# Intelligent Optimization of Distributed Pipeline Execution in Serverless Platforms: A Predictive Model Approach

This repository contains the code and resources associated with the paper **"Intelligent Optimization of Distributed Pipeline Execution in Serverless Platforms: A Predictive Model Approach"** presented at the **10th International Workshop on Serverless Computing (WoSC10 '24)**. The paper focuses on optimizing the execution of distributed data pipelines in serverless environments by using a predictive model based on **XGBoost**.

## Abstract

The research addresses one of the biggest challenges in cloud computing: optimizing the execution time and cost of distributed pipelines in serverless environments. We propose a predictive approach to optimize the execution of data analytics pipelines in serverless platforms such as **AWS Lambda** using the **Lithops** framework. The model predicts the optimal configurations for pipeline execution, achieving significant reductions in execution time and operational costs.

## Key Contributions

- **XGBoost-based predictive model**: We trained a machine learning model using XGBoost to predict the execution time and optimize parameters such as memory allocation, vCPUs, and the number of splits for parallel processing.
- **Cost and time optimization**: The approach resulted in a **79.9% reduction in execution time** and **30% cost savings** compared to traditional methods like **Design Space Analysis (DSA)**.
- **Geospatial water consumption case study**: We applied the model to a case study of geospatial water consumption data, showing how it can be used to optimize real-world data analytics pipelines.

## Methodology

In the paper, we propose a solution that leverages **machine learning** to predict pipeline execution time and optimize parameters that minimize both execution time and cost. The model was trained on data collected from 148 pipeline executions in **Lithops**, and hyperparameters were optimized using the **Optuna** framework. The model predicts optimal configurations without the need for exhaustive testing, providing a more efficient and cost-effective alternative to **Design Space Analysis (DSA)**.

## Results

The **XGBoost model** achieved:
- **79.9% reduction in execution time** compared to suboptimal configurations.
- **30% cost savings** compared to exhaustive testing methods (Design Space Analysis).
- Significant improvements in execution efficiency for serverless pipelines, particularly when dealing with large datasets or complex data processing tasks.

## Research Impact

This work demonstrates the potential of machine learning to optimize distributed pipeline execution in serverless environments, highlighting its ability to:
- Reduce time and costs significantly compared to traditional optimization methods.
- Be applied across various serverless platforms (AWS Lambda, Google Cloud Functions, Azure Functions).
- Provide a scalable solution for data-intensive applications in cloud computing.

## Paper Access

The full paper is available in the **ACM Digital Library**:  
[Read the paper here](https://doi.org/10.1145/3702634.3702951)

## Acknowledgements

This work has been partially funded by the **CLOUDLESS project**, a platform for edge computing information, under the **UNICO I+D CLOUD 2022 subproject**, which is financed by the **Ministry of Economic Affairs and Digital Transformation** and the **European Union - NextGenerationEU**.

Additionally, this work has been supported by the **European Union** through the **Horizon Europe CloudSkin project** (101092646).

We would also like to express our gratitude to the reviewers for their invaluable feedback, which greatly enhanced the quality of this work.

## Contact

For any questions or further details, feel free to contact me at **usama.benabdelkrim@urv.cat**.

---

**Keywords**: Serverless Computing, Distributed Pipelines, Machine Learning, XGBoost, Cloud Computing, Resource Optimization, Cost Efficiency, Geospatial Analysis
