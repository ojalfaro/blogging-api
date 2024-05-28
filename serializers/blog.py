#one doc
def decodeBlog(doc) -> dict:
    return {
        "_id":str(doc["_id"]),
        "title":doc["title"],
        "sub_title":doc["sub_title"],
        "content":doc["content"],
        "athor":doc["athor"],
        "date":doc["date"]
    }

def decodeBlogs(docs) -> list:
    return [decodeBlog(doc) for doc in docs]