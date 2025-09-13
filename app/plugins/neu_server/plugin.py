from app.plugins.base import AIPlugin


class Plugin(AIPlugin):
    tasks = ["ping"]

    def load(self) -> None:
        pass

    def infer(self, payload: dict) -> dict:
        pass
