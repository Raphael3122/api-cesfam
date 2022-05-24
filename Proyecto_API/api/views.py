from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Medicamento, Registro, Usuario, InsumoMedico
import json

# Create your views here.

##  Esta primera parte es el servicio para registro prescripciones

class RegisterView(View):

    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)

# Listar registros

    def get(self,request,id=0):
        if(id>0):
            register=list(Registro.objects.filter(id=id).values())
            if len(register)>0:
                registro=register[0]
                datos={'message':"prescripciones encontrada",'registro':registro}
            else:
                datos={'message':"Prescripciones no encontrada...",}
            return JsonResponse(datos)
        else:

            register=list(Registro.objects.values())
            if len(register)>0:
                datos={'message':"prescripciones encontradas",'registro':register}
            else:
                datos={'message':"Prescripciones no encontrada...",}
            return JsonResponse(datos)
        

#   Registro

    def post(self,request): 
        print(request.body)
        jd=json.loads(request.body)
        print(jd)
        Registro.objects.create(paciente=jd['paciente'],prescripcion=jd['prescripcion'],fecha_venc=jd['fecha_venc'])
        datos={'message':"Prescripcion registrada correctamente"}
        return JsonResponse(datos)

#   modificar

    def put(self,request,id):
        jd=json.loads(request.body)
        register=list(Registro.objects.filter(id=id).values())
        if len(register)>0:
            registro=Registro.objects.get(id=id)
            registro.paciente=jd['paciente']
            registro.prescripcion=jd['prescripcion']
            registro.fecha_venc=jd['fecha_venc']
            registro.save()
            datos={'message':"Prescripcion modificada correctamente"}
        else:
            datos={'message':"Prescripcion no encontrada..."}
        return JsonResponse(datos)


#   eliminar

    def delete(self,request, id):
        register=list(Registro.objects.filter(id=id).values())
        
        if len(register)>0:
            Registro.objects.filter(id=id).delete()
            datos={'message':"Prescripcion eliminada"}
        else:
            datos={'message':"Prescripcion no encontrada..."}
        return JsonResponse(datos)


##        ------------------ MEDICAMENTO   ----------------------------      


class MedicamentoView(View):

    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)

    # Listar
    def get(self,request,codigo=''):
        if(len(codigo) > 0):
            medicamento = list(Medicamento.objects.filter(codigo=codigo).values())
            if len(medicamento)>0:
                medicamen =medicamento[0]
                datos = {'message':"Medicamento encontrado",'medicamento':medicamen}
            else:
                datos={'message':"Medicamento no encontrado..."}
            return JsonResponse(datos)
        else:
            medicamento = list(Medicamento.objects.values())
            if len(medicamento)>0:
                datos={'message':"Medicamento encontrado",'medicamento':medicamento}
            else:
                datos={'message':"Medicamento no encontrado..."}
            return JsonResponse(datos)

    # Registro

    def post(self,request):
        jd=json.loads(request.body)
        Medicamento.objects.create(codigo=jd['codigo'],remedio=jd['remedio'],fabricante=jd['fabricante'],contenido=jd['contenido'],cantidad=jd['cantidad'],gramaje=jd['gramaje'],caducidad=jd['caducidad'])
        datos={'message':"Medicamento ingresado correctamente"}
        return JsonResponse(datos)


    #Actualizar

    def put(self,request,codigo):
        jd=json.loads(request.body)
        medicamento = list(Medicamento.objects.filter(codigo=codigo).values())
        if len(medicamento)>0:
            medicamento=Medicamento.objects.get(codigo=codigo)
            medicamento.codigo=jd['codigo']
            medicamento.remedio=jd['remedio']
            medicamento.fabricante=jd['fabricante']
            medicamento.contenido=jd['contenido']
            medicamento.cantidad=jd['cantidad']
            medicamento.gramaje=jd['gramaje']
            medicamento.caducidad=jd['caducidad']
            medicamento.save()
            datos={'message':"Medicamento modificado"}
        else:
            datos={'message':"Medicamento no encontrado..."}
        return JsonResponse(datos)


    def delete(self,request,codigo):
        medicamento = list(Medicamento.objects.filter(codigo=codigo).values())
        if len(medicamento)>0:
            Medicamento.objects.filter(codigo=codigo).delete()
            datos={'message':"Medicamento eliminado"}
        else:
            datos={'message':"Medicamento no encontrado..."}
        
        return JsonResponse(datos)


##        ------------------ USUARIO   ----------------------------   

class UsuarioView(View):
    def get(self,request,  correo='', password=''):
        if(len(correo)>0):
            usuario=list(Usuario.objects.filter(correo=correo).values())
            if len(usuario)>0:
                usuario=usuario[0]
                datos={'message':"Listado de usuario",'usuario':usuario}
            else:
                
                datos={'message':"Usuario no encontrado..."}
            
        if(len(password)>0):
            usuario=list(Usuario.objects.filter(password=password).values())
            if len(password)>0:
                usuario=usuario[0]
                datos={'message':"Listado de usuario",'usuario':usuario}
            else:            
               datos={'message':"Usuario no encontrado..."}
            return JsonResponse(datos)
            

            
        else:

            usuario=list(Usuario.objects.values())
            if len(usuario)>0:
                datos={'message':"Listado de usuario",'usuario':usuario}
            else:
                datos={'message':"Usuario no encontrado..."}
            return JsonResponse(datos)
    
    


##        ------------------ Insumo medico   ----------------------------   

class InsumoView(View):

    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            insumomedico=list(InsumoMedico.objects.filter(id=id).values())
            
            if len(insumomedico)>0:
                insumomedico=insumomedico[0]
                datos={'message':"Listado insumo medico",'insumomedico':insumomedico}
            else:
                
                datos={'message':"Insumo medico no encontrado..."}
            return JsonResponse(datos)
        else:

            insumomedico=list(InsumoMedico.objects.values())
            if len(insumomedico)>0:
                datos={'message':"Listado insumo medico",'insumomedico':insumomedico}
            else:
                datos={'message':"Insumo medico no encontrado..."}
            return JsonResponse(datos)



    def post(self,request):
        jd=json.loads(request.body)
        InsumoMedico.objects.create(insumo=jd['insumo'],cantidad=jd['cantidad'],descripcion=jd['descripcion'])
        datos={'message':"Insumo medico ingresado correctamente"}
        return JsonResponse(datos)


    def put(self,request, id):
        
        jd=json.loads(request.body)
        insumomedico=list(InsumoMedico.objects.filter(id=id).values())
            
        if len(insumomedico)>0:
            insumomedico=InsumoMedico.objects.get(id=id)
            insumomedico.insumo=jd['insumo']
            insumomedico.cantidad=jd['cantidad']
            insumomedico.descripcion=jd['descripcion']
            insumomedico.save()
            datos={'message':"Insumo medico modificado correctamente"}
        else:
            datos={'message':"Insumo medico no encontrado.."}
        return JsonResponse(datos)


    def delete(self,request,id):
        insumomedico=list(InsumoMedico.objects.filter(id=id).values())
        
        if len(insumomedico)>0:
            InsumoMedico.objects.filter(id=id).delete()
            datos={'message':"Insumo medico borrado correctamente"}
        else:
            datos={'message':"Insumo medico no encontrado..."}
        return JsonResponse(datos)
