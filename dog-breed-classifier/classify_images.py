from classifier import classifier 

def classify_images(images_dir, results_dic, model):

    for image_file in results_dic:
        classifier_label = classifier(images_dir + image_file, model).lower().strip()
        #results_dic[key].append(classifier_label)
        real_label = results_dic[image_file][0]
        # Compare the pet image and classifier labels to determine if they match.
        prediction = 1 if real_label in classifier_label else 0
        # Add the results to the results dictionary (results_dic).
        results_dic[image_file].append(classifier_label)
        results_dic[image_file].append(prediction)
    
    return None
