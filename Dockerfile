FROM python:3.11 as init

ARG API_URL


WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt
RUN reflex init
CMD reflex run --env prod --backend-only