import scraper
from model import summarize

def main():
    user_input = input('Enter query to summarize: ')

    print("="*30)
    print("Processing scraping...".center(30))
    print("="*30)
    
    scrap = scraper.Scraper()
    scrap.enter_input(user_input)

    # Get Google summary and queries
    google_summary  = scrap.google_summary()
    google_queries = scrap.get_google_queries()

    # Get Wikipedia summary
    scrap.wikipedia_page(user_input)
    wikipedia_text = scrap.clean_text(scrap.get_text())
    
    scrap.close()

    # Get Wikipedia summary
    wikipedia_summary = summarize(wikipedia_text)

    with open("output.txt", "w", encoding='utf-8') as f:
        f.write("Google summary: \n\n")
        f.write(google_summary)
        f.write("\n\n")

        f.write("\nGoogle queries and ansewers:\n\n")
        f.write(google_queries)
        f.write("\n\n")

        f.write("\nSummary text from Wikipedia:\n\n")
        f.write(wikipedia_summary )

        f.close()

if __name__ == '__main__':
    main()