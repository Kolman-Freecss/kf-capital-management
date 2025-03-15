# KF Capital Management

A desktop application built with Python and Kivy for capital management.

## Table of Contents

- [KF Capital Management](#kf-capital-management)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Project Structure](#project-structure)
  - [License](#license)

## Getting Started

<details>
    <summary>Requirements</summary>
<br>

  - **To package the application using Buildozer, you need to be on a Linux system (preferably Ubuntu). You will also need to install the following packages:**

```bash
# Optional WSL package
wsl --install
# ----

sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake ant

```

</details>

<details>
  <summary>Setup</summary>
<br>

  - **Install Android SDK and NDK:** To package the application for Android, you need to have the Android SDK and NDK installed.
    You also need to configure the `ANDROID_HOME` and `ANDROID_NDK_HOME` environment variables.
    -   `ANDROID_HOME`: Path to your Android SDK installation.
    -   `ANDROID_NDK_HOME`: Path to your Android NDK installation.

  - **Create and activate virtual environment:**
```bash
python -m venv venv
.\\venv\\Scripts\\activate
```

  -   **Install dependencies:**
```bash
pip install -r requirements.txt
```

  -   **Run the application:**
```bash
python src/main.py
```

</details>

<details>
  <summary>Package</summary>
<br>

  - **To package the application for desktop (Windows), you can use the following command:**

```bash
buildozer distclean
buildozer -v windows debug
```

  -   **To package the application for Android, you need to have the Android SDK and NDK installed. Then, you can use the following command:**

```bash
buildozer android debug

# WSL way
wsl bash -c "buildozer android debug"

```

</details>

## Project Structure

-   `src/`: Source code
    -   `controllers/`: Business logic
    -   `models/`: Data models
    -   `views/`: UI components
-   `resources/`: Static resources
-   `requirements.txt`: Project dependencies

## License

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. See the LICENSE file for details.
