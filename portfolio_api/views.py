from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from portfolio_api.models import Portfolio 
from portfolio_api.serializer import PortfolioSerializer
from rest_framework.permissions import IsAuthenticated




        
class PortfolioList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.user)
        portfolios = Portfolio.objects.all();
        serializer = PortfolioSerializer(portfolios, many=True) 
        return Response(serializer.data)  

class PortfolioCreate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PortfolioSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PortfolioDetails(APIView):
    permission_classes = [IsAuthenticated]
    def get_portfolio_by_pk(self,request,pk):
        try:
            return Portfolio.objects.get(pk=pk)
        except:
            return Response({'error': 'Portfolio does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
        except:
            return Response({'error': 'Portfolio does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
        except:
            return Response({'error': 'Portfolio does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PortfolioSerializer(portfolio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
        except:
            return Response({'error': 'Portfolio does not exist'}, status=status.HTTP_404_NOT_FOUND)        
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
