
import json

class JsonHelper:
    """Serves all strings & settings from the JSON database."""

    def get_points(self, user_id):
        """Returns the points of the user that belongs to the specified ID."""
        with open('database.json') as f:
            db = json.load(f)
            f.close()
        for attribute in db['users']:
            if attribute['id'] == user_id:
                return attribute['points']


    def get_blacklist(self):
        """Returns the whole blacklist."""
        with open('database.json') as f:
            db = json.load(f)
            f.close()
        return db['blacklist']


    def is_blacklisted(self, command):
        """Returns a boolean that describes the current blacklist state of a command."""
        with open('database.json') as f:
            db = json.load(f)
            f.close()
        for cmd in db['blacklist']:
            return cmd == command


    def add_to_blacklist(self, command):
        """Adds a command to the blacklist."""
        pass

    def remove_from_blacklist(self, command):
        """Removes a command from the blacklist."""
        pass

    def is_muted(self, user_id):
        """Returns a boolean that describes the current mute state of a user."""
        with open('database.json') as f:
            db = json.load(f)
            f.close()
        for attribute in db['users']:
            if attribute['id'] == user_id:
                return attribute['muted']


    def unmute(self, user_id):
        """Unmutes a user."""
        pass

    def mute(self, user_id):
        """Mutes a user."""
        pass
