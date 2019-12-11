
import re


class ProfileMixin():

    def __getattr__(self, name):
        pattern = re.compile(r'^is_(.+)$')
        match = re.match(pattern, name)
        if match:
            return self.is_profile(match.group(1))

    def is_profile(self, name):
        return bool(getattr(self, name, None))
