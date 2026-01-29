import os
from fasalguru.app import create_app

PORT = int(os.environ.get("PORT", 4000))
app = create_app()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
