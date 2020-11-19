# latest pytorch image from docker hub
FROM pytorch/pytorch:latest
WORKDIR /app                    

# first copying all the files from the local to the docker image
COPY server.py __main__.py
COPY model.py model.py
COPY utils.py  utils.py
COPY visualize_maskrcnn_predictions.py visualize_maskrcnn_predictions.py

# running the commands to install all the dependies 
RUN apt-get update ##[edited]
RUN apt-get install 'ffmpeg'\
    'libsm6'\ 
    'libxext6'  -y
RUN pip install flask
RUN pip install pillow
RUN pip install matplotlib
RUN pip install opencv-python

# Entry point of the image  and the port to be exposed
ENTRYPOINT [ "python3", "__main__.py" ]
EXPOSE 5000


# to create the image : docker build --tag keypoint .
# to run the docker image : docker run --publish 5000:5000 --name keypoint --detach --rm keypoint
# to clear the docker images :  docker system prune