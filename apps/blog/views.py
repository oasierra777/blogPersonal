from django.db.models.query_utils import Q
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
        
        if Post.postsobjects.all().exists():
            
            posts = Post.postsobjects.all()
            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(posts, request)
            serializer = PostListSerializer(posts, many=True)
            
            return paginator.get_paginated_response({'posts':serializer.data})
        else:
            return Response({'error':'No posts found'}, status=status.HTTP_404_NOT_FOUND)

class ListPostsByCategoryView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        
        if Post.postsobjects.all().exists():
            
            slug = request.query_params.get('slug')
            category = Category.objects.get(slug=slug)
            posts = Post.postsobjects.order_by('-published').all()
            
            #Filtrar cuando la categoría es el mismo padre
            if Category.objects.filter(parent=category).exists():
                posts = posts.filter(category=category)
            #Si la categoría tiene hijos, se filtra por la categoría padre y sus hijos
            else:
                sub_categories = Category.postsobjects.filter(parent=category)
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

class PostDetailView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, slug, format=None):
        
        if Post.postsobjects.filter(slug=slug).exists():
            
            post = Post.postsobjects.get(slug=slug)
            serializer = PostSerializer(post)
            #HTTP_X_FORWARDED_FOR nos permite obtener información del buscador
            address = request.META.get('HTTP_X_FORWARDED_FOR')
            if address:
                ip = address.split(',')[-1].strip()
            else:
                ip = request.META.get('REMOTE_ADDR')
            
            if not ViewCount.postsobjects.filter(post=post, ip_address=ip):
                view = ViewCount(post=post, ip_address=ip)
                view.save()
                post.views += 1
                post.save()
                
            return Response({'post':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Post doesnt exist'}, status=status.HTTP_404_NOT_FOUND)

class SearchBlogView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        
        search_term = request.query_params.get('s')
        matches = Post.postsobjects.filter(
                                        Q(title__icontains=search_term) |
                                        Q(descriptions__icontains=search_term) |
                                        Q(content__icontains=search_term) |
                                        Q(category__name__icontains=search_term)
                                    )
        paginator = SmallSetPagination()
        results = paginator.paginate_queryset(matches, request)
        serializer = PostListSerializer(matches, many=True)
        return paginator.get_paginated_response({'filtered_posts':serializer.data})
