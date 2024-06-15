# Setup the environment

```bash
# using mamba speeds up the process
# install mamba using conda!
conda install mamba -n base -c conda-forge  
mamba env create -f environment.yml
conda activate rag-app

```

## pgVector 
A pre-baked docker image that has pgVector extension installed can be used for local development
```bash 
docker run --name pgvector-container -e POSTGRES_USER=langchain -e POSTGRES_PASSWORD=langchain -e POSTGRES_DB=langchain -p 6024:5432 -d pgvector/pgvector:pg16
```