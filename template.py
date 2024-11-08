import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "tourplanner"

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/agents/__init__.py',
    f'src/{project_name}/agents/user_interaction_agent.py',
    f'src/{project_name}/agents/itinerary_generation_agent.py',
    f'src/{project_name}/agents/optimization_agent.py',
    f'src/{project_name}/agents/memory_agent.py',
    f'src/{project_name}/agents/weather_agent.py',
    f'src/{project_name}/agents/map_agent.py',
    f'src/{project_name}/database/__init__.py',
    f'src/{project_name}/database/neo4j_connection.py',
    f'src/{project_name}/database/memory_manager.py',
    f'src/{project_name}/frontend/__init__.py',
    f'src/{project_name}/frontend/chat_interface.py',
    f'src/{project_name}/frontend/itinerary_display.py',
    f'src/{project_name}/frontend/login.py',
    f'src/{project_name}/llm/__init__.py',
    f'src/{project_name}/llm/llm_interface.py',
    f'src/{project_name}/llm/call_user_interaction.py',
    f'src/{project_name}/llm/call_itinerary_generation.py',
    f'src/{project_name}/llm/call_memory.py',
    f'src/{project_name}/routers/__init__.py',
    f'src/{project_name}/routers/user_interaction.py',
    f'src/{project_name}/routers/itinerary_generation.py',
    f'src/{project_name}/routers/optimization.py',
    f'src/{project_name}/routers/memory.py',
    f'src/{project_name}/routers/weather.py',
    f'src/{project_name}/routers/map.py',
    f'src/{project_name}/schemas/__init__.py',
    f'src/{project_name}/schemas/user.py',
    f'src/{project_name}/schemas/itinerary.py',
    f'src/{project_name}/schemas/memory.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/helpers.py',
    f'src/{project_name}/utils/constants.py',
    f'src/{project_name}/utils/logger.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html',
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir!='':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory; {filedir} for the file: {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'{filename} is already exists')
    
    else:
        logging.info(f'{filename} is alraedy exists')