FROM agrigorev/zoomcamp-model:2025
# add your stuff here


#RUN apt-get update && apt-get install -y curl

#ADD https://astral.sh/uv/0.9.5/install.sh /uv-installer.sh
#RUN sh /uv-installer.sh 

#RUN curl -LsSf https://astral.sh/uv/install.sh | sh -s && mv /root/.local/bin/uv /usr/local/bin/uv

RUN pip install uv

WORKDIR /code

COPY ["pyproject.toml", "uv.lock", "./"]

RUN uv sync

COPY ["homework.py", "pipeline_v1.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["uv", "run", "uvicorn", "homework:app", "--host", "0.0.0.0", "--port", "9696"]
