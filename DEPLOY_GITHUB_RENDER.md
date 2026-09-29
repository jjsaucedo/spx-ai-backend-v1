2# Deploy SPX AI Backend V1 to GitHub + Render

## 1. GitHub repository

Repository:

`jjsaucedo/spx-ai-backend-v1`

The main branch should contain:

- `app/`
- `tests/`
- `requirements.txt`
- `render.yaml`
- `.env.example`
- `.python-version`
- `.gitignore`
- `README.md`
- `DEPLOY_GITHUB_RENDER.md`

## 2. Create the Render Web Service

In Render:

1. Click **New +**
2. Select **Web Service**
3. Connect GitHub
4. Select:

`jjsaucedo/spx-ai-backend-v1`

## 3. Render configuration

Runtime:

`Python`

Build command:

```text
pip install -r requirements.txt
