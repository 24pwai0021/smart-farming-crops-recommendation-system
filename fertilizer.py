def get_fertilizer(crop):

    fertilizers = {
        "rice": "Urea",
        "wheat": "DAP",
        "maize": "NPK",
        "cotton": "Potash",
        "jute": "Compost"
    }

    return fertilizers.get(crop.lower(), "General Fertilizer")