import argparse

import numpy 
import numpy as np

import spherecluster.util



def main(kappas, dims, samples, saveto):

    for kp in kappas:
        for di in dims:
            for sn in samples:
                print('Sampling {} {} {} ... '.format(kp, di, sn), end="")
                fname = '{}/samples_{}_{}_{}.txt'.format(saveto, kp, di, sn)

                direction = np.zeros((di))
                direction[0] = 1.

                ss = spherecluster.util.sample_vMF(direction, kp, sn)

                numpy.savetxt(fname, ss)
                print("Done")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('kappas', type=str)
    parser.add_argument('dims', type=str)
    parser.add_argument('samples', type=str)
    parser.add_argument('saveto', type=str)

    args = parser.parse_args()

    kappas = [float(n) for n in args.kappas.split(',')]
    dims = [int(n) for n in args.dims.split(',')]
    samples = [int(n) for n in args.samples.split(',')]

    main(kappas, dims, samples, args.saveto)

