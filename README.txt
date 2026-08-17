InfraHealth CLI Patch
=====================

Purpose
-------
After this update, you can still run:

    python main.py

But after installing the project you can also run:

    infrahealth

And:

    python -m infrahealth

Files to copy into your repository
----------------------------------
1. infrahealth/cli.py          (new)
2. infrahealth/__main__.py     (new)
3. main.py                     (replace)
4. pyproject.toml              (replace)

Install / verify
----------------
From the InfraHealth repository directory:

    python -m pip install -e .
    infrahealth --version

Expected output:

    InfraHealth 0.1.0

Then try:

    infrahealth

Git commit
----------
    git add .
    git commit -m "Add installable InfraHealth CLI"
    git push

What did NOT change
-------------------
- ping.py
- tcp.py
- http.py
- reporter.py
- runner.py
- config format
- monitoring behavior

This update only changes how the application is started and packaged.
