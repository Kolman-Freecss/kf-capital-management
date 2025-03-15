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
  <summary>Setup</summary>
<br>

  -   **Create and activate virtual environment:**
    \`
    python -m venv venv
    .\\venv\\Scripts\\activate
    \`

  -   **Install dependencies:**
    \`
    pip install -r requirements.txt
    \`

  -   **Run the application:**
    \`
    python src/main.py
    \`

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
