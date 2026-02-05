# SUPER beginner guide: get a Windows `.exe` without owning Windows

You are doing great. We will do this in tiny steps.

You only need:
- A GitHub account
- Any browser (Chrome, Edge, Safari, Firefox)

No Windows computer needed.

---

## Big picture (1 sentence)

You upload this project to GitHub, click a button in the **Actions** tab, then download the built EXE.

---

## Part 1: Open GitHub in a browser

1. Open a browser:
   - Mac: Safari or Chrome
   - Linux: Firefox or Chrome
2. Go to: `https://github.com`
3. Sign in.

---

## Part 2: Find your repo page (this is the page you were asking about)

A repo page looks like this:
- `https://github.com/<your-username>/<repo-name>`

Example:
- `https://github.com/jane/Windows-SOP`

### If you already uploaded this project

1. Click your profile picture (top-right).
2. Click **Your repositories**.
3. Click the repo name (for example `Windows-SOP`).
4. You are now on the **repo page**.

### If you did NOT upload yet

Ask someone to upload once, or use GitHub Desktop. After upload, come back to this file and continue.

---

## Part 3: Build the EXE from the repo page

Now you should be on:
- `https://github.com/<your-username>/<repo-name>`

At the top of the repo page, you will see tabs like:
- **Code**
- **Issues**
- **Pull requests**
- **Actions**  ← click this one

### Click-by-click

1. Click **Actions**.
2. On the left side, click workflow: **Build Windows EXE**.
3. On the right, click **Run workflow**.
4. In the small popup, click green **Run workflow** button.
5. Wait 2–8 minutes.
6. When done, the run gets a green check ✅.
7. Click that finished run.
8. Scroll down to **Artifacts**.
9. Click artifact: **SOP-Video-Cutter-Windows** to download.
10. Unzip the downloaded file.

Inside it, you will find:
- `SOP Video Cutter.exe`

---

## Part 4: What to send to your users

Send users the **whole unzipped folder**, not only the EXE.

Users then do only this:
1. Open folder
2. Double-click `SOP Video Cutter.exe`
3. Drag/drop video

No terminal for users.

---

## If you cannot see the Actions tab

Possible reasons:
- You are not on the repo page yet
- You are in the wrong repo
- Actions are disabled in repo settings

Quick check:
1. URL should be `github.com/<username>/<repo>`
2. You should see tabs: Code / Issues / Pull requests / Actions

---

## If SmartScreen appears on Windows

Tell user to click:
1. **More info**
2. **Run anyway**

This is common for unsigned apps.
