FROM python:3.10

ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"

ENV SPARK_HOME="/opt/spark" \
    SPARK_VERSION="3.2.1" \
    HADOOP_VERSION="2.7" \
    PYSPARK_PYTHON=python

ENV POETRY_VERSION="1.1.12" \
    POETRY_VIRTUALENVS_CREATE=false

ENV PATH="$SPARK_HOME/bin:$PATH"
ENV PATH="$SPARK_HOME/python:$PATH"
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /opt

# 👇 Java
RUN echo "deb http://ftp.us.debian.org/debian sid main" >> /etc/apt/sources.list
RUN apt-get update && apt-get -y install gcc-10-base openjdk-11-jdk && apt-get -y autoremove

# 👇 Spark
ADD "https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz" .
RUN tar -xzf spark*.tgz && rm -f spark*.tgz && mv spark* spark

# 👇 Poetry
RUN apt-get update \
    && apt-get install -y build-essential python3-dev python3-setuptools curl \
    && pip install --upgrade --no-cache-dir pip \
    && curl -sSL https://install.python-poetry.org | python - --version "$POETRY_VERSION"

# 👇 Adding Files
COPY *.lock .
COPY *.toml .

# 👇 Installing project dependencies
RUN poetry install --no-dev

CMD tail -f /dev/null
