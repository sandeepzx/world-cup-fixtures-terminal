# World Cup Fixtures Terminal CLI ⚽

A lightweight, terminal-based Command Line Interface (CLI) application that fetches and displays upcoming FIFA World Cup match fixtures. Built to provide football fans with a fast, distraction-free way to track their favorite teams directly from the terminal without opening a browser.

The application integrates with the `football-data.org` API to retrieve real-time tournament data, dynamically filters the response based on user input, and automatically converts UTC match times into Indian Standard Time (IST).

---

## ✨ Features

- **Smart Team Filtering:** Instantly searches the tournament schedule based on your favourite country.
- **IST Time Conversion:** Automatically handles timezone offsets to display accurate match dates and times in Indian Standard Time.
- **Minimalist CLI Design:** A clean, fast, and light terminal interface.
- **Live API Integration:** Fetches accurate, structured tournament data on-demand.

---

## 🚀 How It Works

Simply run the script, enter your favourite team when prompted, and get a clean list of their upcoming matches:

```text
Enter your favourite team: brazil

Brazil's Fixtures are:
2026-06-14 03:30 AM  -  Brazil vs Morocco
2026-06-20 06:00 AM  -  Brazil vs Haiti
2026-06-25 03:30 AM  -  Scotland vs Brazil
```

---

## 🛠️ Tech Stack & Prerequisites

- **Language:** Python 
- **API Source:** [football-data.org](https://football-data.org)
- **Core Modules Used:** API Requests, JSON Parsing, Datetime Timezone Conversion

---

## 📦 Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/sandeepzx/world-cup-fixtures-terminal
cd YOUR_REPOSITORY_NAME
```

### 2. Get a Free API Key
1. Go to [football-data.org](https://football-data.org) and register for a free API token.
2. Keep the token safe.

### 3. Run the Application
*(Modify this step based on your project's language and requirements)*
```bash
python match.py
```

---

## 🗺️ Future Roadmap

- [ ] Add live score updates for ongoing matches.
- [ ] Display current group stage standings and tables.
- [ ] Add support for multiple timezone conversions globally.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

