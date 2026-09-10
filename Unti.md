#  [[#Android Security Checkli
### Post-malware recovery & hardening, for when things feel "off"

---

## 🚩 Red flags to take seriously

| Symptom | What it usually means |
|---|---|
| Windows/apps opening by themselves | Possible malware, accessibility abuse, or adware |
| Pop-up pushing a "security" app download | Classic **scareware** — do NOT install |
| Phone "acting weird" after a factory reset | Something likely re-synced or reinstalled from a backup |
| Unknown apps in your app list | Investigate — may be malware or bloat to remove |
| Battery/data spikes | Something is running in the background you didn't start |

---

## 🧹 The clean-slate factory reset (if you didn't do it right the first time)

1. **Settings → System → Reset → Factory data reset**
2. During setup, **skip "Restore from backup"** entirely
3. **Do not** auto-reinstall apps from your Google account
4. Set it up as a **fresh device** — sign in, but don't sync apps
5. Reinstall apps **one at a time**, only the ones you actually use
6. This eliminates anything that may have carried over

> The first reset only helps if you stop the bad stuff from re-entering through backup/restore.

---

## 🔐 Permissions — revoke aggressively

The permissions most abused by malware, in priority order:

### ⛔ Accessibility — the #1 danger
Can read your screen, read what you type, and control other apps. Go through **every** app that has it. Only trusted system apps (and maybe a password manager) should have it.

### ⚠️ High-risk permissions
- **Phone / Call logs** — only your dialer
- **SMS** — only your messaging app
- **Contacts** — only dialer, messaging, verified contacts apps
- **Location** — only maps, rideshare, weather
- **Microphone / Camera** — only camera, video call apps

### ✅ Safe-ish permissions
- Storage / Files (most apps genuinely need this)
- Notifications

### Rule of thumb
> A **game has zero business** with accessibility, phone, SMS, contacts, location, microphone, or camera. Revoke all of them.

---

## ⌨️ Keyboards & keylogging

- **Samsung Keyboard** and **Gboard** are both legitimate stock keyboards — switching between them won't fix or cause malware
- The real keylogging risk comes from **third-party keyboards** or apps with **accessibility** permission
- If you want to be safe: stick with a stock keyboard (Samsung or Gboard) and audit anything else with accessibility

---

## 🛡️ Safe browsing & hardening tips

- **Safe Browsing → Enhanced Protection**: good. Keep it on.
- **Don't install apps from pop-ups, ads, or "you have a virus" prompts** — only from the Play Store, and even then, check the developer name and reviews
- **Review installed apps periodically**: Settings → Apps → scroll the full list, uninstall anything you don't recognize
- **Disable "Install unknown apps"** for everything except, maybe, a file manager you explicitly trust
- **Keep Google Play Protect on**

---

## 🔁 The paranoid-but-practical loop

```
1. Notice something weird
2. Note the symptom (don't dismiss it)
3. Revoke permissions broadly
4. Check the app list for unknowns
5. If it keeps happening → clean reset, skip restore
6. Reinstall minimal apps, one at a time
7. Watch for recurrence
```

---

## 🎓 Why this is good training

Every scare like this teaches you the actual Android permission pathways, the settings layout, and the muscle memory to shut things down fast. That knowledge is worth more than any one security app. The goal isn't to never get hit — it's to **recover fast and confidently** when you do.