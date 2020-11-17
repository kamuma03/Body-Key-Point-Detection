FROM python:latest
WORKDIR /app

COPY server.py __main__.py
COPY model.py model.py
COPY utils.py .
RUN pip install flask
RUN pip install pillow
RUN conda install torchvision
#RUN pip install torch
ENTRYPOINT [ "python3", "__main__.py" ]



# COPY . __main__.py
# # COPY . ./requirements.txt
# RUN pip install flask
# ENTRYPOINT python3 /app/__main__.py
# # ENTRYPOINT ["tail", "-f", "/dev/null"]
