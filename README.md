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

1. **Clone the Repository:**
   git clone https://github.com/YOUR_USERNAME/osrs-price-checker.git
   cd osrs-price-checker

2. **Set Up a Virtual Environment & Dependencies:**
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install requests python-dotenv

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory of the project and provide a descriptive User-Agent string as required by the OSRS Wiki API policy:
   USER_AGENT=OSRS Price Checker - Portfolio Project - @YourGitHubUsername

4. **Run the Application:**
   python main.py

## 🖥️ Usage Showcase

===================================
      OSRS LIVE PRICE CHECKER      
===================================
[1] Search for an Item Price
[0] Exit Program
===================================
Enter your choice: 1

What are you looking for?: whip

-----------------------------------
    RESULTS PAGE 1
-----------------------------------
[1] Abyssal whip (ID: 4151)
[2] Frozen whip mix (ID: 12769)
[3] Volcanic whip mix (ID: 12771)
-----------------------------------
[0] Cancel Search

Select an item number, 'M' for more, or '0' to cancel: 1

Item: Abyssal whip (ID: 4151)
High Price: 997,862 gp
Low Price: 973,158 gp

Press Enter to continue back to menu...

## 🔒 Git Etiquette

Note that `item_cache.json` is explicitly included in the `.gitignore` to prevent committing bloated game data into the codebase repository. The application will autonomously generate it on its first launch environment.