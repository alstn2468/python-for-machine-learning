import numpy as np

def n_size_ndarray_creation(n, dtype = np.int) :

def zero_or_one_or_empty_ndarray(shape, type = 0, dtype = np.int) :

def change_shape_of_ndarray(X, n_row) :

def concat_ndarray(X_1, X_2, axis) :

def normalize_ndarray(X, axis = 99, dtype = np.float32) :

def save_ndarray(X, filename = "test.npy") :

def boolean_index(X, condition) :

def find_nearest_value(X, target_value) :

def get_n_largest_values(X, n) :


if __name__ == '__main__' :

    # zero_or_one_or_empty_ndarray test
    print(zero_or_one_or_empty_ndarray(shape = (2, 2), type = 1)
    print(zero_or_one_or_empty_ndarray(shape = (3, 3), type = 99))


    # change_shape_of_ndarray test
    X = np.ones((32, 32), dtype = np.int)

    print(change_shape_of_ndarray(X, 1))
    print(change_shape_of_ndarray(X, 512))


    # concat_ndarray test
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6]])

    print(concat_ndarray(a, b, 0))
    print(concat_ndarray(a, b, 1))

    a = np.array([1, 2])
    b = np.array([5, 6, 7])

    print(concat_ndarray(a, b, 1))
    print(concat_ndarray(a, b, 0))


    # normalize_ndarray test
    X = np.arange(12, dtype = np.float32).reshape(6, 2)

    print(normalize_ndarray(X))
    print(normalize_ndarray(X, 1))
    print(normalize_ndarray(X, 0))


    # save_ndarray test
    X = np.arange(32, dtype = np.float32).reshape(4, -1)
    filename = "test.npy"
    save_ndarray(X, filename)


    # boolean_index test
    X = np.arange(32, dtype = np.float32).reshape(4, -1)
    print(boolean_index(X, 'x == 3'))

    X = np.arange(32, dtype = np.float32)
    print(boolean_index(X, "> 6"))


    # find_nearest_value test
    X = np.random.uniform(0, 1, 100)
    target_value = 0.3

    print(find_nearest_value(X, target_value))


    # get_n_largest_values test
    X = np.random.uniform(0, 1, 100)

    get_n_largest_values(X, 3)
    get_n_largest_values(X, 5)
