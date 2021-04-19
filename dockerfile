FROM ubuntu
RUN apt update && apt install python3 -y
COPY sp5.py .
CMD python3 sp5.py
