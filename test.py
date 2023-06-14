import os
import numpy as np


def main():
    filename = 'zero123/views_whole_sphere/0a00b69cc98b45ab9fdd02cf86729909/001.npy'
    RT = np.load(filename)
    print('RT from npy: ' + str(RT))
    # cond_RT = np.load(filename)
    R, T = RT[:3, :3], RT[:, -1]
    print('R: ' + str(R))
    print('T: ' + str(T))


if __name__ == "__main__":
    main()