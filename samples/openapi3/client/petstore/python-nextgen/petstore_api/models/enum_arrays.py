# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist, validator

class EnumArrays(BaseModel):
    """
    EnumArrays
    """
    just_symbol: Optional[StrictStr] = None
    array_enum: Optional[conlist(StrictStr)] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["just_symbol", "array_enum"]

    @validator('just_symbol')
    def just_symbol_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('>=', '$'):
            raise ValueError("must be one of enum values ('>=', '$')")
        return v

    @validator('array_enum')
    def array_enum_validate_enum(cls, v):
        if v is None:
            return v

        for i in v:
            if i not in ('fish', 'crab'):
                raise ValueError("each list item must be one of ('fish', 'crab')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EnumArrays:
        """Create an instance of EnumArrays from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnumArrays:
        """Create an instance of EnumArrays from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EnumArrays.parse_obj(obj)

        _obj = EnumArrays.parse_obj({
            "just_symbol": obj.get("just_symbol"),
            "array_enum": obj.get("array_enum")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

