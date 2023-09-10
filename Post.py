#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
#-uvicorn Post:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: User

class Passenger(BaseModel):
    id: int
    Name: str
    Pclass: int
    Survived: int
    Sex: str
    Age: int
    SibSp: int
    Parch: int  

#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
passengers_list= [Passenger(id="1",Name="Owen Harris", Pclass="3", Survived=0, Sex="male", Age="22", SibSp="1", Parch="0"),
                  Passenger(id="2",Name="Laina", Pclass="3", Survived=0, Sex="female", Age="26", SibSp="0", Parch="0"),
                  Passenger(id="3",Name="James ", Pclass="3", Survived=0, Sex="male", Age="0", SibSp="0", Parch="0")]


#***Get
@app.get("/passengersclass/")
async def passengersclass():
    return (passengers_list) #http://127.0.0.1:8000/passengersclass/
 # En el explorador colocamos la raiz de la ip: 


#***Post
@app.post("/passengersclass/")
async def passengersclass(passenger:Passenger):

    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 

    for index, saved_passenger in enumerate(passengers_list):
        if saved_passenger.id == passenger.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el pasajero ya existe"}
    else:
        passengers_list.append(passenger)
        return passenger


#Actualizacion Put
@app.put("/passengersclass/")
async def passengersclass(passenger: Passenger):

    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 

    for index, saved_passenger in enumerate(passengers_list):
        if saved_passenger.id == passenger.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            passengers_list[index] = passenger
            found=True
    if not found:
            return {"error":"No se ha actualizado el usuario"}
    else:
            return passenger, {"respuesta":"El usuario se ha actualizado exitosamente!"}
#http://127.0.0.1:8000/passengersclass/


#Eliminar
@app.delete("/passengersclass/")
async def delete_passenger(passenger: Passenger):

    found=False 

    for index, saved_passenger in enumerate(passengers_list):
         if saved_passenger.id == passenger.id:
           del passengers_list[index]
           found = True
           break
    
    if not found:
         return {"error": "No existe"}
        
    return {"mensaje": "Usuario eliminado"}

#{"id":1,"Name":"Owen Harris", "Pclass":"3", "Survived":0, "Sex":"male", "Age":22, "SibSp":1, "Parch":0,}




#{"id":"25", "Name":"Danira", "Pclass":"3", "Survived":"0", "Sex":"male", "Age":"20", "SibSp":"3", "Parch":"1"} 