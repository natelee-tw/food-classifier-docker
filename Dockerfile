FROM continuumio/miniconda3
MAINTAINER MengyongLee meng_yong_lee@aiap.sg

WORKDIR /app

COPY conda.yml .
RUN conda env create -f conda.yml

RUN conda env update -f conda.yml -n base
#SHELL ["conda", "run", "-n", "food-classifier", "/bin/bash", "-c"]

#RUN conda env update -f conda.yml -n base

COPY src/. .
COPY tensorfood.h5 .
COPY tensorfood.json .

EXPOSE 5000

RUN echo "Making sure flask is installed..."
RUN python -c "import flask"

#ENTRYPOINT ["python"]
ENTRYPOINT ["python", "app.py"]