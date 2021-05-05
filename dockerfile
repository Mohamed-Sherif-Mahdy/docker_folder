#base image
FROM python
COPY . /docker_folder
WORKDIR /docker_folder
RUN pip3 install newspaper3k
CMD python common_words.py