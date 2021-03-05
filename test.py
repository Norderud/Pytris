def rotate(arr, center):
    new_shape = []
    center_cell = shape[center]
    x_offset = center_cell[0] - (-center_cell[1])
    y_offset = center_cell[1] - center_cell[0]

    for cell in shape:
        temp = cell[0]  + y_offset
        new_x = -cell[1]  + x_offset
        new_y = temp
        new_shape.extend([[new_x, new_y]])
    return new_shape


# shape = [[1, 1], [1, 2], [1, 3], [2, 3]]
shape = [[5, 10], [5, 11], [5, 12], [6, 12]]

new_shape = rotate(shape, 2)

print(shape)
print(new_shape)



