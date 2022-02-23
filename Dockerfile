FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/medusa_light
WORKDIR /usr/src/medusa_light
RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip install -r /usr/src/medusa_light/requirements.txt && \
    mkdir -p /vol/web/static && \
    adduser --disabled-password --no-create-home app_user && \
    chown -R app_user:app_user /vol && \
    chmod -R 755 /vol/web && \
    chmod -R +x /usr/src/medusa_light/scripts && \

ENV PATH="/usr/src/medusa_light/scripts:${PATH}"

USER app_user

CMD ["entrypoint.sh"]



