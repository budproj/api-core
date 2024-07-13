from enum import Enum


class ObjectiveModeEnum(Enum):
    COMPLETED = 'COMPLETED'
    PUBLISHED = 'PUBLISHED'
    DRAFT = 'DRAFT'
    DELETED = 'DELETED'
