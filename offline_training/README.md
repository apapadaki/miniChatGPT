
## Getting Started


### Installation (Environment setup)
Download anaconda following the instructions in the [official website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

Create an environment.

```bash
conda env create -f environment.yml #this should be executed in the `offline_training` directory

conda activate offline_training # activate the environment
```

[//]: # (Install the following packages:)


[//]: # (* [PyTorch]&#40;https://pytorch.org/&#41; - select you based your preferences and hardware characteristics. Pick the GPU-supported installation.)

[//]: # ()
[//]: # (* [Transformers]&#40;https://huggingface.co/docs/transformers/installation&#41;)

[//]: # ()
[//]: # (* [Hugginface Datasets]&#40;https://huggingface.co/docs/datasets/installation&#41;)

[//]: # ()
[//]: # (* [titoken]&#40;https://github.com/openai/tiktoken&#41;)

### Pre-process dataset
```bash
conda activate offline_training # run this command if environment is not already activated

jupyter notebook # start notebook server
```
Select `notebooks\{dataset}_data_preprocessing.ipynb` notebook, where `dataset` is one of the supported datasets, and run all cells.


[//]: # (### Download Pre-trained models)

[//]: # (Download pre-trained models from [here]&#40;&#41; and put them under the `model_params` folder.)
