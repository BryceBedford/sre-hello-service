FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# fail the build if deps didn't install
RUN python -c "import flask, gunicorn; print('deps ok:', flask.__version__, gunicorn.__version__)"

COPY . /app

ENV PORT=5000
EXPOSE 5000

CMD ["python", "-m", "gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"
