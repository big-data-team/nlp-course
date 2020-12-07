# nlp-course

Natural Language Processing (NLP) course materials

See also Machine Learning course:
- https://bigdatateam.org/ml-course

# Environment Configuration

1. Download [requirements.txt](requirements.txt)
2. Create environment:
```bash
export env_name="bdt-nlp-course"
conda create -n $env_name python=3.7
conda activate $env_name
conda install --file requirements.txt
```

See available conda environments with the help of:
```bash
conda info --envs
```

If you need to remove environment use the following command:
```bash
conda remove --name $env_name --all
```
