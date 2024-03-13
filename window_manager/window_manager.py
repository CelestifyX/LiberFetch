import os

def get_window_manager():
    if 'WM' in os.environ:
        env_type       = 'WM'
        window_manager = os.environ['WM']
    elif 'XDG_CURRENT_DESKTOP' in os.environ:
        env_type       = 'DE'
        window_manager = os.environ['XDG_CURRENT_DESKTOP']
    elif 'DESKTOP_SESSION' in os.environ:
        env_type       = 'DE'
        window_manager = os.environ['DESKTOP_SESSION']
    else:
        env_type = 'WM'

        with open(os.path.join(os.environ['HOME'], '.xinitrc'), 'r') as f:
            lines          = f.readlines()
            window_manager = lines[-1].split()[1]
    return env_type, window_manager
