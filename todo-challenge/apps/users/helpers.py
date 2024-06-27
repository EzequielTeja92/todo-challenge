
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import validate_email

def validate_username(value):
    UnicodeUsernameValidator()(value)
    if User.objects.filter(username=value).exists():
        raise DjangoValidationError("Username already exists")
    return value

def validate_email_address(value):
    validate_email(value)
    if User.objects.filter(email=value).exists():
        raise DjangoValidationError("Email already exists")
    return value

def validate_first_name(value):
    if not value.isalpha():
        raise DjangoValidationError("First name should only contain alphabetic characters")
    if len(value) < 2:
        raise DjangoValidationError("First name should be at least 2 characters long")
    return value

def validate_last_name(value):
    if not value.isalpha():
        raise DjangoValidationError("Last name should only contain alphabetic characters")
    if len(value) < 2:
        raise DjangoValidationError("Last name should be at least 2 characters long")
    return value
