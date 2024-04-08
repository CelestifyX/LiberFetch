import os

def get_window_manager():
    env_mapping = {
        'WM': ['WM'],
        'DE': ['XDG_CURRENT_DESKTOP', 'DESKTOP_SESSION']
    }

    for env_type, env_vars in env_mapping.items():
        for env_var in env_vars:
            if env_var in os.environ:
                return env_type, os.environ[env_var]

    try:
        with open(os.path.join(os.environ['HOME'], '.xinitrc'), 'r') as file:
            return 'WM', file.readlines()[-1].split()[1]
    except FileNotFoundError:
        return 'WM', 'Unknown'
