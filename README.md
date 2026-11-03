# Play Time HoldCo — Venture Capital & Sports-Tech Web Platform

A 100% pixel-accurate replication of [Play Time HoldCo (playtime.vc)](https://www.playtime.vc/) with an executive-grade Master Administration Portal and full REST API backend.

## 🚀 Key Features

- **100% Visual Fidelity**: Exact typography (Fixture Condensed, Oswald, Roboto), split-screen layout, high-res background photography, SVGs, and Webflow-style smooth reveal animations.
- **Master Admin Portal (`admin.html`)**: Real-time content management for Hero, Portfolio Startups, Press Features, Footer & Socials, and SEO Meta tags.
- **REST API Backend (`server.py`)**: Full CRUD endpoints with local persistence in `data.json`.
- **Hybrid Hosting Architecture**: Works both with the Python REST API server or static hosting (GitHub Pages, Vercel, Netlify).

## 🛠️ Local Development

Run the API server with Python:

```bash
python server.py
```

- Public Site: `http://localhost:8888/index.html`
- Admin Portal: `http://localhost:8888/admin.html`
- API Content Endpoint: `http://localhost:8888/api/content`

---

## 🌐 Custom Domain Setup Guide (Hướng Dẫn Kết Nối Tên Miền)

### Cách 1: Kết nối tên miền qua GitHub Pages (Miễn phí)

1. **Bật GitHub Pages**:
   - Vào repository trên GitHub: `Settings` → `Pages`.
   - Tại mục **Build and deployment** / **Source**: Chọn `Deploy from a branch`.
   - Chọn branch `main` (hoặc `master`), thư mục `/ (root)`, nhấn **Save**.
2. **Cấu hình Custom Domain trên GitHub**:
   - Trong `Settings` → `Pages`, tại ô **Custom domain**, nhập tên miền của bạn (ví dụ: `playtime.yourdomain.com` hoặc `yourdomain.com`).
   - Nhấn **Save**.
   - Tích chọn **Enforce HTTPS** (để tự động có SSL miễn phí).
3. **Cấu hình DNS tại nhà cung cấp tên miền** (Cloudflare, Namecheap, GoDaddy, MatBao, PA Vietnam...):
   - **Nếu dùng Apex domain (`yourdomain.com`)**:
     Tạo 4 bản ghi `A` trỏ về IP của GitHub:
     - `185.199.108.153`
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`
   - **Nếu dùng Subdomain (`playtime.yourdomain.com` hoặc `www.yourdomain.com`)**:
     Tạo bản ghi `CNAME`:
     - Host / Name: `playtime` (hoặc `www`)
     - Value / Target: `<your-username>.github.io`

---

### Cách 2: Kết nối tên miền qua Vercel / Netlify / Render (Hỗ trợ cả REST API Server)

1. Đăng nhập Vercel hoặc Netlify bằng tài khoản GitHub.
2. Chọn **Add New Project** → Import repository vừa tạo.
3. Vào **Settings** → **Domains** → Điền tên miền của bạn và cấu hình bản ghi DNS theo hướng dẫn của nền tảng.
