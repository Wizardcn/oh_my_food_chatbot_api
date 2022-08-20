def knowledge_serializer(knowledge) -> dict:
    
    return {
        "topic": str(knowledge["topic"]),
        "criterion": str(knowledge["criterion"]),
        "sub-topic": str(knowledge["sub-topic"]),
        "food_list": list(knowledge["food_list"])
    }
    

def knowledges_serializer(knowledges) -> list:
    return [knowledge_serializer(knowledge) for knowledge in knowledges]