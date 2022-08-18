from dbconnector import Mongoatlas

# เชื่อมต่อกับ blind app database
foods_col = Mongoatlas(collection="foods")

def query_with_food_id(food_id_list: list):
    try:
        foods = foods_col.find({"food_id": {
            "$in": food_id_list
        }})["documents"]
        if len(foods) == 0:
            return {404: "Foods with these food_id is not available"}
        else:
            return {200: foods}
    except:
        return {520: "Fail to connnect Database"}
    
        