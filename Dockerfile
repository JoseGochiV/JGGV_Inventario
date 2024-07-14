FROM python:3.9-slim-bullseye

WORKDIR /inventario

COPY requerirements.txt requerirements.txt

RUN pip install --no-cache-dir -r requerirements.txt

COPY . .

EXPOSE 5000

CMD [ "python",  "/inventario/run.py"]
