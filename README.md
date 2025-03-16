# KF Capital Management

A desktop application built with Python and Kivy for capital management.

## Table of Contents

- [KF Capital Management](#kf-capital-management)
  - [Table of Contents](#table-of-contents)
  - [Tech Stack](#tech-stack)
  - [Getting Started](#getting-started)
  - [Windows Setup](#windows-setup)
  - [Project Structure](#project-structure)
  - [License](#license)

## Tech Stack

- Python
- Kivy (Package manager for Android)
- PyInstaller

## Getting Started

<details>
    <summary>Setup</summary>
<br>

## Windows Setup

  - **Simple execution in local**

```bash
# Install dependencies

pip install -r requirements.txt
```

  - **To package the application using p4a (Android), you need to be on a Linux system (preferably Ubuntu) or PyInstaller (Windows). You will  need to install the following packages:**

/##########################<br>
/##    Android Packages  ##<br>
/##########################<br>

```bash
# Optional WSL package if you're on Windows and you're trying to package for Android
wsl --install
wsl.exe -d Ubuntu
# Inside wsl
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-pip
python3 --version
pip3 --version
pip install cython
pip show cython
# pip install matplotlib

# Create and activate virtual environment
cd ~
python3 -m venv venv
source venv/bin/activate
pip install python-for-android
# ----
```

```bash
# Using venv of python from WSL
# Ref: https://python-for-android.readthedocs.io/en/latest/quickstart.html#installation

# (Don't follow these steps if you've env built from wsl) Common issue: We've to convert activate script to unix format
sudo apt install dos2unix
sudo dos2unix venv/Scripts/activate
# ----

source venv/bin/activate
pip install python-for-android

# Install Prerequisites (Follow above REF)
# Now Install Android SDK with NDK
# Check latest SDK https://developer.android.com/studio?hl=es-419
# Use: https://dl.google.com/android/repository/<Replace with the latest you found in the link above>
# Install SDK
wget wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O commandlinetools-linux.zip
mkdir -p $HOME/android-sdk/cmdline-tools
unzip commandlinetools-linux.zip -d $HOME/android-sdk/cmdline-tools
mv $HOME/android-sdk/cmdline-tools/cmdline-tools $HOME/android-sdk/cmdline-tools/latest
# Export variables
# Edit nano ~/.bashrc and add the lines at bottom of file
nano ~/.bashrc
# Add the lines
export ANDROID_HOME=$HOME/android-sdk
export PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$PATH
export PATH=$ANDROID_HOME/platform-tools:$PATH
# Reloading environment
source ~/.bashrc

# Install NDK (Same as above)
wget https://dl.google.com/android/repository/android-ndk-r28-linux.zip -O android-ndk.zip
mkdir -p $HOME/android-sdk/ndk
unzip android-ndk.zip -d $HOME/android-sdk/ndk
# Edit nano ~/.bashrc and add the lines at bottom of file
nano ~/.bashrc
# Add the lines
export ANDROID_NDK_HOME=$HOME/android-sdk/ndk/android-ndk-r28
export PATH=$ANDROID_NDK_HOME:$PATH
# Reloading environment
source ~/.bashrc
# Check
ndk-build --version

# Install platform API and build-tools
sdkmanager "platforms;android-34"
sdkmanager "build-tools;28.0.2"

# Edit nano ~/.bashrc and add the lines at bottom of file

# Adjust the paths based on your installation
export ANDROIDSDK="$HOME/android-sdk"
export ANDROIDNDK="$HOME/android-sdk/ndk/android-ndk-r28"
export ANDROIDAPI="34"  # Target API version of your application
export NDKAPI="21"  # Minimum supported API version of your application
export ANDROIDNDKVER="r28"  # Version of the NDK you installed

# Reloading environment
source ~/.bashrc


# (Optional) Example packaging
p4a apk --private /mnt/d/Data/ProjectsData/Programming/Projects/AI/kf-capital-management --package=org.example.myapp --name "My application" --version 0.1 --bootstrap=sdl2 --requirements=python3,kivy --arch arm64-v8a --use-setup-py
``` 


/##########################<br>
/##    Windows Packages  ##<br>
/##########################<br>



</details>

<details>
  <summary>Package</summary>
<br>

  - **To package the application for desktop (Windows), you can use the following command:**

```bash
```

  -   **To package the application for Android, you need to have the Android SDK and NDK installed. Then, you can use the following command:**

With p4a (https://python-for-android.readthedocs.io/en/latest/quickstart.html#build-a-kivy-or-sdl2-application)

```bash
p4a apk --private /mnt/d/Data/ProjectsData/Programming/Projects/AI/kf-capital-management --package=org.example.myapp --name "My application" --version 0.1 --bootstrap=sdl2 --requirements=python3,kivy --arch arm64-v8a --use-setup-py
```

</details>

<details>
  <summary>Execute</summary>
<br>

  -   **Run the application:**
```bash
python src/main.py
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
