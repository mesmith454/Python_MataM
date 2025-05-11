# pull python image, currently working with 3.13.3
FROM python:3.13.3

# copy requirements file to image
COPY ./requirements.txt /python_app/requirements.txt

# switch working directory
WORKDIR /python_app

# install dependencies and packages specified in requirements
RUN pip install -r requirements.txt

# copy all content from local file to image
COPY . /python_app

#Config container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD [ "About.py" ]


