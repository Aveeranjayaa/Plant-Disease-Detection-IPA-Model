\# Dataset



\## Source



The project uses the PlantVillage dataset for plant leaf disease classification.



The original dataset contains images of healthy and diseased plant leaves across multiple plant and disease categories.



\## Selected Classes



For this project, four tomato leaf categories were selected:



1\. Healthy

2\. Tomato Early Blight

3\. Tomato Late Blight

4\. Tomato Leaf Mold



\## Dataset Preparation



A balanced subset was created for this project.



Approximately 500 images were selected from each class.



The selected images were divided into:



\- 80% training data

\- 10% validation data

\- 10% test data



This gives approximately:



| Split | Images |

|---|---:|

| Training | 1600 |

| Validation | 200 |

| Testing | 200 |

| Total | 2000 |



The images are not stored in the Git repository to keep the repository lightweight.



The `scripts/prepare\_dataset.py` script contains the procedure used to create the processed dataset from the original PlantVillage images.



\## Image Type



The color images are used for model training because color information can be useful for identifying visible symptoms such as discoloration and lesions.



\## Reproducibility



To reproduce the processed dataset, place the original PlantVillage dataset in the expected source directory and run:



```text

python scripts/prepare\_dataset.py

```

