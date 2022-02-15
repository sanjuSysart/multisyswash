import os
from re import S
import sys

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from.models import User,ServiceDetails,ClothDetails,PriceDetails,AccountDetails,PlantDetails
from.serializer import UserSerializer,ServiceSerializer,ClothSerializer,PriceSerializer,AccountSerializer,PlantSerializer

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(request.user)
        content = {'message': 'Hello, World!'}
        return Response(content)

class SignupView(generics.CreateAPIView):
    
    queryset=User.objects.all()
    serializer_class=UserSerializer


class Services(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class=ServiceSerializer
    def post(self,request):           
        try:
            print(request.user)
            data = self.request.data
            ServiceName = data['serviceName']
            ServiceCode = data['serviceCode']

            if (ServiceName == '') | (ServiceCode == ''):
                return Response({'error': 'Please Fill all fields'})
            elif ServiceDetails.objects.filter(user=request.user,serviceName = ServiceName, trash = 0).exists(): 
                return Response({'error': 'Service Name already exists'})
            elif ServiceDetails.objects.filter(user=request.user,serviceCode = ServiceCode, trash = 0).exists(): 
                return Response({'error': 'Service Code already exists'})
            else:
                service_details = ServiceDetails(serviceName = ServiceName, serviceCode = ServiceCode,user=request.user)
                service_details.save()
                return Response({'data': ServiceName, 'Message': 'Success', })

        except Exception as e:
            print(str(e))
            exc_type, exc_obj, exc_tb = sys.exc_info
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
    def get(self, request, ser_id = None):
            
        if ser_id:
            try:
                queryset = ServiceDetails.objects.get(serviceId = ser_id, trash = False,user=request.user)
            except ServiceDetails.DoesNotExist:
                return Response({'data': ser_id, 'Message': 'Service does not exist',})

            read_serializer = ServiceSerializer(queryset)
         
        else:
            queryset = ServiceDetails.objects.filter(trash = False,user=request.user)

            read_serializer = ServiceSerializer(queryset, many = True)

        return Response(read_serializer.data)



#Add cloth

class ClothData(APIView):
    permission_classes = (IsAuthenticated,)                  
    serializer_class=ClothSerializer
    def post(self, request, format = None):
  
        try:

            data = self.request.data
            ClothName = data['clothName']
            ClothCode = data['clothCode']
            clothImg = data['clothImg']
            ClothNameArabic = data['clothNameArabic']

            if (ClothName == '') | (ClothCode == ''):
                return Response({'error': 'Please Fill all fields'})
            elif ClothDetails.objects.filter(user=request.user,clothName = ClothName, trash = False,).exists(): 
                return Response({'error': 'Cloth Name already exists'})
            elif ClothDetails.objects.filter(user=request.user,clothCode = ClothCode, trash = False).exists(): 
                return Response({'error': 'Cloth Code already exists'})
            else:
               cloth_details = ClothDetails(user=request.user,clothName = ClothName, clothCode = ClothCode, clothImg = clothImg,clothNameArabic = ClothNameArabic)
               cloth_details.save()
               return Response({'data': ClothName, 'Message': 'Success', })

        except Exception as e:
            print(str(e))
            exc_type, exc_obj, exc_tb = sys.exc_info
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)


# View All cloths and view By Cloth Name'

    def get(self, request, cloth_id = None):
        # clothPermmission(request)
        if cloth_id:
            try:
                queryset = ClothDetails.objects.get(clothId = cloth_id, trash = False,user=request.user,)
            except ClothDetails.DoesNotExist:
                return Response({'data': cloth_id, 'Message': 'Cloth does not exist', })
            
            read_serializer = ClothSerializer(queryset)
        else:
            queryset = ClothDetails.objects.filter(user=request.user,trash = False)
            read_serializer = ClothSerializer(queryset, many = True)
            # Clothdata = []
            # for i in range(len(read_serializer.data)):
            #    ClothName = read_serializer.data[i]['clothName']
            #    querySet1 = PriceDetails.objects.filter(clothType = ClothName, trash = False)
            #    serializer1 = PriceSerializer(querySet1, many = True)  
            #    data = [] 
            #    Clothdata.append({'data':read_serializer.data[i],'priceAndService': data})
            #    for j in range(len(serializer1.data)):
            #        ServiceName = serializer1.data[j]['serviceName']
            #     #    print(ServiceName)
            #        querySet2 = ServiceDetails.objects.filter(serviceName = ServiceName, trash = False)
            #        serializer2 = ServiceSerializer(querySet2, many = True)
            #        for k in range(len(serializer2.data)):
            #            ServiceCode = serializer2.data[k]['serviceCode']
            #         #    print(ServiceCode)
            #        Price = serializer1.data[j]['price']
            #        Xprice = serializer1.data[j]['xprice']
            #        a = {'ClothName': ClothName,'ServiceCode': ServiceCode, 'Price': Price, 'Xprice': Xprice}
            #        data.append(a)                   
            # return Response(Clothdata)
        return Response(read_serializer.data)



# Add Price

class PriceData(APIView):
    # permission_classes = (IsAuthenticated,)                  
    # permission_classes = (permissions.AllowAny,)
    def post(self, request, format = None):
        # pricePermmission(request)
        try:
            data = self.request.data
            ServiceName = data['serviceName']
            ClothType = data['clothType']
            price = data['price']
            xprice = data['xprice']
            

            if (ServiceName == '') | (ClothType == '') | (price == '') | (xprice == ''):
                return Response({'error': 'Please Fill all fields'})
            elif PriceDetails.objects.filter(serviceName = ServiceName,user=request.user, clothType = ClothType, trash = 0).exists():
                return Response({'error': 'This service with cloth already exists',})
            else:
               price_details = PriceDetails(serviceName = ServiceName, clothType = ClothType, price = price, xprice = xprice,user=request.user )
               price_details.save()
               return Response({'data': ClothType, 'Message': 'Success', })

        except Exception as e:
            print(str(e))
            exc_type, exc_obj, exc_tb = sys.exc_info
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)


    # View All Price and View Price by Id

    def get(self, request, price_id = None):
        # pricePermmission(request)
        if price_id:
            try:
                queryset = PriceDetails.objects.get(user=request.user,priceId = price_id, trash = False)
                
            except PriceDetails.DoesNotExist:
                return Response({'data': price_id, 'Message': 'Price does not exist'})

            read_serializer = PriceSerializer(queryset)
            
        else:
            queryset = PriceDetails.objects.filter(user=request.user,trash = False)
            read_serializer = PriceSerializer(queryset, many = True)
            
        
        return Response(read_serializer.data)



#Add Account type

class AccountData(APIView):
    permission_classes = (IsAuthenticated,) 
    serializer_class=AccountSerializer                 
    # permission_classes = (permissions.AllowAny,)
    def post(self, request, format = None):
        # accountTypePermmission(request)
        try:
            data = self.request.data
            AcTypeName = data['acTypeName']

            if (AcTypeName == ''):
                return Response({'error': 'Please Fill all fields'})
            elif AccountDetails.objects.filter(acTypeName = AcTypeName, trash = False,user=request.user).exists(): 
                return Response({'error': 'Account Type Name already exists'})
            else:
               account_details = AccountDetails(acTypeName = AcTypeName,user=request.user)
               account_details.save()
               return Response({'data': AcTypeName, 'Message': 'Success', })

        except Exception as e:
            print(str(e))
            exc_type, exc_obj, exc_tb = sys.exc_info
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
    
    # View All Account Type and View Account Type by Id

    def get(self, request, ac_type_id = None):
        # accountTypePermmission(request)
        if ac_type_id:
            try:
                queryset = AccountDetails.objects.get(acTypeId = ac_type_id, trash = False,user=request.user)
            except AccountDetails.DoesNotExist:
                return Response({'data': ac_type_id, 'Message': 'Account does not exist',})

            read_serializer = AccountSerializer(queryset)
            
        else:
            queryset = AccountDetails.objects.filter(user=request.user,trash = False)

            read_serializer = AccountSerializer(queryset, many = True)

        return Response(read_serializer.data)




# Add Plant

class PlantData(APIView):
    permission_classes = (IsAuthenticated,)    
    serializer_class=PlantSerializer              
    # permission_classes = (permissions.AllowAny,)
    def post(self, request, format = None):
        # plantPermmission(request)
        try:
            data = self.request.data
            PlantName = data['plantName']
            Location = data['location']
            ClothType = data['clothType']
            ContactName = data['contactName']
            ContactNumber = data['contactNumber']
            
            
            if (PlantName == '') | (Location == '') | (ClothType == ''):
                return Response({'error': 'Please Fill all fields'})
            
            else:
               plant_details = PlantDetails(plantName = PlantName, location = Location, clothType = ClothType, contactName = ContactName, contactNumber = ContactNumber,user=request.user)
               plant_details.save()
               return Response({'data': PlantName, 'Message': 'Success',})

        except Exception as e:
            print(str(e))
            exc_type, exc_obj, exc_tb = sys.exc_info
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

    # View Plant and View by Plant id

    def get(self, request, plant_id = None):
        # plantPermmission(request)
        if plant_id:
            try:
                queryset = PlantDetails.objects.get(user=request.user,plantId = plant_id, trash = False)
                
            except PlantDetails.DoesNotExist:
                return Response({'data': plant_id, 'Message': 'Plant does not exist',})

            read_serializer = PlantSerializer(queryset)
            
        else:
            queryset = PlantDetails.objects.filter(user=request.user,trash = False)
            read_serializer = PlantSerializer(queryset, many = True)
            return Response({'data':read_serializer.data})
        return Response({'data':read_serializer.data})








