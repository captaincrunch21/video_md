def grayscale(image,size):
    # print(image[30, 30],"aaa", size)
    m = size[0]
    n = size[1]
    a = [0 for _ in range(m)]
    array = [a.copy() for _ in range(n)]
    # print(len(array),len(a),size)
    for i in range(n):
        for j in range(m):
            # print(image[i, j])
            red, green, blue = image[j, i]
            gray = red * 0.3 + green * 0.59 + blue * 0.11
            array[i][j] = gray
    return array
a_lap=[0,-1,0,-1,4,-1,0,-1,0]
a_mean=[1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9]
def filter(image_array,tag='l'):
    m = len(image_array)
    n = len(image_array[0])
    a = [0 for _ in range(n)]
    array = [a.copy() for _ in range(m)]
    if tag=='l':

        for image_row in range(m):
            for image_col in range(n):
                pix_range_i = [-1,-1,-1,0,0,0,1,1,1]
                pix_range_j = [-1,0,1,-1,0,1,-1,0,1]
                filter_pointer = 0
                filtered_pixel_value = 0
                for i , j in zip(pix_range_i,pix_range_j):
                    try:
                        filtered_pixel_value+=image_array[image_row+i,image_col+j] * a_lap[filter_pointer]
                        filter_pointer+=1
                    except:
                        filter_pointer+=1
                array[image_row][image_col]=filtered_pixel_value
                filter_pointer = 0
        return array
    if tag=='f':

        for image_row in range(m):
            for image_col in range(n):
                pix_range_i = [-1,-1,-1,0,0,0,1,1,1]
                pix_range_j = [-1,0,1,-1,0,1,-1,0,1]
                filter_pointer = 0
                filtered_pixel_value = 0
                for i , j in zip(pix_range_i,pix_range_j):
                    try:
                        filtered_pixel_value+=image_array[image_row+i,image_col+j] * a_mean[filter_pointer]
                        filter_pointer+=1
                    except:
                        filter_pointer+=1
                array[image_row][image_col]=filtered_pixel_value
                filter_pointer = 0
        return array




