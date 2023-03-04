
## Getting Started


### Installation (Environment setup)
Download anaconda following the instructions in the [official website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

Create an environment.

```bash
conda create -n minichatgpt python=3.8 # create an environment called 'minichatgpt' with Python version 3.8

conda activate minichatgpt # activate the environment
```

Install the following packages:

* `conda install numpy`

* `conda install pandas`

* [PyTorch](https://pytorch.org/) - select you based your preferences and hardware characteristics. Pick the GPU-supported installation.

* [Transformers](https://huggingface.co/docs/transformers/installation)

* [Hugginface Datasets](https://huggingface.co/docs/datasets/installation)

* [titoken](https://github.com/openai/tiktoken)

* `pip install tqdm`

* `pip install wandb`

* `conda install -c conda-forge notebook`

TBC

[//]: # (### Download Pre-trained models)

[//]: # (Download pre-trained models from [here]&#40;&#41; and put them under the `model_params` folder.)
