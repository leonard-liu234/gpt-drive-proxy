# GPT Drive Proxy

This is a lightweight proxy service designed to solve the domain restriction issue when integrating Google OAuth in ChatGPT plugins.

## 🌐 Purpose

OpenAI plugins require the `authorization_url`, `token_url`, and plugin backend (`api`) to share the **same root domain**.  
Since Google OAuth is hosted on `*.google.com`, this service serves as a **proxy** to bridge OpenAI ↔ Google safely, allowing access to private Google Drive content like folders and files.

---

## 🚀 Features

- OAuth 2.0 redirect proxy compatible with OpenAI plugin framework
- Secure token exchange via your own Render instance
- Works seamlessly with ChatGPT plugin calls
- Enables "read-only" access to shared Google Drive folders

---

## 🛠️ How to Deploy

### Step 1: Clone the repository

```bash
git clone https://github.com/leonard-liu234/gpt-drive-proxy.git
