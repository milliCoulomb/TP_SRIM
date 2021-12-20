import numpy as np
from srim.output import Results
import os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

linestyles = lss = [
    ('solid', (0, ())),

    # ('loosely dotted', (0, (1, 10))),
    ('dotted', (0, (1, 1))),
    ('densely dotted', (0, (1, 1))),

    # ('loosely dashed', (0, (5, 10))),
    ('dashed', (0, (5, 5))),
    ('densely dashed', (0, (5, 1))),

    ('loosely dashdotted', (0, (3, 10, 1, 10))),
    ('dashdotted', (0, (3, 5, 1, 5))),
    ('densely dashdotted', (0, (3, 1, 1, 1))),

    ('dashdotdotted', (0, (3, 5, 1, 5, 1, 5))),
    ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
    ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]

plt.rcParams.update({'font.size': 14})
N = 10000
fluence = 1e+16 #cm-2
density = 7.332E+22 # atoms/cm3
modify_range = False
modify_coll = False
res_path = os.getcwd()
new_path = res_path + '\srim_output'
# print(res_path)
# print('C:\\Users\\Mathis\\Desktop\\TP_SRIM\\Alpha in UO2\\srim_output')
# print(new_path)
# print(res_path+'\srim_output')
# data = Results('C:\\Users\\Mathis\\Desktop\\TP_SRIM\\Alpha in UO2\\srim_output')
data = Results(new_path)


def plot_ioniz(res):
    """
    Plot the ionization due to electronic and ballistic interactions.
    """
    ioniz = res.ioniz
    fig, ax = plt.subplots()
    ax.set_xlabel(r'Depth ($\AA$)')
    ax.set_ylabel(r'eV/$\AA$')
    ax.plot(ioniz.depth, ioniz.ions, label='Ionization from Ions')
    ax.plot(ioniz.depth, ioniz.recoils, label='Ionization from Recoils')
    plt.legend()
    plt.tight_layout()
    fig.savefig('ionization.pdf')
    plt.close(fig)


def plot_etorecoils(res):
    """
    Plot the energy transfered from recoils.
    """
    etorecoils = res.etorecoils
    fig, ax = plt.subplots()
    ax.set_xlabel(r'Depth ($\AA$)')
    ax.set_ylabel(r'eV/$\AA$')
    ax.plot(etorecoils.depth, etorecoils.ions, label='Energy from Ions')
    plt.legend()
    plt.tight_layout()
    fig.savefig('etorecoils.pdf')
    plt.close(fig)


def plot_range(res, fluence, mod):
    """
    Plot the distribution of incorporated projectiles.
    """
    if mod:
        range = res.range
        fig, ax = plt.subplots()
        ax.set_xlabel(r'Depth ($\AA$)')
        ax.set_ylabel(r'Atoms/cm3 / Atoms / cm2')
        ax.plot(range.depth, range.ions, label='Ions range')
        plt.legend()
        plt.tight_layout()
        fig.savefig('range.pdf')
        plt.close(fig)
    else:
        range = res.range
        fig, ax = plt.subplots()
        ax.set_xlabel(r'Depth ($\AA$)')
        ax.set_ylabel(r'He/cm3')
        ax.plot(range.depth, range.ions * fluence, label='Concentration of He')
        print("Max of concentration of He = "+"{:e}".format(np.max(range.ions * fluence))+" cm3")
        plt.legend()
        plt.tight_layout()
        fig.savefig('range.pdf')
        plt.close(fig)


def plot_collision(res, fluence, c, mod):
    """
    Plot the collision events graph.
    """
    if mod:
        vacancies = res.vacancy
        fig, ax = plt.subplots()
        ax.set_xlabel(r'Depth ($\AA$)')
        ax.set_ylabel(r'Number/$\AA$')
        ax.plot(vacancies.depth, vacancies.knock_ons, label='Knock-ons')
        ax.plot(vacancies.depth, vacancies.vacancies, label='Vacancies')
        plt.legend()
        plt.tight_layout()
        fig.savefig('collisions.pdf')
        plt.close(fig)
    else:
        vacancies = res.vacancy
        fig, ax = plt.subplots()
        ax.set_xlabel(r'Depth ($\AA$)')
        ax.set_ylabel(r'DPA')
        DPA = vacancies.knock_ons * fluence * 1e+8 / c
        ax.plot(vacancies.depth, DPA, label='Atoms displaced')
        print("Max of DPA is "+str(np.max(DPA)))
        print("At ten nanometers "+str(DPA[1]))
        # ax.plot(vacancies.depth, vacancies.vacancies, label='Vacancies')
        plt.legend()
        plt.tight_layout()
        fig.savefig('collisions.pdf')
        plt.close(fig)

Rp = 903.2e+2 / 1e+4
std_Rp = 465.7e+1 / 1e+4
#mean_range = np.mean(data.range)
#std_range = np.std(data.range)
err = std_Rp / np.sqrt(N)
print('Range of the projectile in matter, Rp='+"{:e}".format(Rp)+"+-"+"{:e}".format(err)+" micrometers")

plot_ioniz(data)
plot_etorecoils(data)
plot_range(data, fluence, modify_range)
plot_collision(data, fluence, density, modify_coll)
