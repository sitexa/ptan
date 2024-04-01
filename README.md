
# PTAN

PTAN stands for PyTorch AgentNet -- reimplementation of
[AgentNet](https://github.com/yandexdataschool/AgentNet) library for
[PyTorch](http://pytorch.org/)

This library was used in ["Deep Reinforcement Learning Hands-On"](https://www.packtpub.com/data/deep-reinforcement-learning-hands-on-second-edition) book, here you can find [sample sources](https://github.com/PacktPublishing/Deep-Reinforcement-Learning-Hands-On).


## Code branches
The repository is forked from https://github.com/Shmuma/ptan .

The main work is to replace Gym with Gymnasium, upgrade torch version to meet the GPU upgrade to RTX4090。

## Installation

From sources:
```bash
pip install -e . 
```

From pypi:
```bash
pip install ptan
```

From github:
```bash
pip install pip install git+https://github.com/Shmuma/ptan.git 
```

## Requirements

* [PyTorch](http://pytorch.org/): version 2.2.1 is required
* [PyTorch Ignite](https://pytorch.org/ignite/): provides extra bindings for ignite
* [OpenAI Gym](https://gym.openai.com/): ```pip install gymnasium gymnasium[atari]```
* [Python OpenCV](https://pypi.org/project/opencv-python/): ```pip install opencv-python```
* [TensorBoardX](https://github.com/lanpa/tensorboardX): ```pip install tensorboardX```

### Note for [Anaconda Python](https://anaconda.org/anaconda/python) users

To run some of the samples, you will need these modules:
```bash
conda install pytorch torchvision -c pytorch
pip install tensorboard-pytorch
pip install gymnasium
pip install gym[atari]
pip install opencv-python
```

## Documentation

* [Ptan introduction](docs/intro.ipynb)

Random pieces of information

* `ExperienceSource` vs `ExperienceSourceFirstLast`: https://github.com/Shmuma/ptan/issues/17#issuecomment-489584115
