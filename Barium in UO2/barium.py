import numpy as np
from srim.output import Results
import os
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 14})
N = 2000 # number of particules
fluence = 1e+17 #cm-2, fluence during one year
density = 7.332E+22 # atoms/cm3
modify_range = False
modify_coll = False
res_path = os.getcwd()
new_path = res_path + '\srim_output'
data = Results(new_path)


def plot_collision(res, fluence, c, mod):
    """
    Plot the collision events graph.
    """
    if mod:
        vacancies = res.vacancy
        fig, ax = plt.subplots()
        ax.set_xlabel(r'Depth ($\mu$m)')
        ax.set_ylabel(r'Number/$\AA$')
        ax.plot(vacancies.depth / 1e+4, vacancies.knock_ons, label='Knock-ons')
        ax.plot(vacancies.depth / 1e+4, vacancies.vacancies, label='Vacancies')
        plt.legend()
        plt.tight_layout()
        fig.savefig('collisions.pdf')
        plt.close(fig)
    else:
        vacancies = res.vacancy
        fig, ax = plt.subplots()
        ax.set_xlabel(r'Depth ($\mu$m)')
        ax.set_ylabel(r'DPA')
        DPA = (vacancies.knock_ons + vacancies.vacancies.sum(axis=1)) * fluence * 1e+8 / c
        ax.plot(vacancies.depth / 1e+4, DPA, label='Atoms displaced')
        print("Max of DPA is "+str(np.max(DPA)))
        print("At ten nanometers "+str(DPA[1]))
        plt.legend()
        plt.tight_layout()
        fig.savefig('collisions.pdf')
        plt.close(fig)

plot_collision(data, fluence, density, modify_coll)
