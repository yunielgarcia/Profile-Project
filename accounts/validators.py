import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class CurrentValidator(object):
    def validate(self, password, user=None):
        """Validates new psw is different from current"""
        if user and user.check_password(password):
            raise ValidationError('Use different password than current')

    def get_help_text(self):
        return _(
            "Your password must not be the same as current one"
        )


class NamePartsValidator(object):
    def validate(self, password, user=None):
        """Validates new psw doesn't contain parts of full name"""
        if user:  # Means is changing psw
            if self.contain_weak_psw(password, user.username, user.first_name, user.last_name):
                raise ValidationError('Password must not contain username/first name/last name')

    def get_help_text(self):
        return _(
            "Your password must not be the same as current one"
        )

    def contain_weak_psw(self, psw, username, first, last):
        password = str(psw).lower()
        return (str(username).lower() in password or
                str(first).lower() in password or
                str(last).lower() in password)


class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 digit, 0-9."
        )


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter, A-Z."
        )


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 lowercase letter, a-z."
        )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&;*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("The password must contain at least 1 symbol: " +
                  "()[]{}|\`~!@#$%^&;*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 symbol: " +
            "()[]{}|\`~!@#$%^&amp;*_-+=;:'\",<>./?"
        )
