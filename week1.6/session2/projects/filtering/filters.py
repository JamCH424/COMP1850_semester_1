from image import Image

def blur(img):
    # Create a new image with the same dimensions
    result = Image.create(img.width, img.height, maximum=img.max_value)

    # Go through each pixel, excluding the edges
    for row in range(1, img.height - 1):
        for col in range(1, img.width - 1):

            total = 0

            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    total += img.get(r, c)

            # Calculate average
            average = total // 9

            # Store the result
            result.set(row, col, average)

    return result

img = Image.read("../../images/coins.pgm")
#img = Image.read("/workspaces/COMP1850_semester_1/week1.6/session2/images/coins.pgm")
result = blur(img)
result.write_pgm("blurred.pgm")
