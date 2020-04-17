
# FluSense-data

[AudioSet](https://research.google.com/audioset/) data (originally released by Google) labeled for the FluSense project (https://dl.acm.org/doi/10.1145/3381014).

This repository only contains annotations for the audio files. To download the original audio dataset, please use the following link: [Google Drive](https://drive.google.com/drive/folders/1c-qkb_ljD6xXqU4AGm4jEf8-lygRjLtS?usp=sharing)

The TextGrid (output format of ["praat"](http://www.fon.hum.uva.nl/praat/) annotation tool) annotation files are under flusense_data folder. There is a python example that can be used for getting duration statistics for each label in the dataset using ["praatIO"](https://pypi.org/project/praatio/) package. However, many other packages can achieve the same goal.

# Labels

The avialable labels are:

1. cough
2. sneeze
3. sniffle
4. throat-clearing
5. speech
6. etc (i.e everything else)

There are also some other events that were labeled, but their total duration in the dataset is very small.

# Citation
If you find our work useful please cite our work at: 

    @article{10.1145/3381014,
    author = {Al Hossain, Forsad and Lover, Andrew A. and Corey, George A. and Reich, Nicholas G. and Rahman, Tauhidur},
    title = {FluSense: A Contactless Syndromic Surveillance Platform for Influenza-Like Illness in Hospital Waiting Areas},
    year = {2020},
    issue_date = {March 2020},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {4},
    number = {1},
    url = {https://doi.org/10.1145/3381014},
    doi = {10.1145/3381014},
    journal = {Proc. ACM Interact. Mob. Wearable Ubiquitous Technol.},
    month = mar,
    articleno = {Article 1},
    numpages = {28},
    keywords = {Contactless Sensing, Crowd Behavior Mining, Edge Computing, Influenza Surveillance}
    }


