from flask import Flask, render_template, send_from_directory, abort, jsonify
import os
import time

app = Flask(__name__, static_folder="static", template_folder="templates")

START_TIME = time.time()
VERSION = "v1.0.0"
SLO_TARGET = "99.9% availability (30-day window)"


def _resume_filename():
    """
    Prefer bb-cloudres.pdf, but fall back to resume.pdf if that's what exists.
    """
    candidates = ["bb-cloudres.pdf", "resume.pdf"]
    static_dir = os.path.join(app.root_path, "static")
    for f in candidates:
        if os.path.exists(os.path.join(static_dir, f)):
            return f
    return None


@app.route("/")
def home():
    resume_file = _resume_filename()
    return render_template(
        "index.html",
        github_url="https://github.com/BryceBedford",
        resume_file=resume_file,
        health_url="/healthz",
        metrics_url="/metrics",
        version=VERSION,
        slo_target=SLO_TARGET
    )


@app.route("/download")
def download_resume():
    resume_file = _resume_filename()
    if not resume_file:
        abort(404, description="Resume file not found in /static (expected bb-cloudres.pdf or resume.pdf).")
    return send_from_directory(
        directory=os.path.join(app.root_path, "static"),
        path=resume_file,
        as_attachment=True,
        download_name=resume_file
    )


@app.route("/healthz")
def healthz():
    return jsonify(status="ok"), 200


@app.route("/metrics")
def metrics():
    uptime_seconds = int(time.time() - START_TIME)
    return jsonify(
        status="healthy",
        uptime_seconds=uptime_seconds,
        slo_target=SLO_TARGET,
        version=VERSION
    ), 200


if __name__ == "__main__":
    # Local debugging only; production should run via gunicorn behind nginx/systemd
    app.run(host="0.0.0.0", port=5000)
@app.route("/healthz")
def healthz():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    # Local debugging only; production runs via gunicorn/nginx
    app.run(host="0.0.0.0", port=5000)
