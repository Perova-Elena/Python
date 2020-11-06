source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
generated_list = [el for i, el in enumerate(source_list)
                  if source_list[i] > source_list[i-1] and i != 0]
print(generated_list)