from profile import Profile
import re


class ProfileMixin(object):

    @property
    def profile(self):
        if not hasattr(self, '_profile') or not self._profile:
            self._profile = None
            for field in self._meta.get_fields():
                field_name = field.name
                value = getattr(self, field_name, None)
                if value and isinstance(value, Profile):
                    self._profile = value
        return self._profile

    def __getattr__(self, name):
        pattern = re.compile(r'^is_(.+)$')
        match = re.match(pattern, name)
        if match:
            return self.is_profile(match.group(1))

    def is_profile(self, name):
        return bool(getattr(self, name, None))
