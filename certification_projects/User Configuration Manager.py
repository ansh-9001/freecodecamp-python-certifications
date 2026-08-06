def add_setting(settings, key_value_tuple):
    key, value = key_value_tuple
    norm_key = key.lower()
    norm_value = value.lower()
    
    if norm_key in settings:
        return f"Setting '{norm_key}' already exists! Cannot add a new setting with this name."
    
    settings[norm_key] = norm_value
    return f"Setting '{norm_key}' added with value '{norm_value}' successfully!"

def update_setting(settings, key_value_tuple):
    key, value = key_value_tuple
    norm_key = key.lower()
    norm_value = value.lower()
    
    if norm_key in settings:
        settings[norm_key] = norm_value
        return f"Setting '{norm_key}' updated to '{norm_value}' successfully!"
        
    return f"Setting '{norm_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    norm_key = key.lower()
    
    if norm_key in settings:
        del settings[norm_key]
        return f"Setting '{norm_key}' deleted successfully!"
        
    return "Setting not found!"

def view_settings(settings):
    if settings == {}:
        return "No settings available."
    
    output = "Current User Settings:\n"
    for key, value in settings.items():
        output += f"{key.capitalize()}: {value}\n"
    return output


test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

view_settings(test_settings)

