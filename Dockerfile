FROM python:2.7

#USER Dronekit

WORKDIR /app

#RUN apk update && \
#    apk add --virtual build-deps gcc python-dev musl-dev 
RUN pip install dronekit-sitl -UI

EXPOSE 5760
EXPOSE 5762
EXPOSE 5763
EXPOSE 14550

ENTRYPOINT ["dronekit-sitl"]
CMD ["copter","--home=41.879427,-87.630797,0,0"] 