from dataclasses import dataclass
from typing import Union

from dataclass_wizard import JSONWizard


@dataclass
class Container:
    """
    Container dataclass

    """
    data: 'Data'


@dataclass
class Data(JSONWizard):
    """
    Data dataclass

    """
    source_file: str
    exif_tool: 'ExifTool'
    file: 'File'
    png: 'PNG'
    exif: 'EXIF'
    xmp: 'XMP'
    composite: 'Composite'


@dataclass
class ExifTool:
    """
    ExifTool dataclass

    """
    exif_tool_version: 'ExifToolVersion'
    now: 'Now'
    new_guid: 'NewGUID'
    file_sequence: 'FileSequence'
    processing_time: 'ProcessingTime'


@dataclass
class ExifToolVersion:
    """
    ExifToolVersion dataclass

    """
    desc: str
    val: float


@dataclass
class Now:
    """
    Now dataclass

    """
    desc: str
    val: str


@dataclass
class NewGUID:
    """
    NewGUID dataclass

    """
    desc: str
    num: str
    val: str


@dataclass
class FileSequence:
    """
    FileSequence dataclass

    """
    desc: str
    val: int


@dataclass
class ProcessingTime:
    """
    ProcessingTime dataclass

    """
    desc: str
    num: float
    val: str


@dataclass
class File:
    """
    File dataclass

    """
    file_name: 'FileName'
    base_name: 'BaseName'
    directory: 'Directory'
    file_path: 'FilePath'
    file_size: 'FileSize'
    file_modify_date: 'FileModifyDate'
    file_access_date: 'FileAccessDate'
    file_inode_change_date: 'FileInodeChangeDate'
    file_permissions: 'FilePermissions'
    file_attributes: 'FileAttributes'
    file_device_number: 'FileDeviceNumber'
    file_inode_number: 'FileInodeNumber'
    file_hard_links: 'FileHardLinks'
    file_user_id: 'FileUserID'
    file_group_id: 'FileGroupID'
    file_device_id: 'FileDeviceID'
    file_block_size: 'FileBlockSize'
    file_block_count: 'FileBlockCount'
    file_create_date: 'FileCreateDate'
    md_item_fs_content_change_date: 'MDItemFSContentChangeDate'
    md_item_fs_creation_date: 'MDItemFSCreationDate'
    md_item_fs_creator_code: 'MDItemFSCreatorCode'
    md_item_fs_finder_flags: 'MDItemFSFinderFlags'
    md_item_fs_has_custom_icon: 'MDItemFSHasCustomIcon'
    md_item_fs_invisible: 'MDItemFSInvisible'
    md_item_fs_is_extension_hidden: 'MDItemFSIsExtensionHidden'
    md_item_fs_is_stationery: 'MDItemFSIsStationery'
    md_item_fs_label: 'MDItemFSLabel'
    md_item_fs_name: 'MDItemFSName'
    md_item_fs_node_count: 'MDItemFSNodeCount'
    md_item_fs_owner_group_id: 'MDItemFSOwnerGroupID'
    md_item_fs_owner_user_id: 'MDItemFSOwnerUserID'
    md_item_fs_size: 'MDItemFSSize'
    md_item_fs_type_code: 'MDItemFSTypeCode'
    x_attr_macl: 'XAttrMacl'
    file_type: 'FileType'
    file_type_extension: 'FileTypeExtension'
    mime_type: 'MIMEType'
    exif_byte_order: 'ExifByteOrder'


@dataclass
class FileName:
    """
    FileName dataclass

    """
    desc: str
    val: str


@dataclass
class BaseName:
    """
    BaseName dataclass

    """
    desc: str
    val: str


@dataclass
class Directory:
    """
    Directory dataclass

    """
    desc: str
    val: str


@dataclass
class FilePath:
    """
    FilePath dataclass

    """
    desc: str
    val: str


@dataclass
class FileSize:
    """
    FileSize dataclass

    """
    desc: str
    num: int
    val: str


@dataclass
class FileModifyDate:
    """
    FileModifyDate dataclass

    """
    desc: str
    val: str


@dataclass
class FileAccessDate:
    """
    FileAccessDate dataclass

    """
    desc: str
    val: str


@dataclass
class FileInodeChangeDate:
    """
    FileInodeChangeDate dataclass

    """
    desc: str
    val: str


@dataclass
class FilePermissions:
    """
    FilePermissions dataclass

    """
    desc: str
    num: int
    val: str


@dataclass
class FileAttributes:
    """
    FileAttributes dataclass

    """
    desc: str
    num: str
    val: str


@dataclass
class FileDeviceNumber:
    """
    FileDeviceNumber dataclass

    """
    desc: str
    val: int


@dataclass
class FileInodeNumber:
    """
    FileInodeNumber dataclass

    """
    desc: str
    val: int


@dataclass
class FileHardLinks:
    """
    FileHardLinks dataclass

    """
    desc: str
    val: int


@dataclass
class FileUserID:
    """
    FileUserID dataclass

    """
    desc: str
    num: int
    val: str


@dataclass
class FileGroupID:
    """
    FileGroupID dataclass

    """
    desc: str
    num: int
    val: str


@dataclass
class FileDeviceID:
    """
    FileDeviceID dataclass

    """
    desc: str
    num: int
    val: int


@dataclass
class FileBlockSize:
    """
    FileBlockSize dataclass

    """
    desc: str
    val: int


@dataclass
class FileBlockCount:
    """
    FileBlockCount dataclass

    """
    desc: str
    val: int


@dataclass
class FileCreateDate:
    """
    FileCreateDate dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSContentChangeDate:
    """
    MDItemFSContentChangeDate dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSCreationDate:
    """
    MDItemFSCreationDate dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSCreatorCode:
    """
    MDItemFSCreatorCode dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSFinderFlags:
    """
    MDItemFSFinderFlags dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSHasCustomIcon:
    """
    MDItemFSHasCustomIcon dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSInvisible:
    """
    MDItemFSInvisible dataclass

    """
    desc: str
    val: int


@dataclass
class MDItemFSIsExtensionHidden:
    """
    MDItemFSIsExtensionHidden dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSIsStationery:
    """
    MDItemFSIsStationery dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSLabel:
    """
    MDItemFSLabel dataclass

    """
    desc: str
    num: str
    val: str


@dataclass
class MDItemFSName:
    """
    MDItemFSName dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSNodeCount:
    """
    MDItemFSNodeCount dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSOwnerGroupID:
    """
    MDItemFSOwnerGroupID dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSOwnerUserID:
    """
    MDItemFSOwnerUserID dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSSize:
    """
    MDItemFSSize dataclass

    """
    desc: str
    val: str


@dataclass
class MDItemFSTypeCode:
    """
    MDItemFSTypeCode dataclass

    """
    desc: str
    val: str


@dataclass
class XAttrMacl:
    """
    XAttrMacl dataclass

    """
    desc: str
    val: str


@dataclass
class FileType:
    """
    FileType dataclass

    """
    desc: str
    val: str


@dataclass
class FileTypeExtension:
    """
    FileTypeExtension dataclass

    """
    desc: str
    num: str
    val: str


@dataclass
class MIMEType:
    """
    MIMEType dataclass

    """
    desc: str
    val: str


@dataclass
class ExifByteOrder:
    """
    ExifByteOrder dataclass

    """
    desc: str
    num: str
    val: str


@dataclass
class PNG:
    """
    PNG dataclass

    """
    image_width: 'ImageWidth'
    image_height: 'ImageHeight'
    bit_depth: 'BitDepth'
    color_type: 'ColorType'
    compression: 'Compression'
    filter: 'Filter'
    interlace: 'Interlace'
    srgb_rendering: 'SRGBRendering'


@dataclass
class ImageWidth:
    """
    ImageWidth dataclass

    """
    desc: str
    val: int


@dataclass
class ImageHeight:
    """
    ImageHeight dataclass

    """
    desc: str
    val: int


@dataclass
class BitDepth:
    """
    BitDepth dataclass

    """
    desc: str
    val: int


@dataclass
class ColorType:
    """
    ColorType dataclass

    """
    desc: str
    num: int
    val: str


@dataclass
class Compression:
    """
    Compression dataclass

    """
    desc: str
    num: int
    val: str


@dataclass
class Filter:
    """
    Filter dataclass

    """
    desc: str
    num: int
    val: str


@dataclass
class Interlace:
    """
    Interlace dataclass

    """
    desc: str
    num: int
    val: str


@dataclass
class SRGBRendering:
    """
    SRGBRendering dataclass

    """
    desc: str
    num: int
    val: str


@dataclass
class EXIF:
    """
    EXIF dataclass

    """
    orientation: 'Orientation'
    date_time_original: 'DateTimeOriginal'
    user_comment: 'UserComment'
    color_space: 'ColorSpace'
    exif_image_width: 'ExifImageWidth'
    exif_image_height: 'ExifImageHeight'


@dataclass
class Orientation:
    """
    Orientation dataclass

    """
    desc: str
    num: int
    val: str


@dataclass
class DateTimeOriginal:
    """
    DateTimeOriginal dataclass

    """
    desc: str
    val: str


@dataclass
class UserComment:
    """
    UserComment dataclass

    """
    desc: str
    val: str


@dataclass
class ColorSpace:
    """
    ColorSpace dataclass

    """
    desc: str
    num: int
    val: str


@dataclass
class ExifImageWidth:
    """
    ExifImageWidth dataclass

    """
    desc: str
    val: int


@dataclass
class ExifImageHeight:
    """
    ExifImageHeight dataclass

    """
    desc: str
    val: int


@dataclass
class XMP:
    """
    XMP dataclass

    """
    xmp_toolkit: 'XMPToolkit'
    date_created: 'DateCreated'
    user_comment: 'UserComment'


@dataclass
class XMPToolkit:
    """
    XMPToolkit dataclass

    """
    desc: str
    val: str


@dataclass
class DateCreated:
    """
    DateCreated dataclass

    """
    desc: str
    val: str


@dataclass
class UserComment:
    """
    UserComment dataclass

    """
    desc: str
    val: str


@dataclass
class Composite:
    """
    Composite dataclass

    """
    image_size: 'ImageSize'
    megapixels: 'Megapixels'
    base_name: 'BaseName'
    fsmime_type: 'FSMIMEType'
    file_extension: 'FileExtension'
    file_type_description: 'FileTypeDescription'
    is_original: 'IsOriginal'
    long_edge: 'LongEdge'
    parent_folder: 'ParentFolder'
    short_edge: 'ShortEdge'
    fs_date: 'FSDate'
    fs_day: 'FSDay'
    fs_model: 'FSModel'
    fs_month: 'FSMonth'
    fs_year: 'FSYear'
    fs_directory: 'FSDirectory'


@dataclass
class ImageSize:
    """
    ImageSize dataclass

    """
    desc: str
    num: str
    val: str


@dataclass
class Megapixels:
    """
    Megapixels dataclass

    """
    desc: str
    num: float
    val: float


@dataclass
class BaseName:
    """
    BaseName dataclass

    """
    desc: str
    val: str


@dataclass
class FSMIMEType:
    """
    FSMIMEType dataclass

    """
    desc: str
    val: str


@dataclass
class FileExtension:
    """
    FileExtension dataclass

    """
    desc: str
    val: str


@dataclass
class FileTypeDescription:
    """
    FileTypeDescription dataclass

    """
    desc: str
    val: str


@dataclass
class IsOriginal:
    """
    IsOriginal dataclass

    """
    desc: str
    val: bool


@dataclass
class LongEdge:
    """
    LongEdge dataclass

    """
    desc: str
    val: int


@dataclass
class ParentFolder:
    """
    ParentFolder dataclass

    """
    desc: str
    val: str


@dataclass
class ShortEdge:
    """
    ShortEdge dataclass

    """
    desc: str
    val: int


@dataclass
class FSDate:
    """
    FSDate dataclass

    """
    desc: str
    val: str


@dataclass
class FSDay:
    """
    FSDay dataclass

    """
    desc: str
    val: int


@dataclass
class FSModel:
    """
    FSModel dataclass

    """
    desc: str
    val: str


@dataclass
class FSMonth:
    """
    FSMonth dataclass

    """
    desc: str
    val: Union[int, str]


@dataclass
class FSYear:
    """
    FSYear dataclass

    """
    desc: str
    val: int


@dataclass
class FSDirectory:
    """
    FSDirectory dataclass

    """
    desc: str
    val: str
