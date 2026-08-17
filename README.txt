InfraHealth CI Patch
====================

Add this file to your repository:

.github/workflows/ci.yml

Then commit and push:

git add .github/workflows/ci.yml
git commit -m "Add GitHub Actions CI"
git push

GitHub Actions will automatically run the existing pytest tests on:
- Ubuntu
- Windows
- macOS

with Python:
- 3.10
- 3.11
- 3.12
