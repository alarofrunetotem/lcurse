from PyQt5 import Qt

WOW_FOLDER_KEY = "WowFolder"
WOW_TOC_KEY = "CurrentToc"
WOW_VERSION_KEY = "version"
WOW_FOLDER_DEFAULT = "{}/.wine/drive_c/Program Files (x86)/World of Warcraft".format(Qt.QDir.homePath())

LCURSE_FOLDER = "{}/.lcurse".format(Qt.QDir.homePath())
LCURSE_MAXTHREADS_KEY = "MaxThreads"
LCURSE_MAXTHREADS_DEFAULT = 50
LCURSE_DBVERSION = 1
TOC = "80200"
TOC_CLASSIC = "11302"

LCURSE_ADDONS = ''
LCURSE_ADDON_CATALOG = ''
LCURSE_ADDON_TOCS_CACHE = ''
LCURSE_PREFIX = ''
CURSE_URL='http://www.curseforge.com/wow'


def ApplyWowVersion():
    settings=Qt.QSettings()
    global LCURSE_ADDON_CATALOG
    global LCURSE_ADDONS
    global LCURSE_ADDON_TOCS_CACHE
    global LCURSE_PREFIX
#    global WOW_VERSION_KEY
    version=settings.value(WOW_VERSION_KEY)
    if not version:
        version='Retail'
    settings.beginGroup(version)
    prefix=settings.value('path')
    if not prefix:
        raise RuntimeError('Unable to get a prefix')
    settings.endGroup()
    LCURSE_PREFIX= LCURSE_FOLDER +  prefix
    LCURSE_ADDONS = LCURSE_PREFIX + "/addons.json"
    LCURSE_ADDON_CATALOG = LCURSE_PREFIX + "/addon-catalog.json"
    LCURSE_ADDON_TOCS_CACHE = LCURSE_PREFIX + "/tocs.json"
    return version


# with open(toc, encoding="utf8", errors='replace') as f:
#     line = f.readline()
#     while line != "":
#         print(line)
# sys.exit(42)
