FROM python:latest
WORKDIR /home/discord/
ADD main.py Game369.py MemberList.py TailCatcher.py /home/discord/
COPY DB/ DB/
COPY Files/ Files/
COPY Setting/ Setting/
RUN pip install -U discord.py \
    && rm -rf /var/lib/apt/lists/*
CMD ["python3", "/home/discord/main.py"]