cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeep_string = ""
    for value in cars["Jeep"]:
        jeep_string += value + ", "
    return jeep_string[:-2]


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_mod = []
    for key in cars.keys():
        first_mod.append(cars[key][0])
    return first_mod


def get_all_matching_models(cars=cars, grep="trail"):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    trail_list = []
    for make in cars.keys():
        for model in cars[make]:
            if grep.lower() in model.lower():
                trail_list.append(model)
    trail_list.sort()
    return trail_list


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    alpha_cars = {}
    for key in cars.keys():
        cars[key].sort()
        alpha_cars[key] = cars[key]
    return alpha_cars


if __name__ == "__main__":
    # get_all_matching_models()
    sort_car_models()
