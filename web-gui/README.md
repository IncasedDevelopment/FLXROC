![Banner](https://github.com/incaseddevelopment/flxroc/blob/master/flxroc/static/fluxroc_logo_black.svg)

[![license](https://img.shields.io/badge/license-GPL-brightgreen.svg)](https://github.com/incaseddevelopment/flxroc/blob/master/LICENSE)
[![version](https://img.shields.io/badge/version-1.0-lightgrey.svg)](https://github.com/incaseddevelopment/flxroc)
![build](https://github.com/incaseddevelopment/flxroc/workflows/build/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/incaseddevelopment/flxroc/badge.svg)](https://coveralls.io/github/incaseddevelopment/flxroc)

Questions? [Join the Discord support server](https://discord.gg/hTUKhHYTPe)

__Disclaimer__: This project should be used for authorized testing or educational purposes only.

FLXROC is an open-source post-exploitation framework for students, researchers and developers. It includes features such as:
- Command & control server with intuitive user-interface
- Custom payload generator for multiple platforms
- 12 post-exploitation modules

It is designed to allow students and developers to easily implement their own code and add cool new
features *without* having to write a C2 server or Remote Administration Tool from scratch.

This project has 2 main parts: the **original console-based application** (`/flxroc`) and the **web GUI** (`/web-gui`).

# Web GUI

## Dashboard
A control panel for your C2 server with a point-and-click interface for executing post-exploitation modules. The control panel includes an interactive map of client machines and a dashboard which allows efficient, intuitive administration of client machines.

![dashboard_preview](https://github.com/incaseddevelopment/flxroc/blob/master/web-gui/flxroc/assets/images/previews/preview-dashboard.png)

## Payload Generator
The payload generator uses black magic involving Docker containers & Wine servers to compile executable payloads for any platform/architecture you select. These payloads spawn reverse TCP shells with communication over the network encrypted via AES-256 after generating a secure symmetric key using the [Diffie-Hellman IKE](https://tools.ietf.org/html/rfc2409).

![payloads_preview](https://github.com/incaseddevelopment/flxroc/blob/master/web-gui/flxroc/assets/images/previews/preview-payloads2.png)

## Terminal Emulator
The web app includes an in-browser terminal emulator so you can still have direct shell access even when using the web GUI.

![terminal_preview](https://github.com/incaseddevelopment/flxroc/blob/master/web-gui/flxroc/assets/images/previews/preview-shell.png)
