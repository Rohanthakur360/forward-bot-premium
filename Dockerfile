FROM python:3.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN Rohanthakur360/forward_bot_premium_ultra
WORKDIR /forward_bot_premium_ultra
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"] 






# Stubborn Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Stubborn1223
