import os


configs = {
    "URL": "https://randomuser.me/api/?results=5",
    "bucket":{
        "name": "de04-demo",
        "raw":"cadastro/raw/",
        "work":"cadastro/logs/",
        "logs": "cadastro/work/"    
    } ,
    "metadados":{
        "nome_original": [
            "gender",
            "name.title",
            "name.first",
            "name.last",
            "location.city",
            "location.state",
            "location.country",
            "email",
            "dob.date"
            ],
         "nome": [
            "sexo",
            "titulo",
            "nome",
            "sobrenome",
            "cidade",
            "estado",
            "pais",
            "email",
            "data_nascimento"
         ],
         "tipos":{
             "sexo": "string",
             "titulo": "string",
             "nome": "string",
             "sobrenome": "string",
             "estado": "string",
             "pais": "string",
             "email": "string",
             "data_nascimento": "date"
         }
    }
}