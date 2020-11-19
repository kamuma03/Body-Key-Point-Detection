FROM pytorch/pytorch:latest
WORKDIR /app

COPY server.py __main__.py
COPY model.py model.py
COPY utils.py  utils.py
COPY visualize_maskrcnn_predictions.py visualize_maskrcnn_predictions.py
RUN apt-get update ##[edited]
RUN apt-get install 'ffmpeg'\
    'libsm6'\ 
    'libxext6'  -y
RUN pip install flask
RUN pip install pillow
RUN pip install matplotlib
RUN pip install opencv-python
ENTRYPOINT [ "python3", "__main__.py" ]
EXPOSE 5000



# COPY . __main__.py
# # COPY . ./requirements.txt
# RUN pip install flask
# ENTRYPOINT python3 /app/__main__.py
# # ENTRYPOINT ["tail", "-f", clear"/dev/null"]
