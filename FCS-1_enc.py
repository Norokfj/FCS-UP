# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))