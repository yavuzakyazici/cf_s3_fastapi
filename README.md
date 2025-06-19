# ☁️ FastAPI + Cloudflare R2 (S3-Compatible) File Upload API

Minimal FastAPI project demonstrating secure file uploads and retrievals using **Cloudflare R2** (Amazon S3-compatible API) via **Boto3**.

---

## 🔧 Tech Stack

- **FastAPI** – Web framework
- **Boto3** – AWS-compatible SDK for Python
- **Cloudflare R2** – S3-compatible object storage
- **Pydantic** – Data validation
- **Uvicorn** – ASGI server

---

## 📂 Features

- Upload files to a private Cloudflare R2 bucket
- Retrieve download URLs securely
- Uses signed S3-compatible requests
- Compatible with AWS S3 if R2 keys are swapped
- Simple local `.env` setup for API keys and config

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yavuzakyazici/cf_s3_fastapi.git
cd cf_s3_fastapi
```
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Create a .env file
```env
R2_ACCESS_KEY=your_r2_access_key
R2_SECRET_KEY=your_r2_secret_key
R2_ENDPOINT=https://your_r2_endpoint
R2_BUCKET_NAME=your_bucket_name
```
⚠️ Do NOT commit .env — it's in .gitignore

5. Run the server
```bash
uvicorn main:app --reload
```
Visit http://localhost:8000/docs for Swagger UI.

🧪 Example API Usage
Upload File
```bash
POST /upload
FormData: file (binary)
```
List Files (optional)
```bash
GET /files

```
Get File URL

```bash
GET /files/{filename}
```

## 📎 Notes
-  Cloudflare R2 is S3-compatible, but faster for public delivery
-  You can easily swap in AWS S3 by changing credentials + endpoint
-  Safe for client-side integration (mobile/web uploads)


👤 Author
Yavuz Akyazıcı – Full-stack developer & creator of Jazz-A-Minute (JAM)-[iOS](https://apps.apple.com/tr/app/j-a-m/id6504705021) - [Android](https://play.google.com/store/apps/details?id=com.jazzaminute&hl=en)

This project is a simplified demo version of the backend streaming logic used in JAM.
