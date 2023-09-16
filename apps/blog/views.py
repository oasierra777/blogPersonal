from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.blog.models import Post
from apps.blog.models import ViewCount
from apps.blog.pagination import LargeSetPagination
from apps.blog.pagination import MediumSetPagination
from apps.blog.pagination import SmallSetPagination
from apps.blog.serializers import PostListSerializer
from apps.blog.serializers import PostSerializer
from apps.category.models import Category

class BlogListView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        
        if Post.objects.all().exists():
            
            posts = Post.objects.all()
            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(posts, request)
            serializer = PostListSerializer(posts, many=True)
            
            return paginator.get_paginated_response({'posts':serializer.data})
        else:
            return Response({'error':'No posts found'}, status=status.HTTP_404_NOT_FOUND)

class ListPostsByCategoryView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        
        if Post.objects.all().exists():
            
            slug = request.query_params.get('slug')
            category = Category.objects.get(slug=slug)
            posts = Post.objects.order_by('-published').all()
            
            #Filtrar cuando la categoría es el mismo padre
            if Category.objects.filter(parent=category).exists():
                posts = posts.filter(category=category)
            #Si la categoría tiene hijos, se filtra por la categoría padre y sus hijos
            else:
                sub_categories = Category.objects.filter(parent=category)
                filtered_categories = [category]
                
                for cat in sub_categories:
                    filtered_categories.append[cat]
                    
                filtered_categories = tuple(filtered_categories)
                posts = posts.filter(category__in=filtered_categories)
            
            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(posts, request)
            serializer = PostListSerializer(results, many=True)
            
            return paginator.get_paginated_response({'posts':serializer.data})
        else:
            return Response({'error':'No posts found'}, status=status.HTTP_404_NOT_FOUND)