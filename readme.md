# RocketLaunchCountdown

RocketLaunchCountdown is a Python + HTML system to operate a launch countdown and Go/No-Go indicator. The Go/No-Go indicator can be driven either from a spreadsheet (CSV export via a share link configured in the Settings window) or from manual buttons in the app. The mode is selected with the radio button in Settings.

## Latest release

[RocketLaunchCountdown 0.7.0](https://github.com/HamsterSpaceNerd3000/RocketLaunchCountdown/releases/tag/v0.7.0-alpha)

### Features added

- Added ability to change clock once in T+.
- Added Major Concerns display.

## OBS instructions

To use the HTML files in OBS (or similar software) as browser sources:

1. Create a Browser source.
2. Select **Local file** and choose the HTML file you want to display (e.g. `countdown.html`, `gonogo.html`, `major_concerns.html`).
3. Check **Shutdown source when not visible** and **Refresh browser when scene becomes active**.
4. (Optional) Install the `xObsBrowserAutoRefresh` extension to enable timed automatic refreshes.
   - Download: https://obsproject.com/forum/resources/xobsbrowserautorefresh-timed-automatic-browser-source-refreshing.1677
   - Set auto-refresh times to your preference. Note: very fast refresh rates increase the chance of browser caching issues.

> Caution: The `xObsBrowserAutoRefresh` extension may not have a Mac version.

## Install instructions

Install is simple: download the installer, run it, and follow the prompts to install RocketLaunchCountdown.

If you want help wiring this into OBS (example scene setup, recommended refresh settings, or troubleshooting browser-source caching), tell me the OBS version and platform and I can give a short step-by-step.