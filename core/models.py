from datetime import datetime
from bson import ObjectId
from django.conf import settings
from pymongo import MongoClient


class MongoModel:
    collection_name = None  # 상속받는 클래스에서 정의해야 함
    _client = None

    def __init__(self, **kwargs):
        self._id = kwargs.get('_id', ObjectId())
        self.created_at = kwargs.get('created_at', datetime.utcnow())
        
    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = MongoClient(settings.MONGODB_SETTINGS['url'])
        return cls._client

    @classmethod
    def get_collection(cls):
        client = cls.get_client()
        db = client[settings.MONGODB_SETTINGS['db_name']]
        return db[cls.collection_name]
    
    @classmethod
    def find_one(cls, filter_dict, projection=None):
        doc = cls.get_collection().find_one(filter_dict, projection)
        return cls(**doc) if doc else None
    
    @classmethod
    def find(cls, filter_dict=None):
        docs = cls.get_collection().find(filter_dict or {})
        return [cls(**doc) for doc in docs]
    
    def save(self):
        self.get_collection().update_one(
            {'_id': self._id},
            {'$set': self.to_dict()},
            upsert=True
        )
        return self
    
    def delete(self):
        self.get_collection().delete_one({'_id': self._id})
    
    def to_dict(self):
        return {
            '_id': str(self._id),
            'created_at': self.created_at.isoformat()
        }

# 예시 모델
class Item(MongoModel):
    collection_name = 'articles'
    
    def __init__(self, **kwargs):
        if '_id' in kwargs and not isinstance(kwargs['_id'], ObjectId):
            kwargs['_id'] = ObjectId(kwargs['_id'])
        super().__init__(**kwargs)
        self.articleId = kwargs.get('articleId', '')
        self.title = kwargs.get('title', '')
        self.url = kwargs.get('url', '')
        self.prologue = kwargs.get('prologue', '')
        
    @classmethod
    def find_by_custom_id(cls, custom_id_field, custom_id, fields=None):
        projection = None
        if fields:
            projection = {field: 1 for field in fields}
            if '_id' not in fields:
                projection['_id'] = 0
        
        return cls.find_one({custom_id_field: custom_id}, projection)
    
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'articleId': self.articleId,
            'title': self.title,
            'url': self.url,
            'prologue': self.prologue
        })
        return base_dict
