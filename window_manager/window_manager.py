import os

def get_window_manager():
    env_mapping = {
        'WM': ['WM'],
        'DE': ['XDG_CURRENT_DESKTOP', 'DESKTOP_SESSION']
    }

    for env_type, env_vars in env_mapping.items():
        for env_var in env_vars:
            if env_var in os.environ:
                if env_type == 'WM':
                    window_manager = os.environ[env_var]
                else:
                    window_manager = os.environ[env_var]

                return env_type, window_manager

    with open(os.path.join(os.environ['HOME'], '.xinitrc'), 'r') as f:
        lines          = f.readlines()
        window_manager = lines[-1].split()[1]

    return 'WM', window_manager
