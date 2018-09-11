FROM python:3.6-alpine

LABEL maintainer="GaidarOS"


# Creating pwd
ENV INSTALL_PATH /
COPY ./requirements.txt ${INSTALL_PATH}/
WORKDIR ${INSTALL_PATH}

# Copy and install requirements for the app
RUN pip install -r requirements.txt
RUN rm requirements.txt && mkdir app
WORKDIR ${INSTALL_PATH}/app
EXPOSE 27346:27346
# Execute the program
CMD ["python", "app.py"]
