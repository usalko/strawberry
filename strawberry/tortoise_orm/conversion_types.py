from __future__ import annotations

from typing import Any, Dict, Optional, TypeVar
from typing_extensions import Protocol

from tortoise.models import Model

from strawberry.types.types import TypeDefinition

TortoiseOrmModel = TypeVar("TortoiseOrmModel", bound=Model)


class StrawberryTypeFromTortoiseOrm(Protocol[TortoiseOrmModel]):
    """This class does not exist in runtime.
    It only makes the methods below visible for IDEs"""

    def __init__(self, **kwargs):
        ...

    @staticmethod
    def from_extra_model(
        instance: TortoiseOrmModel, extra: Optional[Dict[str, Any]] = None
    ) -> StrawberryTypeFromTortoiseOrm[TortoiseOrmModel]:
        ...

    def to_extra_model(self, **kwargs) -> TortoiseOrmModel:
        ...

    @property
    def _type_definition(self) -> TypeDefinition:
        ...

    @property
    def _extra_model_type(self) -> TortoiseOrmModel:
        ...
