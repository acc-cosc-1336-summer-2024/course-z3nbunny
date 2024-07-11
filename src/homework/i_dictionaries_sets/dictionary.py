#
#
def get_p_distance(list1, list2):

    differences = 0
    list_length = len(list1)

    for i in range(list_length):
        if list1[i] != list2[i]:
            differences +=1
    p_distance = differences / list_length
    return p_distance

def get_p_distance_matrix(list1):

    list_length = len(list1)

    p_distance_matrix = []

    for i in range(list_length):
        row = [0] * list_length
        p_distance_matrix.append(row)
    
    for i in range(list_length):
        for j in range(list_length):
            if i != j:
                p_distance_matrix[i][j] = get_p_distance(list1[i], list1[j])
            else:
                p_distance_matrix[i][j] = 0.0
    
    return p_distance_matrix