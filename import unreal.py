# -*- coding: utf-8 -*-
"""
=========================================================
 UE5.5 Modular Texture Importer
 Config.py

 所有可修改配置统一放这里
=========================================================
"""

# ======================================================
# Source & Destination
# ======================================================

# 磁盘贴图目录
SOURCE_ROOT = r"E:\UEEEEEEEEEEEEEEEEEEEEEEEEEEEEE_FBX\OUT BOX\blender----fbx\model\fbx_modularization\new\s_f_7\tex"

# UE目标目录
DEST_ROOT = "/Game/out-box/out_material_modularization/ss7"

# 材质实例模板
MASTER_MATERIAL_INSTANCE = (
    "/Game/out-box/out_fbx_modularization/"
    "small_stuff_3/fountain/f_m/new/NewMaterial1.NewMaterial1"
)

# ======================================================
# 自动化开关
# ======================================================

AUTO_CREATE_FOLDER = True
AUTO_IMPORT_TEXTURE = True
AUTO_REIMPORT = True
AUTO_RENAME_TEXTURE = True
AUTO_FIX_TEXTURE = True
AUTO_COPY_MATERIAL_INSTANCE = True
AUTO_BIND_TEXTURE = True
AUTO_SAVE_ASSET = True
AUTO_GENERATE_REPORT = True
AUTO_GENERATE_MANIFEST = True
DRY_RUN = False

# ======================================================
# 支持导入格式
# ======================================================

SUPPORTED_EXTENSIONS = [
    ".png",
    ".tga",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".tif",
    ".tiff",
    ".exr",
    ".hdr",
]

# ======================================================
# 贴图关键字
# （全部小写）
# ======================================================

TEXTURE_KEYWORDS = {

    "BaseColor":[
        "basecolor",
        "base_color",
        "albedo",
        "diffuse",
        "color"
    ],

    "Normal":[
        "normal",
        "nrm",
        "nor"
    ],

    "ORM":[
        "orm",
        "rma"
    ],

    "AO":[
        "ao",
        "ambientocclusion"
    ],

    "Roughness":[
        "roughness",
        "rough"
    ],

    "Metallic":[
        "metallic",
        "metal"
    ],

    "Height":[
        "height",
        "displacement"
    ],

    "Opacity":[
        "opacity",
        "alpha"
    ],

    "Specular":[
        "specular",
        "spec"
    ],

    "Emissive":[
        "emissive",
        "emit"
    ],

    "Mask":[
        "mask"
    ]

}

# ======================================================
# 材质参数映射
# 左边 = 贴图类型
# 右边 = 材质实例参数
# ======================================================

TEXTURE_PARAMETER_MAP = {

    "BaseColor":"BaseColor",

    "Normal":"Normal",

    "ORM":"ORM",

    "AO":"AO",

    "Roughness":"Roughness",

    "Metallic":"Metallic",

    "Height":"Height",

    "Opacity":"Opacity",

    "Specular":"Specular",

    "Emissive":"Emissive",

    "Mask":"Mask"

}

# ======================================================
# Compression 设置
# ======================================================

TEXTURE_SETTINGS = {

    "BaseColor":{
        "sRGB":True,
        "Compression":"Default"
    },

    "Normal":{
        "sRGB":False,
        "Compression":"NormalMap"
    },

    "Default":{
        "sRGB":False,
        "Compression":"Masks"
    }

}

# ======================================================
# 命名前缀
# ======================================================

TEXTURE_PREFIX = "T_"

MATERIAL_INSTANCE_PREFIX = "MI_"

# ======================================================
# Manifest
# ======================================================

MANIFEST_NAME = "ImportManifest.json"

# ======================================================
# Log
# ======================================================

LOG_NAME = "ImportLog.txt"

PRINT_CONSOLE = True

PRINT_UE_LOG = True
# ======================================================
# Texture Import Settings
# ======================================================

OVERWRITE_EXISTING = True

REPLACE_EXISTING = True

SAVE_AFTER_IMPORT = True

CREATE_MISSING_FOLDER = True

AUTO_FIX_COMPRESSION = True

AUTO_FIX_SRGB = True

AUTO_ASSIGN_TEXTURE = True

AUTO_CREATE_MI = True
# ======================================================
# Material Instance Parameter Alias
# ======================================================

PARAMETER_ALIAS = {

    "BaseColor":[
        "BaseColor",
        "BC",
        "Diffuse",
        "Albedo"
    ],

    "Normal":[
        "Normal",
        "N",
        "NormalTex"
    ],

    "ORM":[
        "ORM",
        "RMA",
        "Masks"
    ],

    "AO":[
        "AO"
    ],

    "Roughness":[
        "Roughness"
    ],

    "Metallic":[
        "Metallic"
    ],

    "Height":[
        "Height",
        "Displacement"
    ],

    "Opacity":[
        "Opacity"
    ],

    "Specular":[
        "Specular"
    ],

    "Emissive":[
        "Emissive"
    ]

}
# -*- coding: utf-8 -*-

"""
=========================================================
UE5.5 Modular Importer

Logger.py

统一日志系统
=========================================================
"""

import os
import datetime

import Config

try:
    import unreal
    HAS_UNREAL = True
except:
    HAS_UNREAL = False


class Logger:

    def __init__(self):

        self.start_time = datetime.datetime.now()

        self.lines = []

        self.success = 0

        self.warning = 0

        self.error = 0


    def _write(self, level, message):

        now = datetime.datetime.now().strftime("%H:%M:%S")

        line = f"[{now}] [{level}] {message}"

        self.lines.append(line)

        if Config.PRINT_CONSOLE:

            print(line)

        if HAS_UNREAL and Config.PRINT_UE_LOG:

            if level == "ERROR":

                unreal.log_error(line)

            elif level == "WARNING":

                unreal.log_warning(line)

            else:

                unreal.log(line)


    def info(self, message):

        self.success += 1

        self._write("INFO", message)


    def warning(self, message):

        self.warning += 1

        self._write("WARNING", message)


    def error(self, message):

        self.error += 1

        self._write("ERROR", message)


    def save(self):

        folder = os.path.dirname(__file__)

        path = os.path.join(folder, Config.LOG_NAME)

        with open(path, "w", encoding="utf-8") as f:

            f.write("\n".join(self.lines))

            f.write("\n")

            f.write("=" * 60)

            f.write("\n")

            f.write(f"INFO : {self.success}\n")

            f.write(f"WARNING : {self.warning}\n")

            f.write(f"ERROR : {self.error}\n")

            f.write("=" * 60)

            f.write("\n")

            cost = datetime.datetime.now() - self.start_time

            f.write(f"Elapsed : {cost}\n")


logger = Logger()
# -*- coding: utf-8 -*-

"""
=========================================================
UE5.5 Modular Importer

Logger.py

统一日志系统
=========================================================
"""

import os
import datetime

import Config

try:
    import unreal
    HAS_UNREAL = True
except:
    HAS_UNREAL = False


class Logger:

    def __init__(self):

        self.start_time = datetime.datetime.now()

        self.lines = []

        self.success = 0

        self.warning = 0

        self.error = 0


    def _write(self, level, message):

        now = datetime.datetime.now().strftime("%H:%M:%S")

        line = f"[{now}] [{level}] {message}"

        self.lines.append(line)

        if Config.PRINT_CONSOLE:

            print(line)

        if HAS_UNREAL and Config.PRINT_UE_LOG:

            if level == "ERROR":

                unreal.log_error(line)

            elif level == "WARNING":

                unreal.log_warning(line)

            else:

                unreal.log(line)


    def info(self, message):

        self.success += 1

        self._write("INFO", message)


    def warning(self, message):

        self.warning += 1

        self._write("WARNING", message)


    def error(self, message):

        self.error += 1

        self._write("ERROR", message)


    def save(self):

        folder = os.path.dirname(__file__)

        path = os.path.join(folder, Config.LOG_NAME)

        with open(path, "w", encoding="utf-8") as f:

            f.write("\n".join(self.lines))

            f.write("\n")

            f.write("=" * 60)

            f.write("\n")

            f.write(f"INFO : {self.success}\n")

            f.write(f"WARNING : {self.warning}\n")

            f.write(f"ERROR : {self.error}\n")

            f.write("=" * 60)

            f.write("\n")

            cost = datetime.datetime.now() - self.start_time

            f.write(f"Elapsed : {cost}\n")


logger = Logger()
# ==========================================================
# Part 3
# Utils
# ==========================================================

import re
from pathlib import Path


# ----------------------------------------------------------
# 判断是否支持导入
# ----------------------------------------------------------

def is_supported_texture(file_path):

    suffix = Path(file_path).suffix.lower()

    return suffix in Config.SUPPORTED_EXTENSIONS


# ----------------------------------------------------------
# 获取文件名（无后缀）
# ----------------------------------------------------------

def get_filename(file_path):

    return Path(file_path).stem


# ----------------------------------------------------------
# 获取后缀
# ----------------------------------------------------------

def get_extension(file_path):

    return Path(file_path).suffix.lower()


# ----------------------------------------------------------
# 名称是否合法
# ----------------------------------------------------------

def sanitize_name(name):

    name = re.sub(r"[^\w]", "_", name)

    while "__" in name:

        name = name.replace("__", "_")

    return name.strip("_")


# ----------------------------------------------------------
# 自动增加T_
# ----------------------------------------------------------

def build_texture_name(name):

    name = sanitize_name(name)

    if not name.startswith(Config.TEXTURE_PREFIX):

        name = Config.TEXTURE_PREFIX + name

    return name


# ----------------------------------------------------------
# 自动生成MI名字
# ----------------------------------------------------------

def build_material_instance_name(folder_name):

    return f"{Config.MATERIAL_INSTANCE_PREFIX}{folder_name}"


# ----------------------------------------------------------
# 判断贴图类型
# 返回：
# BaseColor
# Normal
# ORM
# AO
# ...
# ----------------------------------------------------------

def detect_texture_type(filename):

    lower = filename.lower()

    for tex_type, keywords in Config.TEXTURE_KEYWORDS.items():

        for keyword in keywords:

            if keyword in lower:

                return tex_type

    return "Default"


# ----------------------------------------------------------
# 是否BaseColor
# ----------------------------------------------------------

def is_basecolor(filename):

    return detect_texture_type(filename) == "BaseColor"


# ----------------------------------------------------------
# 是否Normal
# ----------------------------------------------------------

def is_normal(filename):

    return detect_texture_type(filename) == "Normal"


# ----------------------------------------------------------
# 获取Compression配置
# ----------------------------------------------------------

def get_texture_setting(texture_type):

    if texture_type in Config.TEXTURE_SETTINGS:

        return Config.TEXTURE_SETTINGS[texture_type]

    return Config.TEXTURE_SETTINGS["Default"]


# ----------------------------------------------------------
# Windows路径转UE路径
# ----------------------------------------------------------

def build_ue_path(relative_folder):

    relative_folder = relative_folder.replace("\\", "/")

    if relative_folder == ".":

        return Config.DEST_ROOT

    return Config.DEST_ROOT + "/" + relative_folder


# ----------------------------------------------------------
# 扫描磁盘所有贴图
# 返回：
# [
#     (完整路径, 相对目录),
# ]
# ----------------------------------------------------------

def scan_all_textures():

    result = []

    source = Path(Config.SOURCE_ROOT)

    if not source.exists():

        logger.error(f"Source Not Found : {source}")

        return result

    for file in source.rglob("*"):

        if file.is_file():

            if not is_supported_texture(str(file)):

                continue

            relative = file.parent.relative_to(source)

            result.append(

                (

                    str(file),

                    str(relative)

                )

            )

    logger.info(f"Scan Finished : {len(result)} Texture(s)")

    return result


# ----------------------------------------------------------
# 输出扫描结果
# ----------------------------------------------------------

def print_scan_result():

    textures = scan_all_textures()

    print()

    print("=" * 60)

    print("Texture Scan Result")

    print("=" * 60)

    for tex, folder in textures:

        print(folder)

        print("   ", tex)

    print("=" * 60)

    print(f"Total : {len(textures)}")

    print("=" * 60)