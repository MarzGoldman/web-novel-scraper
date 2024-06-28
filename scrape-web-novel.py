import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse
import argparse
import os

# Function to get the next chapter URL
def get_next_chapter_url(soup, next_button_selector):
    next_button = soup.select_one(next_button_selector)
    if next_button and next_button.get('href'):
        return next_button['href']
    return None

# Function to scrape a chapter
def scrape_chapter(url, content_selector, heading_selector, text_selector, next_button_selector):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    page_content_html = soup.select_one(content_selector)
    chapter_heading_tag = page_content_html.select_one(heading_selector) if page_content_html else None
    chapter_heading = chapter_heading_tag.text.strip() if chapter_heading_tag else 'No Title'

    chapter_text_elements = page_content_html.select(text_selector) if page_content_html else []
    chapter_text = '\n'.join([p.text.strip() for p in chapter_text_elements])

    next_chapter_url = get_next_chapter_url(soup, next_button_selector)

    return chapter_heading, chapter_text, next_chapter_url

# Function to scrape the entire book
def scrape_book(start_url, content_selector, heading_selector, text_selector, next_button_selector):
    url = start_url
    book_content = []
    total_chapters_scraped = 0

    while url:
        print(f'+++ {total_chapters_scraped} Currently Reading URL: {url} ')
        try:
            chapter_heading, chapter_text, next_chapter_url = scrape_chapter(url, content_selector, heading_selector, text_selector, next_button_selector)
        except requests.RequestException as e:
            print(f'Failed to fetch {url}: {e}')
            break

        book_content.append({'heading': chapter_heading, 'text': chapter_text})
        total_chapters_scraped += 1
        print(f'--- {chapter_heading} >>> {chapter_text[:20]}... {chapter_text[-20:]}')
        print('')

        if total_chapters_scraped % 3 == 0:
            user_input = input(f'Scraped {total_chapters_scraped} chapters. Continue scraping? (y/n): ').strip().lower()
            if user_input != 'y':
                break

        url = next_chapter_url

    return book_content, total_chapters_scraped

# Function to save book content to a JSON file
def save_to_json(data, base_url, total_chapters_scraped):
    parsed_url = urlparse(base_url)
    book_title = parsed_url.path.strip('/').split('/')[-2]
    book_chapter = parsed_url.path.strip('/').split('/')[-1]
    filename = f'{book_title}-{book_chapter}+{total_chapters_scraped}.json'

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f'Book content saved to "{filename}".')
    return filename

# Function to save book content to a Markdown file
def save_to_markdown(data, base_url, total_chapters_scraped):
    parsed_url = urlparse(base_url)
    book_title = parsed_url.path.strip('/').split('/')[-2]
    book_chapter = parsed_url.path.strip('/').split('/')[-1]
    filename = f'{book_title}-{book_chapter}+{total_chapters_scraped}.md'

    markdown_content = ""
    for item in data:
        heading = item.get("heading", "")
        text = item.get("text", "")
        markdown_content += f"# {heading}\n\n{text}\n\n"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f'Book content saved to "{filename}".')
    return filename

# Placeholder function for saving to EPUB (not implemented)
def save_to_epub(data, base_url, total_chapters_scraped):
    print("EPUB format is not supported yet. Stay tuned for future updates!")
    return None

# Main function to parse arguments and start scraping
def main():
    parser = argparse.ArgumentParser(description='Scrape chapters from a web novel.')
    parser.add_argument('url', help='The URL of the first chapter of the book')
    parser.add_argument('--content-selector', default='.read-container', help='CSS selector for the chapter content container')
    parser.add_argument('--heading-selector', default='h1, h2, h3, h4, h5, h6', help='CSS selector for the chapter heading')
    parser.add_argument('--text-selector', default='p', help='CSS selector for the chapter text paragraphs')
    parser.add_argument('--next-button-selector', default='a:contains("Next")', help='CSS selector for the "Next" button')
    parser.add_argument('--output-format', choices=['json', 'markdown', 'epub'], default='json', help='The format to save the scraped content')

    args = parser.parse_args()

    book_content, total_chapters_scraped = scrape_book(
        args.url,
        args.content_selector,
        args.heading_selector,
        args.text_selector,
        args.next_button_selector
    )

    if args.output_format == 'json':
        save_to_json(book_content, args.url, total_chapters_scraped)
    elif args.output_format == 'markdown':
        save_to_markdown(book_content, args.url, total_chapters_scraped)
    elif args.output_format == 'epub':
        save_to_epub(book_content, args.url, total_chapters_scraped)
    else:
        print(f'Unsupported format: {args.output_format}')

if __name__ == '__main__':
    print("Welcome to the Web Novel Scraper! Let the scraping begin!")
    main()
    print("Scraping complete. Hope you enjoyed this automated adventure!")
