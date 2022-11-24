from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(image.__len__()):
            image[i] = image[i][::-1]
            for j in range(image[i].__len__()):
                image[i][j] = int(not image[i][j])
        return image
