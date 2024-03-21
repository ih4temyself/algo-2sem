class VersionManager:
    def __init__(self, version="0.0.1"):
        if not version:
            version = "0.0.1"
        parts = version.split(".")
        try:
            self.major_version = int(parts[0])
            self.minor_version = int(parts[1]) if len(parts) > 1 else 0
            self.patch_version = int(parts[2]) if len(parts) > 2 else 0
        except ValueError:
            raise Exception("Error occured while parsing version!")

        self.history = []

        self._save_version()

    def _save_version(self):
        self.history.append(
            (self.major_version, self.minor_version, self.patch_version)
        )

    def major(self):
        self.major_version += 1
        self.minor_version = 0
        self.patch_version = 0
        self._save_version()
        return self

    def minor(self):
        self.minor_version += 1
        self.patch_version = 0
        self._save_version()
        return self

    def patch(self):
        self.patch_version += 1
        self._save_version()
        return self

    def rollback(self):
        if len(self.history) < 2:
            raise Exception("Cannot rollback!")
        self.history.pop()
        self.major_version, self.minor_version, self.patch_version = self.history[-1]
        return self

    def release(self):
        return f"{self.major_version}.{self.minor_version}.{self.patch_version}"


if __name__ == "__main__":
    version_manage = VersionManager("")
    # version_manage.major().minor()
    print(version_manage.release())
