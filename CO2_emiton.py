from abc import ABC, abstractmethod


class PowerPlant(ABC):
    def __init__(self, watt):
        self.watt = watt
        self.co2 = 0
        self.renewable_unit = 0

    @abstractmethod
    def co2_output(self):
        pass


class Coal(PowerPlant):
    CO2_RATE = 50

    def __init__(self, watt):
        super().__init__(watt)
        self.co2_output()

    def co2_output(self):
        self.co2 = self.watt / Coal.CO2_RATE


class Solar(PowerPlant):

    def __init__(self, watt):
        super().__init__(watt)
        self.renewable_unit = 1

    def co2_output(self):
        self.co2 = 0


class PowerResources:

    def __init__(self):
        self.power_list = []

    def add_energy_resource(self, parametre):
        self.power_list.append(parametre)

    @property
    def total_watts_calculation(self):
        return sum(x.watt for x in self.power_list)

    @property
    def total_co2_calculation(self):
        return sum(x.co2 for x in self.power_list)

    @property
    def total_renewable_unit_calculation(self):
        return sum(x.renewable_unit for x in self.power_list)

    def remove_obj(self, index_num):
        del self.power_list[index_num]

    def __str__(self):
        return 'Total Watts:{:.2f}\nTotal Renewable units:{:.2f}\nCO2 Output:{:.2f}' \
            .format(self.total_watts_calculation, self.total_renewable_unit_calculation,
                    self.total_co2_calculation)


power_resources = PowerResources()


def PowerResourcesTotal():
    power_resources.total_watts_calculation
    power_resources.total_co2_calculation
    power_resources.total_renewable_unit_calculation

    print(power_resources, '\n-------')


def TypesOfListedEnergyResources(power_list):
    for x in range(len(power_list)):
        if power_list[x].co2 == 0:
            print('{:d}: Solar power plant with {:d} watts'.format(x, power_list[x].watt))
        else:
            print('{:d}: Coal power plant with {:d} watts'.format(x, power_list[x].watt))


while True:
    x_input = input('(A)dd power plant, (R)emove power plant, e(X)it:')

    if x_input == 'A':
        type_of_power_plant = input('(C)oal or (S)olar:')
        watt_input = int(input('How many watts:'))

        if type_of_power_plant == 'C':
            resource_1 = Coal(watt_input)

        elif type_of_power_plant == 'S':
            resource_1 = Solar(watt_input)

        power_resources.add_energy_resource(resource_1)
        TypesOfListedEnergyResources(power_resources.power_list)
        PowerResourcesTotal()

    elif x_input == 'R':
        index_of_remove_power_plant = int(input('Index of power plant:'))
        power_resources.remove_obj(index_of_remove_power_plant)
        TypesOfListedEnergyResources(power_resources.power_list)
        PowerResourcesTotal()

    elif x_input == 'X':
        TypesOfListedEnergyResources(power_resources.power_list)
        PowerResourcesTotal()
        break