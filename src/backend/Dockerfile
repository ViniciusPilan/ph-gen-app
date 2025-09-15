FROM python:3.12-alpine

WORKDIR "/home/ph-gen-app"

ADD "requirements.txt" "/home/ph-gen-app/requirements.txt"

RUN pip3 install --no-cache-dir -r /home/ph-gen-app/requirements.txt

ADD "api/" "/home/ph-gen-app"

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000", "--reload"]
