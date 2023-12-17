#!/bin/bash

# Change directory to the one containing the scripts
cd /Users/yorrickschoonheydt/Documents/Cinematen/Nieuwsblogger/Nieuwsblogger/Instagram_post_generator

# Run the scripts one after another
echo "Starting replace_image.py"
python replace_image.py
echo "replace_image.py finished"

echo "Starting Open_and_save.py"
python open_and_save.py
echo "Open_and_save.py finished"

# Run the scripts one after another
echo "Starting replace_text.py"
python replace_text.py
echo "replace_text.py finished"

# Run the scripts one after another
echo "Starting quit_photoshop.py"
python quit_photoshop.py
echo "quit_photoshop.py finished"

# Display notification on macOS
osascript -e 'display notification "All scripts have finished executing" with title "Notification"'