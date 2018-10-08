from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from .get_xml import GetDataXml
from . import serializers
import pdb
from rest_framework.response import Response


# from rest_framework.views import APIView



xml_class = GetDataXml()
coins_class = xml_class.create_dict_obj()


def get_next_task_id():
    return max(coins_class) + 1


class SearchCoinsViewSet(viewsets.ViewSet):

    #pdb.set_trace()

    queryset = coins_class
    serializer = serializers.CoinSerializer


    def retrieve(self, request, *args, **kwargs):
        #pdb.set_trace()
        coin_name = self.kwargs['coin_name']
        match = {k:v for k,v in coins_class.items() if v.name == coin_name}




        serializer = serializers.CoinSerializer(list(match.values())[0])
        return Response(serializer.data)



    



    # def get(self, request):

    #     xml_class = GetDataXml()
    #     #import pdb; pdb.set_trace()
    #     coins_class = xml_class.create_dict_obj()
        

    #     keys = coins_class.keys()

    #         # obj = coins_class[k]
    #         # if obj.name = 





class CoinViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.CoinSerializer
    # import pdb; pdb.set_trace()

    def list(self, request):

        
        serializer = serializers.CoinSerializer(
            instance=coins_class.values(), many=True)


        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.CoinSerializer(data=request.data)
        
        if serializer.is_valid():
            task = serializer.save()
            task.id = get_next_task_id()
            coins_class[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        #pdb.set_trace()
        try:
            task = coins_class[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.CoinSerializer(instance=task)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            task = coins_class[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.CoinSerializer(
            data=request.data, instance=task)
        if serializer.is_valid():
            task = serializer.save()
            coins_class[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            task = coins_class[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.CoinSerializer(
            data=request.data,
            instance=task,
            partial=True)
        if serializer.is_valid():
            task = serializer.save()
            coins_class[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            task = coins_class[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        del coins_class[task.id]
        return Response(status=status.HTTP_204_NO_CONTENT)