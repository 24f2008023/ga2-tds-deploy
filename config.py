# ==========================================
# MASTER CONFIGURATION - FILLED WITH YOUR ASSIGNED VALUES
# ==========================================

# 1. Your IITM Email
EMAIL = "24f2008023@ds.study.iitm.ac.in"

# 2. Q1: CORS Allowed Origin
Q1_ALLOWED_ORIGIN = "https://dash-j5mluw.example.com"

# 3. Q2: OAuth JWKS (Issuer, Audience, and Public Key)
ISSUER = "https://idp.exam.local"
AUDIENCE = "tds-qvri8ssr.apps.exam.local"
PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2okOHspNjgA+2rTLbeuY
cxiP/hG8C6Sb9iwg3yiLAA4HCnpITcbWCSelbvbYGuc3EbNy4xFyf5Cbj5DHJMID
EkryOgyd2giIIIBOUBj8S63uGcnRpOBh9NFatfNwheKuzsPuVNldu6A9cNteNpXc
WyJjG2axVfmq7i6SuKr1JoWYG7xTTAvKPujSl4OtsQfO3h5NepzdfXpr28oNnzfW
ed+zclR6BcmNNo/WVfJ4xyCLSf0BCOgdTgW6PdaChd1l9VDetJZVEgC5tkyvXsfI
SI6iyrYbKR0NEBSqq4XkadEjsCs4F1RncsS4LlgniT7GlkL9Mce3b0wGLs9/7ZIX
dQIDAQAB
-----END PUBLIC KEY-----"""

# 4. Q3: 12-Factor Config
# Precedence per key (lowest -> highest): defaults -> YAML -> .env -> OS env
# port:      defaults=8000, yaml=8923, .env=(unset), OS=8895        -> 8895
# workers:   defaults=1,    yaml=3,    .env(NUM_WORKERS)=4, OS=11   -> 11
# debug:     defaults=False,yaml=(unset), .env=False, OS=True       -> True
# log_level: defaults=info, yaml=(unset), .env=(unset), OS=warning  -> "warning"
Q3_PORT = 8895
Q3_WORKERS = 11
Q3_DEBUG = True
Q3_LOG_LEVEL = "warning"

# 5. Q5: Analytics API key
Q5_API_KEY = "ak_wqgly6cacgnwjnahp4pm9h7h"

# 6. Q9: Idempotency & Rate Limit
Q9_TOTAL_ORDERS = 48
Q9_RATE_LIMIT = 16

# 7. Q10: Middleware Rate Limit
Q10_ALLOWED_ORIGIN = "https://app-rts06l.example.com"
Q10_RATE_LIMIT = 12

# ==========================================
# FIXED VARIABLES (Do not change these)
# ==========================================
EXAM_PORTAL_ORIGIN = "https://exam.sanand.workers.dev"
