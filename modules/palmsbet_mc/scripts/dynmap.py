import yaml
import lib.utils.logging as log


def configure_dynmap(db_password:str, db_user, ip:str, port:str = "3306", db_name:str = "dynmap"):
     
    file_path = "modules/palmsbet_mc/server/plugins/dynmap/configuration.txt" 

    log.started("writing dynmap config")
    
    with open(file_path, "w+") as stream:
           
        
        data = {"storage": {}}
        storage_data = data["storage"]

        storage_data["type"] = "mysql"
        storage_data["hostname"] = ip
        storage_data["port"] = port
        storage_data["database"] = db_name
        storage_data["userid"] = db_user
        storage_data["password"] = db_password
        
        data["storage"] = storage_data
        
        stream.seek(0)
        print(data)
        yaml.dump(data, stream)
        
        log.success("successfully wrote dynmap config")



            
