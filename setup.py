"""
PTAN stands for PyTorch AgentNet -- reimplementation of AgentNet library for pytorch
"""
import setuptools


requirements = ['torch', 'gymnasium', 'atari-py', 'numpy', 'opencv-python']


setuptools.setup(
    name="ptan",
    author="PPeng",
    author_email="sitexa@gmail.com",
    license='GPL-v3',
    description="PyTorch reinforcement learning framework",
    version="0.8",
    packages=setuptools.find_packages(),
    install_requires=requirements,
)
