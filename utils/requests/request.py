from utils.configs.config import TEMP_DIR_PATH


class Request:
    def __init__(self, token):
        self.token = token
        print(token)

    def get_document_minio_path(self):
        return f"/document_{self.token.token}.jpg"

    def get_selfie_minio_path(self):
        return f"selfie_{self.token.token}.jpg"

    def get_document_local_path(self):
        return f"{TEMP_DIR_PATH}/document_{self.token.token}.jpg"

    def get_selfie_local_path(self):
        return f"{TEMP_DIR_PATH}/selfie_{self.token.token}.jpg"
