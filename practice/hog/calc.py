import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

