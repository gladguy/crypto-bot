#!/bin/bash

# Create files in app/
touch ./app/{__init__.py,bot.py,analyzer.py,webui.py,models.py,utils.py}

# Create files in templates/
touch ./templates/{index.html,filters.html,logs.html}

# Create files in static/
touch ./static/styles.css

# Create files in tests/
touch ./tests/{test_bot.py,test_analyzer.py}

# Create root-level files
touch ./{config.yaml,.env,.gitignore,requirements.txt,README.md,main.py,Dockerfile,docker-compose.yml}

# Print completion message
echo "Project structure created successfully!"
