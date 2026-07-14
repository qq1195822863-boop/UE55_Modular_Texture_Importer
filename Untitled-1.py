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