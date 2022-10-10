import scraper
from model import summarize

def main():
    user_input = input('Enter query to summarize: ')

    print("="*30)
    print("Processing scraping...".center(30))
    print("="*30)
    
    scrap = scraper.Scraper()
    scrap.enter_input(user_input)

    #google
    google_text = scrap.google_summary()
    google_queries = scrap.get_google_queries()

    #wikipedia
    scrap.wikipedia_page(user_input)
    text = scrap.get_text()
    clean_text = scrap.clean_text(text)
    
    scrap.close()

    #summrize
    summrize_text = summarize(clean_text)

    with open("output.txt", "w", encoding='utf-8') as f:
        f.write("Google summary: \n\n")
        f.write(google_text)
        f.write("\n\n")

        f.write("\nGoogle queries and ansewers:\n\n")
        f.write(google_queries)
        f.write("\n\n")

        f.write("\nSummary text from Wikipedia:\n\n")
        f.write(summrize_text)

        f.close()

if __name__ == '__main__':
    main()