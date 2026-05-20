# Ubuntu Dock Click-Action Commands Reference

This file is for changing how Ubuntu Dock behaves when you click an app icon, especially when multiple windows of the same app are open.

These commands affect only this GNOME/Ubuntu Dock setting:

org.gnome.shell.extensions.dash-to-dock click-action

They do not install software, remove software, or change system files.

---

## 1. Check current dock click behavior

```bash
gsettings get org.gnome.shell.extensions.dash-to-dock click-action
```

What it does:
Shows your current dock click-action setting.

Example output:

```text
'focus-or-previews'
```

---

## 2. Show all allowed values

```bash
gsettings range org.gnome.shell.extensions.dash-to-dock click-action
```

What it does:
Shows all valid values that your Ubuntu system accepts for this setting.

Use this before experimenting if you want to confirm what your system supports.

---

## 3. Set dock click behavior to cycle windows

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'cycle-windows'
```

What it does:
When multiple windows of the same app are open, clicking the app icon repeatedly cycles through those windows.

Example:
If you have 3 Chrome windows open:

- Click Chrome icon once: opens/focuses Chrome window 1
- Click again: switches to Chrome window 2
- Click again: switches to Chrome window 3
- Click again: returns to Chrome window 1

Good for:
People who use multiple Chrome windows and want fast switching.

---

## 4. Set dock click behavior to minimize or show previews

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize-or-previews'
```

What it does:
- If only one window of the app is open, clicking the icon minimizes/restores it.
- If multiple windows are open, clicking the icon shows window previews.

Good for:
A more Mac-like dock behavior where multiple windows can be visually selected.

---

## 5. Set dock click behavior to focus or show previews

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'focus-or-previews'
```

What it does:
- If one window is open, clicking the icon focuses it.
- If multiple windows are open, clicking the icon shows previews.

Good for:
Default-style Ubuntu behavior with previews for multiple windows.

This is commonly the default or near-default behavior.

---

## 6. Set dock click behavior to minimize

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'
```

What it does:
Clicking the app icon minimizes the app window.

Good for:
Users who want simple minimize-on-click behavior.

Possible downside:
It may feel less useful when multiple windows of the same app are open.

---

## 7. Set dock click behavior to previews only

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'previews'
```

What it does:
Clicking the app icon shows window previews.

Good for:
Users who prefer selecting windows visually.

---

## 8. Set dock click behavior to minimize or overview

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize-or-overview'
```

What it does:
Depending on the app/window state, clicking the icon may minimize the window or show the overview.

Good for:
Users who like using GNOME overview.

---

## 9. Set dock click behavior to launch

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'launch'
```

What it does:
Clicking the icon launches the app.

Good for:
Rarely needed. Usually not ideal for everyday dock behavior.

---

## 10. Set dock click behavior to skip

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'skip'
```

What it does:
Clicking the running app icon does nothing.

Good for:
Almost never needed.

---

## 11. Set dock click behavior to quit

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'quit'
```

What it does:
Clicking the app icon quits the app.

Warning:
Be careful with this. It can close apps accidentally.

---

## 12. Reset dock click behavior to Ubuntu default

```bash
gsettings reset org.gnome.shell.extensions.dash-to-dock click-action
```

What it does:
Resets this one setting back to the default value chosen by Ubuntu/GNOME.

Use this if:
You changed the behavior and want to return to the original setting.

---

# Recommended settings

## Best for multiple Chrome windows

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'cycle-windows'
```

Why:
Fastest for switching between several Chrome windows.

---

## Best for Mac-like behavior

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize-or-previews'
```

Why:
Single window minimizes/restores; multiple windows show previews.

---

## Safest way to experiment

Step 1: Save current setting

```bash
gsettings get org.gnome.shell.extensions.dash-to-dock click-action
```

Step 2: Try a new setting

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'cycle-windows'
```

Step 3: If you do not like it, reset

```bash
gsettings reset org.gnome.shell.extensions.dash-to-dock click-action
```

Or manually go back to a known behavior:

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'focus-or-previews'
```

---

# Notes

- No reboot is needed.
- The change usually applies immediately.
- This affects only the dock click behavior.
- It does not harm your stable Ubuntu setup.
- Worst case: the dock feels different, and you reset it.

