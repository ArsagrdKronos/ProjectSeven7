import json
import logging

class Command:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def execute(self, command_str):
        """Wykonanie komendy tekstowej."""
        try:
            command_dict = json.loads(command_str) if isinstance(command_str, str) else command_str
            action = command_dict.get("action", "unknown")
            self.logger.info(f"Wykonano komendę: {action}")
            return {"status": "success", "action": action}
        except Exception as e:
            self.logger.error(f"Błąd wykonania komendy: {e}")
            return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    cmd = Command()
    print(cmd.execute('{"action": "test"}'))