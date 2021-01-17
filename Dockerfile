# Add a line here to specify the docker image to inherit from.
#FROM registry.aisingapore.net/aiap/polyaxon/pytorch-tf2-cpu:latest
FROM tensorflow/tensorflow
MAINTAINER MengyongLee meng_yong_lee@aiap.sg

# # default
ARG WORK_DIR="/home/polyaxon"
ARG USER="polyaxon"

WORKDIR $WORK_DIR

# # Add lines here to copy over your src folder and
# # any other files you need in the image (like the saved model).

COPY src src
COPY conda.yml .
COPY tensorfood.h5 src

# # Add a line here to update the base conda environment using the conda.yml.
# COPY build/conda.yml .

# RUN conda env update -f conda.yml -n base && \
#     rm conda.yml && \
#     chown -R 1000450000:0 $WORK_DIR

# # DO NOT remove the following line - it is required for deployment on Tekong

USER $USER

EXPOSE 8000

# Add a line here to run your app
ENTRYPOINT python -m src.app