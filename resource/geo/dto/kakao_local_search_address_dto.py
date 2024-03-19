from __future__ import annotations

from typing import List
from typing import Any
from dataclasses import dataclass
import json


@dataclass
class Address:
    address_name: str
    b_code: str
    h_code: str
    main_address_no: str
    mountain_yn: str
    region_1depth_name: str
    region_2depth_name: str
    region_3depth_h_name: str
    region_3depth_name: str
    sub_address_no: str
    x: str
    y: str

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        _address_name = str(obj.get("address_name"))
        _b_code = str(obj.get("b_code"))
        _h_code = str(obj.get("h_code"))
        _main_address_no = str(obj.get("main_address_no"))
        _mountain_yn = str(obj.get("mountain_yn"))
        _region_1depth_name = str(obj.get("region_1depth_name"))
        _region_2depth_name = str(obj.get("region_2depth_name"))
        _region_3depth_h_name = str(obj.get("region_3depth_h_name"))
        _region_3depth_name = str(obj.get("region_3depth_name"))
        _sub_address_no = str(obj.get("sub_address_no"))
        _x = str(obj.get("x"))
        _y = str(obj.get("y"))
        return Address(_address_name, _b_code, _h_code, _main_address_no, _mountain_yn, _region_1depth_name,
                       _region_2depth_name, _region_3depth_h_name, _region_3depth_name, _sub_address_no, _x, _y)


@dataclass
class Document:
    address: Address
    address_name: str
    address_type: str
    road_address: RoadAddress
    x: str
    y: str

    @staticmethod
    def from_dict(obj: Any) -> 'Document':
        _address = Address.from_dict(obj.get("address"))
        _address_name = str(obj.get("address_name"))
        _address_type = str(obj.get("address_type"))
        _road_address = RoadAddress.from_dict(obj.get("road_address"))
        _x = str(obj.get("x"))
        _y = str(obj.get("y"))
        return Document(_address, _address_name, _address_type, _road_address, _x, _y)


@dataclass
class Meta:
    is_end: str
    pageable_count: int
    total_count: int

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        _is_end = str(obj.get("is_end"))
        _pageable_count = int(obj.get("pageable_count"))
        _total_count = int(obj.get("total_count"))
        return Meta(_is_end, _pageable_count, _total_count)


@dataclass
class RoadAddress:
    address_name: str
    building_name: str
    main_building_no: str
    region_1depth_name: str
    region_2depth_name: str
    region_3depth_name: str
    road_name: str
    sub_building_no: str
    underground_yn: str
    x: str
    y: str
    zone_no: str

    @staticmethod
    def from_dict(obj: Any) -> 'RoadAddress':
        _address_name = str(obj.get("address_name"))
        _building_name = str(obj.get("building_name"))
        _main_building_no = str(obj.get("main_building_no"))
        _region_1depth_name = str(obj.get("region_1depth_name"))
        _region_2depth_name = str(obj.get("region_2depth_name"))
        _region_3depth_name = str(obj.get("region_3depth_name"))
        _road_name = str(obj.get("road_name"))
        _sub_building_no = str(obj.get("sub_building_no"))
        _underground_yn = str(obj.get("underground_yn"))
        _x = str(obj.get("x"))
        _y = str(obj.get("y"))
        _zone_no = str(obj.get("zone_no"))
        return RoadAddress(_address_name, _building_name, _main_building_no, _region_1depth_name, _region_2depth_name,
                           _region_3depth_name, _road_name, _sub_building_no, _underground_yn, _x, _y, _zone_no)


@dataclass
class KaKaoLocalSearchAddressDto:
    documents: List[Document]
    meta: Meta

    @staticmethod
    def from_dict(obj: Any) -> KaKaoLocalSearchAddressDto:
        _documents = [Document.from_dict(y) for y in obj.get("documents")]
        _meta = Meta.from_dict(obj.get("meta"))
        return KaKaoLocalSearchAddressDto(_documents, _meta)
