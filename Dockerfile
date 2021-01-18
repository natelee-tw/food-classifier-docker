FROM continuumio/miniconda3
MAINTAINER MengyongLee meng_yong_lee@aiap.sg

WORKDIR /app

COPY conda.yml .

RUN conda env update -f conda.yml -n base

COPY src/. .
COPY tensorfood.h5 .
COPY tensorfood.json .


#ENTRYPOINT ["conda", "run", "-n", "food-classifier", "python", "app.py"]
ENTRYPOINT python app.py