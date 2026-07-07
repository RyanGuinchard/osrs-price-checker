# OSRS Live Price Checker

A robust, terminal-based Command Line Interface (CLI) application built in Python that interfaces with the official Old School RuneScape (OSRS) Wiki Prices API. It allows users to dynamically search for in-game items, handle multi-match query selections with a page-by-page breakdown, and instantly fetch live, real-time marketplace prices.

This project was built following a structured Model-View-Controller (MVC) approach to demonstrate clean data pipelines, network optimization, and professional terminal application design.

## 🚀 Features

- **Fuzzy Search & Pagination:** Search for any item with partial keywords (e.g., typing `whip` brings up all whip variants). If there are dozens of results, the app streams them cleanly in chunks of 10 with a responsive `[M] Show More` option.
- **Smart 24-Hour Local Caching:** To remain compliant with the OSRS Wiki API etiquette and avoid redundant network latency, the item catalog mapping is cached locally (`item_cache.json`). The app intelligently tracks file modification timestamps to automatically refresh the cache every 24 hours.
- **Defensive CLI Design:** Implements clean terminal screen-wiping across Windows and Unix environments, graceful input loop validation, and structured summary formatting.

## 🛠️ Tech Stack & Concepts Demonstrated

- **Language:** Python 3.10+ (utilizes modern features like structural pattern matching `match/case`).
- **Networking:** Asynchronous-feeling HTTP REST requests using `requests`.
- **Data Architecture:** Fully separated concerns utilizing an Object-Oriented paradigm (`OSRSApiClient` for network/I/O, `Item` model for data representation and view layout, and a central controller loop in `main.py`).
- **File I/O:** Serializing and deserializing large data streams using Python's native `json` module.

## 📋 Installation & Setup