# 📚 Web Novel Scraper 🚀

Welcome to my **Web Novel Scraper** repository! Ever dreamed of scraping web novels and converting them to markdown? Or epub? Or JSON? Well, you shouldn't, it's illegal, but this educational script is here to inspire your dreams tonight. 🌟

## ⚠️ DISCLAIMER ⚠️

**This script is for educational purposes only.** Seriously. Don't go scraping sites without permission. We’re not here to start an internet riot.

## 📜 Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## 💡 Introduction

Welcome to the world of web scraping! This script allows you to scrape chapters from your favorite web novels and convert them into beautiful Markdown files. It’s like magic, but with code.

P.S. Not all websites are compatible. 

## ✨ Features

- **Scrapes web novels** like a pro.
- **Converts JSON** files to Markdown with elegance.
- **Highly customizable** with CSS selectors.
- **Hilarious debug messages** (well, at least mildly amusing).

## 🛠️ Installation

### Step 1: Clone the Repo

Open your terminal and run:

```sh
git clone https://github.com/your-username/web-novel-scraper.git
cd web-novel-scraper
```

### Step 2: Set Up Your Environment

Activate your virtual environment, or don’t. Who am I to tell you how to live your life?

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Now, let’s get those packages! Run:

```sh
pip install -r requirements.txt
```

(Just kidding, there's no `requirements.txt`. You'll need `requests` and `beautifulsoup4`.)

```sh
pip install requests beautifulsoup4
```

## 🧙‍♂️ Usage

### Scraping Like a Wizard

Run the following command to scrape your web novel:

```sh
python novel_scraper.py "https://url-of-starting-chapter/" --output-markdown "outputfile-name.md"
```

```sh
python novel_scraper.py "https://url-of-starting-chapter/" --output-json "outputfile-name.json"
```

```sh
python novel_scraper.py "https://url-of-starting-chapter/" --output-epub "outputfile-name.epub"
```

And voila! Watch as chapters are magically scraped and transformed into Markdown. 🪄

### Arguments (a.k.a. Spells)

- `url`: The URL of the first chapter.
- `--content-selector`: CSS selector for the chapter content container (default: `.read-container`).
- `--heading-selector`: CSS selector for the chapter heading (default: `h1, h2, h3, h4, h5, h6`).
- `--text-selector`: CSS selector for the chapter text paragraphs (default: `p`).
- `--next-button-selector`: CSS selector for the "Next" button (default: `a:contains("Next")`).
- `--output-markdown`: Name of the output Markdown file (default: `book_content.md`).

## 🧑‍💻 Contributing

Want to make this script even better? Fork the repo, make your changes, and send a pull request. We promise to review it with the utmost seriousness (and a bit of sarcasm).

## 📜 License

This project is licensed under the MIT License, because sharing is caring. Check out the `LICENSE` file for more details.

---

Happy scraping, and remember: with great power comes great responsibility. And a lot of JSON files. 

👾 **Stay classy, coders!** 👾

---
