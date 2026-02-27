from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

# --- Helper: choose whichever resume file exists in /static ---
def _resume_filename():
    # Prefer your real name first
    candidates = ["bb-cloudres.pdf", "resume.pdf"]
    import os
    for f in candidates:
        if os.path.exists(os.path.join(app.static_folder, f)):
            return f
    # fallback (still returns something so you see a helpful error)
    return "bb-cloudres.pdf"

@app.route("/download")
def download_resume():
    filename = _resume_filename()
    return send_from_directory(
        directory=app.static_folder,
        path=filename,
        as_attachment=True,
        download_name=filename,
    )

@app.route("/")
def home():
    resume_file = _resume_filename()
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Bryce Bedford | Cloud & DevOps Engineer</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 980px; margin: auto; padding: 40px; line-height: 1.6; }}
    h1 {{ margin-bottom: 0; }}
    .sub {{ margin-top: 6px; color: #444; }}
    .topbar {{ display:flex; flex-wrap:wrap; align-items:center; gap:14px; margin: 18px 0 28px; }}
    .btn {{
      display:inline-block; padding: 10px 14px; border: 1px solid #111;
      text-decoration:none; border-radius: 10px; color:#111; font-weight:600;
    }}
    .btn:hover {{ opacity: 0.85; }}
    .pill {{ display:inline-block; padding: 6px 10px; border: 1px solid #ccc; border-radius: 999px; font-size: 13px; }}
    h2 {{ margin-top: 34px; border-top: 1px solid #eee; padding-top: 22px; }}
    ul {{ margin-top: 10px; }}
    li {{ margin: 6px 0; }}
    .role {{ font-weight: 700; }}
    .meta {{ color:#444; font-size: 14px; }}
    .grid {{ display:grid; grid-template-columns: 1fr; gap: 10px; }}
    @media (min-width: 800px) {{
      .grid {{ grid-template-columns: 1fr 1fr; }}
    }}
    code {{ background: #f6f6f6; padding: 2px 6px; border-radius: 6px; }}
  </style>
</head>
<body>

  <h1>Bryce Bedford</h1>
  <div class="sub"><strong>AWS Cloud Engineer / Cloud & DevOps-Focused Engineer</strong> • US</div>

  <div class="topbar">
    <span class="pill">brycebedford22@gmail.com</span>
    <a class="pill" href="https://linkedin.com/in/bryceebedford" target="_blank" rel="noreferrer">linkedin.com/in/bryceebedford</a>
    <span class="pill">804.301.9628</span>
    <a class="btn" href="/download">Download Resume</a>
    <span class="meta">Serving: <code>/static/{resume_file}</code></span>
  </div>

  <h2>Professional Summary</h2>
  <p>
    Cloud and DevOps-focused technical product and systems professional with experience supporting federal,
    fintech, and enterprise platforms across AWS, Azure, and secure cloud environments. Experienced deploying
    and maintaining cloud infrastructure, supporting automation-first DevOps workflows, and managing identity,
    security, and system reliability across regulated environments. Strong background in Agile delivery,
    scripting, and technical documentation supporting federal and commercial digital transformation initiatives.
  </p>

  <h2>Experience</h2>

  <div class="role">Digital Product Manager</div>
  <div class="meta">AON • Remote • Jan 2023 – Present</div>
  <ul>
    <li>Supported cloud-hosted enterprise payment and insurance platforms across AWS/Azure, improving reliability, secure integrations, and monitoring for 500K+ users.</li>
    <li>Partnered with engineering on compute assets, identity integrations (SSO/SAML), and cloud APIs supporting secure authentication and transactions.</li>
    <li>Automated operational workflows using scripting and infrastructure configuration practices, reducing manual provisioning effort by ~35%.</li>
    <li>Maintained release notes, system documentation, and technical requirements supporting cloud deployments and infrastructure updates.</li>
  </ul>

  <div class="role">Product Manager</div>
  <div class="meta">FRINGE • Remote • Apr 2022 – Jan 2023</div>
  <ul>
    <li>Partnered with engineering to support deployment/scaling of a cloud-native HRIS & payments platform hosted in AWS.</li>
    <li>Owned technical requirements and documentation for API integrations with payroll/benefits/financial partners, reducing manual processing by ~30%.</li>
    <li>Collaborated with DevOps/engineering to improve release processes and environment configuration automation, reducing defects and deployment delays.</li>
    <li>Acted as liaison across product/engineering/external partners to troubleshoot issues and ensure stable operation of cloud applications.</li>
  </ul>

  <div class="role">Senior Consultant</div>
  <div class="meta">Protiviti • Washington, DC • Aug 2020 – Aug 2022</div>
  <ul>
    <li>Supported federal/financial clients with cloud readiness, compliance, and infrastructure modernization across AWS and hybrid environments.</li>
    <li>Assisted with system configuration, process automation, and technical documentation aligned to SOC2/NIST and federal standards.</li>
    <li>Performed requirements analysis, system mapping, and technical writing for transformation initiatives impacting cloud and enterprise systems.</li>
    <li>Partnered with security teams on IAM, system hardening, and risk mitigation for regulated environments.</li>
  </ul>

  <h2>Education</h2>
  <ul>
    <li><strong>Ph.D., Economics</strong> — Howard University (In Progress)</li>
    <li><strong>M.A., Communications & Media Management</strong> — Virginia State University</li>
    <li><strong>B.A., Economics</strong> — Old Dominion University</li>
  </ul>

  <h2>Certifications</h2>
  <ul>
    <li>Certified ScrumMaster (CSM)</li>
    <li>Certified Scrum Product Owner (CSPO)</li>
    <li>ITIL 4 Foundation</li>
    <li>CompTIA Security+</li>
    <li>AWS Certified Solutions Architect – Associate (In Progress)</li>
  </ul>

  <h2>Core Metrics</h2>
  <ul>
    <li>$300M projected annual payment volume enabled through cloud-based platform modernization</li>
    <li>Supported infrastructure and product delivery across 119+ integrated product environments</li>
    <li>Improved deployment/release velocity by 30%+ through workflow and automation improvements</li>
    <li>Led roadmap and solution design for platforms supporting 500K+ end users</li>
    <li>Delivered cloud and architecture recommendations across multiple enterprise consulting engagements</li>
  </ul>

  <h2>Projects (Relevant DevOps / SRE Work)</h2>
  <ul>
    <li><strong>CI/CD Deployment Pipeline (GitHub Actions → EC2)</strong> — Built automated deployments triggered on push to <code>main</code>, using SSH-based auth and GitHub Secrets to safely deploy app updates.</li>
    <li><strong>Nginx Reverse Proxy Production Setup</strong> — Configured Nginx to serve the site on port 80 and proxy application traffic to the app runtime (avoiding direct exposure of port 5000).</li>
    <li><strong>Systemd + Gunicorn Service Management</strong> — Ran the web app as a managed Linux service for reliability, restart behavior, and consistent boot-time availability.</li>
    <li><strong>Resume Download Feature</strong> — Hosted the resume PDF in <code>/static</code> and implemented a <code>/download</code> route to force-download the correct file.</li>
    <li><strong>Debug + Hardening</strong> — Resolved common failures (missing Python modules/venv, file path issues, port access/security group confusion) to restore service and stabilize deployments.</li>
  </ul>

  <h2>Technical Skills</h2>
  <div class="grid">
    <div>
      <ul>
        <li>AWS Cloud Infrastructure, Azure Cloud Services</li>
        <li>DevOps, CI/CD Pipelines, Git Version Control</li>
        <li>Python (basic scripting), Bash Scripting</li>
        <li>Linux Administration (Red Hat), Windows Server</li>
      </ul>
    </div>
    <div>
      <ul>
        <li>IAM / SSO / SAML</li>
        <li>Cloud Security & Compliance (NIST / SOC2)</li>
        <li>System Monitoring & Troubleshooting</li>
        <li>Agile/Scrum, Jira/Confluence, Technical Documentation</li>
      </ul>
    </div>
  </div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
