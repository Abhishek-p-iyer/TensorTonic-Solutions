def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    best_model = max(models, key= lambda x: (x["accuracy"], -x["latency"], x["timestamp"]))
    return best_model["name"]
    
    