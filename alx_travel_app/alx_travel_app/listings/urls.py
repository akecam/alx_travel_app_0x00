from django.urls import path
from django.http import JsonResponse

# Sample view for testing
def test_view(request):
    return JsonResponse({'message': 'Listings API is working!'})

urlpatterns = [
    path('', test_view),  # Accessible at /api/
]

