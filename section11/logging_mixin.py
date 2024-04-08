class LoggingMixin:

    @staticmethod
    def log(severity, message):
        print(f"{severity} -- {__class__.__name__} -- {message}")

    def info(self, message):
        self.log("INFO", message)

    def error(self, message):
        self.log("ERROR", message)
