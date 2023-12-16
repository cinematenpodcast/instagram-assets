#!/bin/bash

# Change directory to the one containing the scripts
cd /Users/yorrickschoonheydt/Documents/Cinematen/Nieuwsblogger/Nieuwsblogger

# Run the scripts one after another
echo "Starting webscraper.py"
python webscraper.py
echo "webscraper.py finished"

echo "Starting article_scraper.py"
python article_scraper.py
echo "article_scraper.py finished"

echo "Starting article_writer.py"
python article_writer.py
echo "article_writer.py finished"

echo "Starting article_formatting.py"
python article_formatting.py
echo "article_formatting.py finished"

# Display notification on macOS
osascript -e 'display notification "All scripts have finished executing" with title "Notification"'
