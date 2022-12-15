#!/usr/bin/env python3
import base64
import zlib
import marshal

stages = [
        #(lambda x: f"exec(__import__('marshal').loads({x}))", lambda x: marshal.dumps(compile(x, "", "exec", optimize=2))),
        (lambda x: f"eval({x})", lambda x: x),
        (lambda x: f"__import__('zlib').decompress({x})", lambda x: zlib.compress(x.encode('ascii'), 9)),
        (lambda x: f"__import__('base64').a85decode({x})",lambda x: base64.a85encode(x.encode('ascii'))),
        (lambda x: f"eval({x})", lambda x: x),
        ]


with open(f"runfromvenv.py", "rb") as f:
    code = f.read()
    print(f"init: {len(code)}")

for stage in stages:
    code = stage[0](stage[1](code))

print(f"after: {len(code)}")
print(code)
eval(code)


exit()

payload = zlib.compress(marshal.dumps(compile(code, "runfromvenv", "exec", optimize=2)), 9)
stage2 = marshal.dumps(compile(f"exec(__import__('marshal').loads(__import__('zlib').decompress({payload})))", "2", "eval", optimize=2))
stage1 = marshal.dumps(compile(f"exec(__import__('marshal').loads(__import__('base64').a85decode({base64.a85encode(stage2)})))", "1", "eval", optimize=2))

print(f"size: {len(str(payload))} -> {len(str(stage1))}")
cmd = f"exec(__import__('marshal').loads({str(stage1)}))"
print(cmd)
eval(cmd)
