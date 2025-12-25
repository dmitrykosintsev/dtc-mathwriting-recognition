# Handwritten math recognition using CNN
This project aims at creating a simple solution to transform written math formulae into LaTex expressions.

## Problem description
Writing formulae in mathematics using LaTex can be cumbersome. An old pen-and-paper approach or modern devices with touchscreen and digital pens can save a lot of time. However, such writings are usually not appropriate for research papers or academic work, as the readability depends a lot on how neat one's writing is. This application built using a convolutional neural network aims to bridge the gap and make it easier to digitalise any handwritten notes in mathematics.

## Data and EDA insights

### Dataset
```bibtex
@misc{gervais2025mathwritingdatasethandwrittenmathematical,
      title={MathWriting: A Dataset For Handwritten Mathematical Expression Recognition}, 
      author={Philippe Gervais and Anastasiia Fadeeva and Andrii Maksai},
      eprint={2404.10690},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2404.10690}, 
}
```
[Dataset on HuggingFace](https://huggingface.co/datasets/deepcopy/MathWriting-human)

## Model training

### CNN-based Image Recognition

### Tokenization into LaTeX

### Training

### Output

### Challenges

## Notebook to script

## How to reproduce
Explicitly installed packages:
* huggingface_hub
* jupyter notebook
* pandas
* fastparquet
* numpy
* pillow

1. Clone the repository:
```bash
git clone 
```
2. Install huggingface_hub:
```bash
pip install huggingface_hub
```
3. To get data, run the following command in the root folder of the cloned project:
```bash
python get_dataset.py
```
A new folder named **data** will be created. It contains the dataset split into train, test and validation sets.

## Model deployment
### Dependencies

### Containerization

### Cloud deployment
