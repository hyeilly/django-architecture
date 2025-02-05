from pymongo import MongoClient
import os

class PyMongoConnection:
    def __init__(self):
        """pymongo 연결 정보 초기화"""
        self.client = None
        self.db = None
        self.mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        self.db_name = os.getenv("MONGO_DB_NAME", "mydatabase")

    def __enter__(self):
        """with 문에서 pymongo 연결"""
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]
        print("✅ [pymongo] MongoDB 연결 성공")
        return self  # pymongo 인스턴스를 반환하여 사용 가능

    def __exit__(self, exc_type, exc_value, traceback):
        """with 문에서 pymongo 연결 해제"""
        if self.client:
            self.client.close()
            self.client = None
            self.db = None
            print("❌ [pymongo] MongoDB 연결 종료")

    def get_database(self):
        """데이터베이스 객체 반환"""
        return self.db

    def get_collection(self, collection_name):
        """컬렉션 객체 반환"""
        return self.db[collection_name] if self.db else None
