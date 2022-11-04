import os

UPLOAD_FOLDER=os.environ.get("UPLOAD_FOLDER","../images")
PROFANITY_THRESHOLD=os.environ.get("PROFANITY_THRESHOLD", 0.8)
STEP_LIMIT=os.environ.get("STEP_LIMIT", 150)            # I think this is obsolete
AUTHOR_LIMIT=os.environ.get("AUTHOR_LIMIT", 100)        # I think this is obsolete
MONGODB_CONNECTION=os.environ.get("MONGODB_CONNECTION", "mongodb://localhost")
MAX_DREAM_OCCURENCE=os.environ.get("MAX_DREAM_OCCURENCE",20)
AUTH0_DOMAIN=os.environ.get("AUTH0_DOMAIN","dev-yqzsn326.auth0.com")
AUTH0_API_AUDIENCE=os.environ.get("AUTH0_API_AUDIENCE","https://api.feverdreams.app/")
BOT_USE_S3=os.environ.get("BOT_USE_S3",True)
BOT_S3_BUCKET=os.environ.get("BOT_S3_BUCKET","devimages.feverdreams.app")
BOT_S3_WEB=os.environ.get("BOT_S3_WEB","http://devimages.feverdreams.app.s3-website-us-east-1.amazonaws.com/images/")