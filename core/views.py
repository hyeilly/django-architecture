from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from bson import ObjectId

def test_endpoint(request):
    return JsonResponse({'message': 'This is a test endpoint!'})

@api_view(['GET'])
def hello_world(request):
    return Response({
        "message": "Hello, World!12345",
        "status": "success"
    })

@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = Item.find()
        return Response([item.to_dict() for item in items])
    
    elif request.method == 'POST':
        item = Item(**request.data)
        item.save()
        return Response(item.to_dict(), status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, item_id):
    item = Item.find_one({'_id': ObjectId(item_id)})
    if not item:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(item.to_dict())
    
    elif request.method == 'PUT':
        for key, value in request.data.items():
            setattr(item, key, value)
        item.save()
        return Response(item.to_dict())
    
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_article_by_custom_id(request, custom_id):
    # 특정 필드만 가져오기
    fields = ['articleId', 'title', 'url', 'prologue']
    
    # articleId로 문서 찾기 (숫자는 문자열로 변환)
    article = Item.find_by_custom_id('articleId', int(52889), fields=fields)
    
    if not article:
        return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)
    
    return Response(article.to_dict())
