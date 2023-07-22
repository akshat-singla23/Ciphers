def encrypt(plaintext, row_key, col_key):
    num_rows = (len(plaintext) + int(row_key[0]) - 1) // int(row_key[0])
    num_cols = (len(plaintext) + len(col_key) - 1) // len(col_key)

    # Pad the plaintext with spaces to fill out the grid
    plaintext += ' ' * (num_rows * len(row_key) * num_cols - len(plaintext))

    # Break the plaintext into a grid
    grid = [[plaintext[r * num_cols + c] for c in range(len(col_key))] for r in range(num_rows)]

    # Apply the row and column transpositions
    try:
        row_map = {row_key[i]: i for i in range(len(row_key))}
        col_map = {col_key[i]: i for i in range(len(col_key))}
    except IndexError:
        print("Invalid row or column key!")
        return None

    try:
        grid = [[grid[row_map[r]][col_map[c]] for c in range(len(col_key))] for r in range(len(row_key))]
    except IndexError:
        print("Invalid row or column key!")
        return None

    # Convert the grid back into a string
    ciphertext = ''.join([''.join(row) for row in grid])

    return ciphertext


def decrypt(ciphertext, row_key, col_key):
    # create a 2D grid to hold the ciphertext characters
    num_rows = len(ciphertext) // len(col_key)
    grid = [[ciphertext[i * len(col_key) + j] for j in range(len(col_key))] for i in range(num_rows)]

    # un-shuffle the rows and columns of the grid based on the given keys
    try:
        row_map = {row_key[i]: i for i in range(len(row_key))}
        col_map = {col_key[i]: i for i in range(len(col_key))}
    except IndexError:
        print("Invalid row or column key!")
        return None

    try:
        rows = [grid[row_map[r]] for r in range(len(row_key))]
        cols = [list(x) for x in zip(*rows)]
        plaintext = ''.join([cols[col_map[c]][row_map[r]] for r in range(len(row_key)) for c in range(len(col_key))])
    except IndexError:
        print("Invalid row or column key!")
        return None

    # return the un-shuffled grid as a flattened list
    return plaintext


# example usage
plaintext = 'hellokashika'
row_key = [2, 0, 1, 3]
col_key = [3, 1, 0, 2]

ciphertext = encrypt(plaintext, row_key, col_key)
if ciphertext is not None:
    print('Ciphertext:', ciphertext)
    decrypted_plaintext = decrypt(ciphertext, row_key, col_key)
    if decrypted_plaintext is not None:
        print('Decrypted plaintext:', decrypted_plaintext)
