FROM python:3.7

#USER Dronekit

WORKDIR /app

#RUN apk update && \
#    apk add --virtual build-deps gcc python-dev musl-dev 
RUN pip install dronekit-sitl -UI

EXPOSE 5760
EXPOSE 14550

ENTRYPOINT ["dronekit-sitl"]

CMD ["copter"] 