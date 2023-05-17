# CSE 676 Deep Learning Project
# Side View Face Recognition using various Deep Learning techniques

Project for CSE 676 Deep Learning (Spring 2023)

## Contributions:

Jason DCosta | 50468245 | jasondco@bufflo.edu

Dhvani Mitesh Kothari | 50485387 | dhvanimi@buffalo.edu

## Structure:

├── cycleGAN/

├── pix2pix/

├── utils/

├── README.md

├── requirements.yml

└── .gitignore

The project is comprised of  2 main DL techniques: pix2pix and cycleGAN, the code is in their respective folders. 

utils has some driver code we used for manipulation of data. This code may not run as is, since the paths for data manipulation have changed during development.

Our pix2pix implementation was based on a tensorflow [tutorial](https://www.tensorflow.org/tutorials/generative/pix2pix).

Our cycleGAN implementation was based on this pytorch [implementation](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix).

## Installation:

### pix2pix

This was run in a Google Colab notebook with GPU acceleration. Any libraries used are in the code itself.

### cycleGAN

This was run on a PC running Windows 10 with a Nvidia RTX 3060 GPU. We use conda for managing libraries.

```bash
conda env create -f requirements.yml
```

The file 'cycleGAN\face_recog.ipynb' was run in a Google Colab notebook. Any software installed is part of the code itself.

## Usage:

### pix2pix

First upload the 'pix2pix\faces.zip' file to the Colab session storage and then run the notebook.

### cycleGAN


To train the model, run the following:
```bash
python train.py --dataroot faces --name faces --model cycle_gan --n_epochs 12 --n_epochs_decay 12
```

To test the model, run the following:
```bash
python test.py --dataroot faces --name faces --model cycle_gan --num_test 100
```

To test face recognition, upload the files 'input_dir.zip' and 'output_dir.zip' to the Colab session storage and then run the notebook 'cycleGAN\face_recog.ipynb'