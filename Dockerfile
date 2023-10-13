FROM python:3.9.0

ENV PYTHONUNBUFFERED True

RUN python -m pip install --upgrade pip

# Copy local code to the container image.
ENV APP_HOME .
WORKDIR $APP_HOME
COPY . .
RUN pip install -r requirements.txt

CMD exec flask run -h 0.0.0.0