FROM python:latest
ADD main.py Game369.py MemberList.py TailCatcher.py /home/discord/
RUN pip install -U discord.py \
    && rm -rf /var/lib/apt/lists/*
CMD ["python3", "/home/discord/main.py"]