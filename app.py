from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

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
        resume_file=resume_file
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
    return {"status": "ok"}, 200

if __name__ == "__main__":
    # Local debugging only; production runs via gunicorn/nginx
    app.run(host="0.0.0.0", port=5000)
